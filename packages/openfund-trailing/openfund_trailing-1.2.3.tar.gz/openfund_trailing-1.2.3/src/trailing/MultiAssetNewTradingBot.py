# -*- coding: utf-8 -*-
import ccxt
import time
import logging
import requests
import json
import trailing.okx.Trade_api as TradeAPI
from logging.handlers import TimedRotatingFileHandler


class MultiAssetNewTradingBot:
    def __init__(self, config, feishu_webhook=None, monitor_interval=4):
        self.stop_loss_pct = config["all_stop_loss_pct"]  # 全局止损百分比
        
        # 止盈比例
        self.low_trail_stop_loss_pct = config["all_low_trail_stop_loss_pct"] # 第一档
        self.trail_stop_loss_pct = config["all_trail_stop_loss_pct"]# 第二档
        self.higher_trail_stop_loss_pct = config["all_higher_trail_stop_loss_pct"]# 第三档
        # 止盈阈值
        self.low_trail_profit_threshold = config["all_low_trail_profit_threshold"]# 第一档
        self.first_trail_profit_threshold = config["all_first_trail_profit_threshold"]# 第二档
        self.second_trail_profit_threshold = config["all_second_trail_profit_threshold"]# 第三档
        
        self.feishu_webhook = feishu_webhook
        self.monitor_interval = monitor_interval  # 监控循环时间是分仓监控的3倍
        self.highest_total_profit = 0  # 记录最高总盈利
        self.current_tier = "无"
        
        
        self.global_symbol_stop_loss_flag = {} # 记录每个symbol是否设置全局止损
        self.global_symbol_take_profit_price = {} # 记录每个symbol的止盈价格
        # 保留在止盈挂单中最高最低两个价格，计算止盈价格。
        self.max_market_price = 0.0
        self.min_market_price = float('inf')  # 初始化为浮点数最大值

        # 配置交易所
        self.exchange = ccxt.okx({
            'apiKey': config["apiKey"],
            'secret': config["secret"],
            'password': config["password"],
            'timeout': 3000,
            'rateLimit': 50,
            'options': {'defaultType': 'future'},
            'proxies': {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'},
        })

        # 配置 OKX 第三方库
        # self.trading_bot = TradeAPI.TradeAPI(config["apiKey"], config["secret"], config["password"], False, '0')

        # 配置日志
        log_file = "log/okx_MultiAssetNewTradingBot.log"
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7, encoding='utf-8')
        file_handler.suffix = "%Y-%m-%d"
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        self.logger = logger
        self.position_mode = self.get_position_mode()  # 获取持仓模式

    def get_position_mode(self):
        try:
            # 假设获取账户持仓模式的 API
            response = self.exchange.private_get_account_config()
            data = response.get('data', [])
            if data and isinstance(data, list):
                # 取列表的第一个元素（假设它是一个字典），然后获取 'posMode'
                position_mode = data[0].get('posMode', 'single')  # 默认值为单向
                self.logger.info(f"当前持仓模式: {position_mode}")
                return position_mode
            else:
                self.logger.error("无法检测持仓模式: 'data' 字段为空或格式不正确")
                return 'single'  # 返回默认值
        except Exception as e:
            self.logger.error(f"无法检测持仓模式: {e}")
            return None

    def send_feishu_notification(self, message):
        if self.feishu_webhook:
            try:
                headers = {'Content-Type': 'application/json'}
                payload = {"msg_type": "text", "content": {"text": message}}
                response = requests.post(self.feishu_webhook, json=payload, headers=headers)
                if response.status_code == 200:
                    self.logger.info("飞书通知发送成功")
                else:
                    self.logger.error("飞书通知发送失败，状态码: %s", response.status_code)
            except Exception as e:
                self.logger.error("发送飞书通知时出现异常: %s", str(e))

    def fetch_positions(self):
        try:
            positions = self.exchange.fetch_positions()
            return positions
        except Exception as e:
            self.logger.error(f"Error fetching positions: {e}")
            return []

    # 获取当前委托
    def fetch_open_orders(self,symbol,params={}):
        try:
            orders = self.exchange.fetch_open_orders(symbol=symbol,params=params)
            return orders
        except Exception as e:
            self.logger.error(f"Error fetching open orders: {e}")
            return []

    # def cancel_all_orders(self,symbol):
    #     params = {}
    #     orders = self.fetch_open_orders(symbol=symbol,params=params)
    #     # 如果没有委托订单则直接返回
    #     if not orders:
    #         self.global_symbol_stop_loss_flag.clear()
    #         self.logger.debug(f"{symbol} 无挂单列表。")
    #         return
        
    #     # 提取所有订单ID，包括普通订单和策略订单
    #     order_ids = []
    #     for order in orders:
    #         # 处理订单ID
    #         if 'id' in order:
    #             order_ids.append(order['id'])

    #     try:
    #         # 批量取消订单
    #         self.exchange.cancel_orders(order_ids, symbol=symbol)
    #         self.logger.info(f"Orders {order_ids} cancelled for {symbol}")
    #     except Exception as e:
    #         self.logger.error(f"Error cancelling orders for {symbol}: {e}")

   # 计算平均利润
    def calculate_average_profit(self,symbol,position):
        # positions = self.fetch_positions()
        total_profit_pct = 0.0
        num_positions = 0

        entry_price = float(position['entryPrice'])
        current_price = float(position['markPrice'])
        side = position['side']

        # 计算单个仓位的浮动盈利百分比
        if side == 'long':
            profit_pct = (current_price - entry_price) / entry_price * 100
        elif side == 'short':
            profit_pct = (entry_price - current_price) / entry_price * 100
        else:
            return

        # 累加总盈利百分比
        total_profit_pct += profit_pct
        num_positions += 1

        # 记录单个仓位的盈利情况
        self.logger.info(f"仓位 {symbol}，方向: {side}，开仓价格: {entry_price}，当前价格: {current_price}，"
                            f"浮动盈亏: {profit_pct:.2f}%")

        # 计算平均浮动盈利百分比
        average_profit_pct = total_profit_pct / num_positions if num_positions > 0 else 0
        return average_profit_pct

    def reset_highest_profit_and_tier(self):
        """重置最高总盈利和当前档位状态"""
        self.highest_total_profit = 0
        self.current_tier = "无"
        self.global_symbol_stop_loss_flag.clear()
        # self.logger.debug("已重置最高总盈利和档位状态")
        
    def reset_take_profie(self):
        self.global_symbol_take_profit_price.clear()
        self.global_symbol_stop_loss_flag.clear()
        # 保留在止盈挂单中最高最低两个价格，计算止盈价格。
        self.max_market_price = 0.0
        self.min_market_price = float('inf')  # 初始化为浮点数最大值
        self.logger.debug("已重置止盈价格")
        
    def round_price_to_tick(self,symbol, price):
        tick_size = float(self.exchange.market(symbol)['info']['tickSz'])
        # 计算 tick_size 的小数位数
        tick_decimals = len(f"{tick_size:.10f}".rstrip('0').split('.')[1]) if '.' in f"{tick_size:.10f}" else 0

        # 调整价格为 tick_size 的整数倍
        adjusted_price = round(price / tick_size) * tick_size
        return f"{adjusted_price:.{tick_decimals}f}"
        # 放弃当前委托
    def cancel_all_algo_orders(self,symbol):
        
        params = {
            "ordType": "conditional",
        }
        orders = self.fetch_open_orders(symbol=symbol,params=params)
        # 如果没有委托订单则直接返回
        if not orders:
            self.global_symbol_stop_loss_flag.clear()
            self.logger.debug(f"{symbol} 未设置策略订单列表。")
            return
     
        algo_ids = [order['info']['algoId'] for order in orders if 'info' in order and 'algoId' in order['info']]
        try:
            params = {
                "algoId": algo_ids,
                "trigger": 'trigger'
            }
            rs = self.exchange.cancel_orders(ids=algo_ids, symbol=symbol, params=params)
            self.global_symbol_stop_loss_flag.clear()
            # self.logger.debug(f"Order {algo_ids} cancelled:{rs}")
        except Exception as e:
            self.logger.error(f"Error cancelling order {algo_ids}: {e}")
            
    def set_stop_loss_take_profit(self, symbol, position, stop_loss_price=None, take_profit_price=None):
        self.cancel_all_algo_orders(symbol=symbol)
        stop_params = {}
            
        if not position:
            self.logger.warn(f"No position found for {symbol}")
            return
            
        amount = abs(float(position['contracts']))
        
        if amount <= 0:
            self.logger.warn(f"amount is 0 for {symbol}")
            return

        adjusted_price = self.round_price_to_tick(symbol, stop_loss_price)
            
        # 设置止损单 ccxt 只支持单向（conditional）不支持双向下单（oco、conditional）
        if stop_loss_price:
            stop_params = {
                'slTriggerPx':adjusted_price , 
                'slOrdPx':'-1', # 委托价格为-1时，执行市价止损
                'slTriggerPxType':'mark',
                'tdMode':position['marginMode'],
                'sz': str(amount),
                # 'closeFraction': '1',
                'cxlOnClosePos': True,
                'reduceOnly':True
            }
            
            side = 'short' 
            if position['side'] == side: # 和持仓反向相反下单
                side ='long'
                
            orderSide = 'buy' if side == 'long' else 'sell'
         
            try:
                self.exchange.create_order(
                    symbol=symbol,
                    type='conditional',
                    # type='limit',
                    price=adjusted_price,
                    side=orderSide,
                    amount=amount,
                    params=stop_params
                )
                self.logger.debug(f"+++ Stop loss order set for {symbol} at {stop_loss_price}")
            except ccxt.NetworkError as e:
                # 处理网络相关错误
                self.logger.error(f"设置止损单时发生网络错误: {str(e)}")
                
            except ccxt.ExchangeError as e:
                # 处理交易所API相关错误
                self.logger.error(f"设置止损单时发生交易所错误: {str(e)}")
                
            except Exception as e:
                # 处理其他未预期的错误
                self.logger.error(f"设置止损单时发生未知错误: {str(e)}")
                
            
    def set_global_stop_loss(self, symbol, position, side, stop_loss_algo):
        """设置全局止损
        
        Args:
            symbol: 交易对
            position: 持仓信息
            side: 持仓方向
            stop_loss_algo: 止损算法信息
        """
        # 如果已经触发过全局止损并且有止损单，则跳过
        if self.global_symbol_stop_loss_flag.get(symbol, False):
            
            return
        else :
            self.logger.debug(f"{symbol} - 是否设置过全局止损 {self.global_symbol_stop_loss_flag.get(symbol, False)} 策略订单: {stop_loss_algo}")   
            
        # 根据持仓方向计算止损价格
        if side == 'long':
            stop_loss_price = position['entryPrice'] * (1 - self.stop_loss_pct/100)
        elif side == 'short': 
            stop_loss_price = position['entryPrice'] * (1 + self.stop_loss_pct/100)
            
        try:
            # 设置止损单
            self.set_stop_loss_take_profit(
                symbol=symbol,
                position=position,
                stop_loss_price=stop_loss_price
            )
            self.logger.debug(f"{symbol} - {side} 设置全局止损价: {stop_loss_price}")
            
            # 设置全局止损标志
            self.global_symbol_stop_loss_flag[symbol] = True
                
        except Exception as e:
            error_msg = f"{symbol} - 设置止损时发生错误: {str(e)}"
            self.logger.error(error_msg)
            self.send_feishu_notification(error_msg)  
    
    def calculate_take_profit_price(self, symbol, position, stop_loss_pct, offset=1) -> float:
        tick_size = float(self.exchange.market(symbol)['precision']['price'])
        market_price = position['markPrice']
        entry_price = position['entryPrice']
        side = position['side']
        # base_price = abs(market_price-entry_price) * (1-stop_loss_pct)
        # 计算止盈价格，用市场价格（取持仓期间历史最高）减去开仓价格的利润，再乘以不同阶段的止盈百分比。
        if side == 'long':
            self.max_market_price = max(market_price,self.max_market_price)
            base_price = abs(self.max_market_price - entry_price) * (1-stop_loss_pct)
            take_profit_price = entry_price + base_price - offset * tick_size

        elif side == 'short':
            self.min_market_price = min(market_price,self.min_market_price)
            base_price = abs(self.min_market_price - entry_price) * (1-stop_loss_pct)
            take_profit_price = entry_price - base_price + offset * tick_size
        
          
        return float(take_profit_price )
    
    def close_position(self, symbol, position):
        total_profit = self.calculate_average_profit(symbol, position)
        if total_profit > 0.0 :
            self.logger.info(f"{symbol} 当前总盈利: {total_profit:.2f}%")
            self.send_feishu_notification(f"{symbol} 当前总盈利: {total_profit:.2f}%")
        if total_profit > self.highest_total_profit:
            self.highest_total_profit = total_profit
        # 确定当前盈利档位
        if self.highest_total_profit >= self.second_trail_profit_threshold:
            self.current_tier = "第二档移动止盈"
     
        elif self.highest_total_profit >= self.first_trail_profit_threshold:
            self.current_tier = "第一档移动止盈"
         
        elif self.highest_total_profit >= self.low_trail_profit_threshold:
            self.current_tier = "低档保护止盈"
            
            
        if total_profit > 0.0 :
            self.logger.info(
                f"当前总盈利: {total_profit:.2f}%，最高总盈利: {self.highest_total_profit:.2f}%，当前档位: {self.current_tier}")
            self.send_feishu_notification(
                f"当前总盈利: {total_profit:.2f}%，最高总盈利: {self.highest_total_profit:.2f}%，当前档位: {self.current_tier}")
                
        '''
        第一档 低档保护止盈:当盈利达到0.3%触发,要么到第二档,要么回到0.2%止盈
        第二档:盈利达到1%触发,记录最高价,最高价的80%是止盈位
        第三档:盈利达到3%触发,记录最高价,最高价的75%是止盈位
        '''
        # 各档止盈逻辑
           
        if self.current_tier == "低档保护止盈":
            self.logger.info(f"低档回撤止盈阈值: {self.low_trail_stop_loss_pct:.2f}%")
            if total_profit >= self.low_trail_stop_loss_pct:
                
                take_profit_price = self.calculate_take_profit_price(symbol=symbol, position=position,stop_loss_pct=self.low_trail_stop_loss_pct )
                # 判断止盈价格是否变化，无变化不需要设置
                latest_take_profit_price = self.exchange.safe_float(self.global_symbol_take_profit_price,symbol,0.0)
                if take_profit_price == latest_take_profit_price:
                    self.logger.debug(f"{symbol} 止盈价格未变化，不设置")
                    return 
                self.logger.info(f"总盈利触发低档保护止盈，当前回撤到: {total_profit:.2f}%，市场价格:{position['markPrice']},设置止盈位: {take_profit_price:.9f}")
                self.set_stop_loss_take_profit(symbol, position, stop_loss_price=take_profit_price)
                self.global_symbol_take_profit_price[symbol] = take_profit_price
                self.reset_highest_profit_and_tier()
                self.send_feishu_notification(f"总盈利触发低档保护止盈，当前回撤到: {total_profit:.2f}%，市场价格:{position['markPrice']},设置止盈位: {take_profit_price:.9f}")
                return
        elif self.current_tier == "第一档移动止盈":
            trail_stop_loss = self.highest_total_profit * (1 - self.trail_stop_loss_pct)
            self.logger.info(f"第一档回撤止盈阈值: {trail_stop_loss:.2f}%")
            if total_profit >= trail_stop_loss:
                take_profit_price = self.calculate_take_profit_price(symbol=symbol, position=position,stop_loss_pct=self.trail_stop_loss_pct )                
                # 判断止盈价格是否变化，无变化不需要设置
                latest_take_profit_price = self.exchange.safe_float(self.global_symbol_take_profit_price,symbol,0.0)
                if take_profit_price == latest_take_profit_price :
                    self.logger.debug(f"{symbol} 止盈价格未变化，不设置")
                    return  
                self.logger.info(
                    f"总盈利达到第一档回撤阈值，最高总盈利: {self.highest_total_profit:.2f}%,当前回撤到: {total_profit:.2f}%，市场价格: {position['markPrice']},设置止盈位: {take_profit_price:.9f}")
                self.set_stop_loss_take_profit(symbol, position, stop_loss_price=take_profit_price)
                # 记录一下止盈价格
                self.global_symbol_take_profit_price[symbol] = float(take_profit_price)
                self.reset_highest_profit_and_tier()
                
                self.send_feishu_notification(
                    f"总盈利达到第一档回撤阈值，最高总盈利: {self.highest_total_profit:.2f}%，当前回撤到: {total_profit:.2f}%，市场价格: {position['markPrice']}, 设置止盈位: {take_profit_price:.9f}")
                return 

        elif self.current_tier == "第二档移动止盈":
            trail_stop_loss = self.highest_total_profit * (1 - self.higher_trail_stop_loss_pct)
            self.logger.info(f"第二档回撤止盈阈值: {trail_stop_loss:.2f}%")
            if total_profit >= trail_stop_loss:
                take_profit_price = self.calculate_take_profit_price(symbol=symbol, position=position,stop_loss_pct=self.higher_trail_stop_loss_pct)                
                # 判断止盈价格是否变化，无变化不需要设置
                latest_take_profit_price = self.exchange.safe_float(self.global_symbol_take_profit_price,symbol,0.0)
                if take_profit_price == latest_take_profit_price:
                    self.logger.debug(f"{symbol} 止盈价格未变化，不设置")
                    return   
                self.logger.info(f"总盈利达到第二档回撤阈值，最高总盈利: {self.highest_total_profit:.2f}%，当前回撤到: {total_profit:.2f}%，市场价格: {position['markPrice']},设置止盈位: {take_profit_price:.9f}")
                self.set_stop_loss_take_profit(symbol, position, stop_loss_price=take_profit_price)
                # 记录一下止盈价格
                self.global_symbol_take_profit_price[symbol] = take_profit_price
                self.reset_highest_profit_and_tier()
                self.send_feishu_notification(f"总盈利达到第二档回撤阈值，最高总盈利: {self.highest_total_profit:.2f}%，当前回撤到: {total_profit:.2f}%，市场价格: {position['markPrice']},设置止盈位: {take_profit_price:.9f}")
                return 
        else :
            self.logger.info(f"全局止损阈值: {self.stop_loss_pct:.2f}%")
            stop_loss_algo = position['info']['closeOrderAlgo']
            side = position['side']
            self.set_global_stop_loss(symbol, position, side, stop_loss_algo)
            return


    def monitor_total_profit(self):
        self.logger.info("启动主循环，开始监控总盈利...")
        previous_position_size = sum(
            abs(float(position['contracts'])) for position in self.fetch_positions())  # 初始总仓位大小
        while True:
            try:
                positions = self.fetch_positions()
                # 检查是否有仓位
                if not positions:
                    # self.logger.debug("没有持仓，等待下一次检查...")
                    self.reset_highest_profit_and_tier()
                    self.reset_take_profie()
                    time.sleep(1)
                    continue
                # 检查仓位总规模变化
                current_position_size = sum(abs(float(position['contracts'])) for position in self.fetch_positions())
                if current_position_size > previous_position_size:
                    self.send_feishu_notification(f"检测到仓位变化操作，重置最高盈利和档位状态")
                    self.logger.info("检测到新增仓位操作，重置最高盈利和档位状态")
                    self.reset_highest_profit_and_tier()
                    previous_position_size = current_position_size
                    time.sleep(0.1)
                    continue  # 跳过本次循环
                
          

                for position in positions:
                    symbol = position['symbol']
                    self.close_position(symbol, position)


                time.sleep(self.monitor_interval)

            except Exception as e:
                error_message = f"程序异常退出: {str(e)}"
                self.logger.error(error_message)
                self.send_feishu_notification(error_message)
                continue
            except KeyboardInterrupt:
                self.logger.info("程序收到中断信号，开始退出...")
                break

