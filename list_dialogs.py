from telethon import TelegramClient

# Настройки API
api_id = 21078867  # Ваш API ID
api_hash = "95e80b6bea78c5b0c5442702c8cc17de"  # Ваш API Hash
session_name = "session_user"  # Имя файла сессии

# Инициализация клиента
client = TelegramClient(session_name, api_id, api_hash)

async def print_dialogs():
    async for dialog in client.iter_dialogs():
        print(f"Название: {dialog.name}, ID: {dialog.id}")

with client:
    client.loop.run_until_complete(print_dialogs())
