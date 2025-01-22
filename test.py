from telethon import TelegramClient, events

# Настройки API
api_id = 21078867  # Ваш API ID
api_hash = "95e80b6bea78c5b0c5442702c8cc17de"  # Ваш API Hash
session_name = "session_user"  # Имя файла сессии

# ID канала
source_channel_id = -1002361161091  # ID канала-источника

# Инициализация клиента
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel_id))
async def handler(event):
    # Выводим полную информацию о сообщении
    print(event.message.to_dict())  # Это покажет все параметры сообщения

# Запуск клиента
print("Ожидаем новые сообщения...")
client.start()
client.run_until_disconnected()
