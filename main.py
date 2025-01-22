from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

# Получаем данные из переменных окружения
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")

# Инициализация клиента
client = TelegramClient(StringSession(string_session), api_id, api_hash)

# ID каналов
source_channel_id = int(os.getenv("SOURCE_CHANNEL_ID"))  # Канал-источник
target_channel_id = int(os.getenv("TARGET_CHANNEL_ID"))  # Целевая группа

# ID разделов, которые нужно пересылать
allowed_topics = [3, 5, 6, 976, 1986, 736]  # Указанные ID разделов

@client.on(events.NewMessage(chats=source_channel_id))
async def handler(event):
    message = event.message
    reply_to = message.reply_to

    # Проверяем, есть ли привязка к теме
    if reply_to and reply_to.reply_to_top_id:
        topic_id = reply_to.reply_to_top_id
        if topic_id in allowed_topics:
            try:
                await client.send_message(target_channel_id, message.text)
                print(f"Сообщение из раздела {topic_id} отправлено: {message.text}")
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")
        else:
            print(f"Пропущено: сообщение из раздела {topic_id}")
    else:
        print(f"Пропущено: сообщение без раздела. Полное сообщение: {message.to_dict()}")

print("Бот запущен. Ожидаем новые сообщения...")
client.start()
client.run_until_disconnected()
