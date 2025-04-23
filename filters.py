
def is_token_valid(token):
    # Примитивная проверка объема
    if token["volume"] < 5000:
        return False
    # Примитивная проверка ликвидности
    if token["liquidity"] < 1000:
        return False
    return True
