#this *should* cause the bot to prevent spamming messages

#found this info on https://github.com/mayman007/ShinobiBot/blob/main/cogs/antispam/antispam.py
import discord
from discord.ext import commands
import datetime
import time

#10 seconds is the time frame
timeframe = 10
max_messages = 5
#list of user messages
user_messages = {}

#creating bob the bot
bob = commands.Bot(precommand='/')

#using Tyler's code here for ease of coding
@bob.event
async def on_ready() -> None:
    print(f'{bob.user} is running')


@bob.event
async def on_message(message):
    username = message.author.id
    #checking to see if username is in dictionary that was created earlier
    if username not in user_messages:
        #if not, the username is added as a key with an empty array to the dictionary
        user_messages[username] = []
    #here we are adding the time the message was created to the array (value) of the user (key) in the dictionary
    user_messages[username].append(message.created_at)

    #clearing older messages from array that fall outside of the timeframe
    
    if(user_messages[username].length > max_messages):
        await message.channel.send(f'slowwwwww dooowwwwwwnnnn pleeaaasssseeeee')

    await bob.process_commands(message)

bob.run()

