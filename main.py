# main.py
# ===============================================================================================================================
#      Main just set up the bot and tells it to run. as well as give it acces to events and commands
#      We have a start time but we could add some other statistics here too
# ===============================================================================================================================

import discord # discord.py to use its built in commands. this is our api
from discord.ext import commands
# timedelta is a special library within datetime that allows us to set a time interval, 
# and has some built in functions to convert from different time frames (ex days to seconds) 
from datetime import datetime, timedelta
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
# dictionary named user messages - will store (username, list(message times)), weird not defining the types here lol
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
    # says that this does not apply to the bot, just returns
    if message.author.bot:
        return

    # gets the username of the person who sent the message
    username = message.author.name
    # gets the time that the message was sent
    current_time = message.created_at
    
    # if the user is not in our dictionary -
    # creates a dictionary entry of the username and an associated list that is blank for the moment.
    if username not in user_messages:
        user_messages[username] = []
    
    # add the time the message was sent to the list belonging to the username in the dictionary
    user_messages[username].append(current_time)

    # i added timedelta to our imports
    # calculates the timeframe by subtracting timeframe(15 - defined at top) seconds from the current time
    # timedelta is used to convert to a timeframe. 
    timeframe_start = current_time - timedelta(seconds=timeframe)
    
    # creates a blank list of recent messages
    recent_messages = []

    # populates the recent_messages list of the user with all of the messages they sent within the specified timeframe
    for msg_time in user_messages[username]:
        if msg_time > timeframe_start:
            recent_messages.append(msg_time)

    # updates the list of recent messages associated with a user in the dictionary
    # this will count up until it is greater than the max message count, then be cleared (maybe with an action taken)
    user_messages[username] = recent_messages

    # gets the length of messages in the list
    if len(recent_messages) > max_messages:
        await message.channel.send(f'{message.author.mention}, slowwwwww dooowwwwwwnnnn pleeaaasssseeeee:)')
        # clears recent messages so we can start over with testing. 
        # may want to do some other action like block the user from sending messages.
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