
import requests

def check_token_rug(token_address):
    try:
        response = requests.get(f"https://api.rugcheck.xyz/{token_address}")
        if response.status_code == 200:
            data = response.json()
            return {
                "score": data.get("score", 0),
                "rug": data.get("is_rug", True)
            }
    except Exception as e:
        print("RugCheck Error:", e)
    return {"score": 0, "rug": True}
