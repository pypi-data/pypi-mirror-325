import os
import json
from trailing.MultiAssetTradingBot import MultiAssetTradingBot
from trailing.MultiAssetNewTradingBot import MultiAssetNewTradingBot
from trailing.ThreeLineTradingBot import ThreeLineTradingBot

def main():
    # os.environ["ENV"] = env
    # os.environ["DEBUG"] = str(debug)
    openfund_config_path = os.getenv('openfund_config_path','config.json')
    
    with open(openfund_config_path, 'r') as f:
        config_data = json.load(f)
        
    platform_config = config_data['okx']
    feishu_webhook_url = config_data['feishu_webhook']
    monitor_interval = config_data.get("monitor_interval", 60)  # 默认值为60秒

    # bot = MultiAssetTradingBot(platform_config, feishu_webhook=feishu_webhook_url, monitor_interval=monitor_interval)
    # bot.monitor_total_profit()
    bot = MultiAssetNewTradingBot(platform_config, feishu_webhook=feishu_webhook_url, monitor_interval=monitor_interval)
    bot.monitor_total_profit()
    # bot = ThreeLineTradingBot(platform_config, feishu_webhook=feishu_webhook_url, monitor_interval=monitor_interval)
    # bot.monitor_klines()

if __name__ == "__main__":
    main()
