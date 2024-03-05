from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

import pandas as pd
import random


# start of code here
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    author = message.author

    if not user_message:
        print('No Message')
        return
    
    try:
        response: str = get_response(user_message, author)
        await message.channel.send(response)
    except Exception as error:
        print(error)

    
@client.event
async def on_ready() -> None:
    print(f'{client.user} is running')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return   

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: {user_message}')
    if (channel == "bot"):
        await send_message(message, user_message)
    else:
        return

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()