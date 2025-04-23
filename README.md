
# PumpFun Sniper Bot

## Установка

```bash
git clone https://github.com/Andrey4682/pumpfun-sniper-bot.git
cd pumpfun-sniper-bot
pip install -r requirements.txt
```

## Настройка

Создайте файл `config.yaml`:

```yaml
telegram_token: 'ВАШ_ТЕЛЕГРАМ_БОТ_ТОКЕН'
chat_id: 'ВАШ_CHAT_ID'
blacklist: []
```

## Запуск

```bash
python bot.py
```

## Возможности

- Отслеживание новых токенов
- Проверка объема/ликвидности
- Проверка через RugCheck
- Telegram-уведомления
- Поддержка BonkBot/Trojan
