import asyncio

from telethon import TelegramClient

import credentials


async def main():
    client = TelegramClient('MessageSkipper', credentials.api_id, credentials.api_hash)
    client.start()
    await client.connect()
    me = await client.get_me()
    print(me.stringify())
    await client.disconnect()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
