import os
import json
from wick_reversal.WickReversalOrderBot import WickReversalOrderBot
from wick_reversal.ThreeLineOrderBot import ThreeLineOrdergBot

def main():   
    wick_reversal_config_path = os.getenv('config_path','config.json')
    
    with open(wick_reversal_config_path, 'r') as f:
        config_data = json.load(f)
        
    platform_config = config_data['okx']
    feishu_webhook_url = config_data['feishu_webhook']
    # monitor_interval = config_data.get("monitor_interval", 4)  # 默认值为60秒

    bot = WickReversalOrderBot(config_data,platform_config, feishu_webhook=feishu_webhook_url)
    # bot =ThreeLineOrdergBot(config_data,platform_config, feishu_webhook=feishu_webhook_url)
    bot.monitor_klines()

if __name__ == "__main__":
    main()
