# main.py
# ===============================================================================================================================
#      Main just set up the bot and tells it to run. as well as give it acces to events and commands
#      We have a start time but we could add some other statistics here too
# ===============================================================================================================================

import discord # discord.py to use its built in commands. this is our api
from discord.ext import commands
from datetime import datetime
from dotenv import load_dotenv # gets our key from the .env file so that it stays hidden. you can name the file whatever
import os

# Load environment variables from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Intents and Bot initialization
# Intents are specific events that your bot is allowed to watch for and act on
# By setting it to default the bot will monitor messages, reactions, when a message or reaction is deleted, etc.
intents = discord.Intents.default()
# this makes sure that our bot can interact specifically with member events
intents.members = True
# i had a bug and somehow this fixed it
intents.message_content = True
# sets the prefix to send a command to the bot. in this case we are using '/'
client = commands.Bot(command_prefix='/', intents=intents)

# start the bot and set start time as an attribute of the bot, set it to the time you started it
client.bot_start_time = datetime.now()

# the discord api already has a help command, which we want to override to display our own commands
client.help_command = None
# Loading the Cogs, this is from our responses file
from responses import GameCog

#creating some variables to be used for the spam detection
#10 seconds is the time frame
timeframe = 10
max_messages = 5
#list of user messages
user_messages = {}


# events are watched for, commands are called (us using /, as selected earlier, some people use '!' or other symbols)

@client.event
async def on_ready():
    await client.add_cog(GameCog(client))
    print(f"{client.user} is running since {client.bot_start_time.strftime('%Y-%m-%d %H:%M:%S')}")

@client.event
async def on_member_join(member):
    channel_id = 1213568524182880296/1213918263042646067 
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}!")


@client.event
async def on_message(message):
    print(message) # for logging
    username = message.author.name
    print(username) # for logging
    #checking to see if username is in dictionary that was created earlier
    if username != "SSS_Bot" and username not in user_messages:
        #if not, the username is added as a key with an empty array to the dictionary
        user_messages[username] = []
    #here we are adding the time the message was created to the array (value) of the user (key) in the dictionary
    if username != "SSS_Bot": 
        user_messages[username].append(message.created_at)
        #this currently doesnt do anything..

    if(username != "SSS_Bot" and len(user_messages[username]) > max_messages and user_messages[username]):
        await message.channel.send(f'{username} slowwwwww dooowwwwwwnnnn pleeaaasssseeeee')
        user_messages[username] = []

    await client.process_commands(message)

@client.command(name='giverole')
async def assign_role(ctx, member: discord.Member, role_tag: str):
    role = discord.utils.get(ctx.guild.roles, name=role_tag)

    if role:
        await member.add_roles(role)
        await ctx.send(f"Role '{role_tag}' assigned to {member.mention}")
    else:
        await ctx.send(f"Role '{role_tag}' not found.")

@client.command(name='removerole')
async def remove_role(ctx, member: discord.Member, role_tag: str):
    role = discord.utils.get(ctx.guild.roles, name=role_tag)

    if role:
        await member.remove_roles(role)
        await ctx.send(f"Role '{role_tag}' removed from {member.mention}")
    else:
        await ctx.send(f"Role '{role_tag}' not found.")

client.run(DISCORD_TOKEN)