
import time
from filters import is_token_valid
from rugcheck import check_token_rug
from telegram_alerts import send_alert
from execution import execute_buy
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

def get_new_tokens():
    # Здесь будет интеграция с Dexscreener или PumpFun API
    return [{"name": "TestToken", "address": "0x123", "volume": 10000, "liquidity": 5000}]

if __name__ == '__main__':
    print("PumpFun Sniper Bot started...")
    while True:
        tokens = get_new_tokens()
        for token in tokens:
            if is_token_valid(token):
                rug_data = check_token_rug(token["address"])
                if rug_data and not rug_data["rug"]:
                    send_alert(f"Found safe token: {token['name']}")
                    execute_buy(token)
        time.sleep(10)
