from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from datetime import datetime
import pandas as pd


# start of code here
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#intents are the permissions the bots needs to be able to respond to messages
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

startTime = None
started = False

async def startTime():
    global started
    global startTime
    started = True
    startTime = f'{datetime.now().time().hour}:{datetime.now().time().minute} EST on {datetime.now().date()}'

async def send_message(message: Message, user_message: str, startTimeStamp: str) -> None:
    author = message.author

    if not user_message:
        print('No Message')
        return
    
    try:
        response: str = get_response(user_message, author, startTime)
        await message.channel.send(response)
    except Exception as error:
        print(error)

    
@client.event
async def on_ready() -> None:
    global started
    print(f'{client.user} is running')
    if started is False:
        await startTime()

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return   

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: {user_message}')
    if (channel == "bot"):
        await send_message(message, user_message, startTime)
    else:
        return

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()