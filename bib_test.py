import asyncio
import time
import random

from telethon import TelegramClient, events

api_id =
api_hash = ""
session_name = ""

async def start():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        @client.on(events.NewMessage())
        async def handler(event):
            if 'Наш канал: @bibinto' in event.text:
                time.sleep(2)
                await client.send_message("bibinto_bot", message=f'{random.randint(1, 10)}')
            elif 'К сожалению, мы не смогли подобрать для вас новое фото' in event.text:
                time.sleep(2)
                await client.send_message("bibinto_bot", message=f'/start')
                time.sleep(2)
                await client.send_message("bibinto_bot", message=f'🚀Оценивать')

        await client.run_until_disconnected()

async def main():
    await start()

if __name__ == "__main__":
    asyncio.run(main())


