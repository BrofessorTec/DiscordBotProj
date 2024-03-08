# responses.py
from discord.ext import commands
from random import randint
import datetime

# =================================================================================================
# Rabbit hole of documentation

# https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context
# https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
# https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#bots
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html#ext-commands-cogs
# https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.command

# =================================================================================================

# a cog is a way to group related functions. here we have all of our dice and game functions
class GameCog(commands.Cog):
    # intialization of variables
    def __init__(self, bot):
        self.bot = bot
        self.deathroll_cont = 0
        self.author_records = {}
        self.start_time = datetime.datetime.now()  # same as bot.start_time

    # to create a command that would come after our prefix ('/') use @commands.command(name='')
    # this command will be called when a user enters '/roll'
    @commands.command(name='roll')
    # ctx (context) allows us to send and receive messages from the discord server, 
    # as well as gain access to the users, channel name, and other properties
    async def roll(self, ctx, max_num: int = 20): #make sure the function is async
        roll = randint(1, max_num)
        await ctx.send(f'You rolled a {roll} out of {max_num}!')

    @commands.command(name='deathroll')
    async def deathroll(self, ctx, max_num: int = None):
        author = str(ctx.author)
        if max_num is not None:
            self.deathroll_cont = randint(1, max_num)
        elif self.deathroll_cont == 0:
            self.deathroll_cont = randint(1, 999)
        roll = randint(1, self.deathroll_cont)
        deathrollMaxPlaceHolder = self.deathroll_cont
        self.deathroll_cont = roll
        if roll == 1:
            self.author_records[author] = self.author_records.get(author, 0) + 1
            self.deathroll_cont = 0
            await ctx.send(f'You rolled a 1! You lose Deathroll! Total losses: {self.author_records[author]}')
        else:
            await ctx.send(f'You rolled a {roll} out of {deathrollMaxPlaceHolder}! Roll below to continue the Deathroll!')

    @commands.command(name='uptime')
    async def uptime(self, ctx):
        current_time = datetime.datetime.now()
        uptime_duration = current_time - self.start_time
        await ctx.send(f'Uptime: {str(uptime_duration)}')

    @commands.command(name='myrecords')
    async def myrecords(self, ctx):
        author = str(ctx.author)
        losses = self.author_records.get(author, 0)
        await ctx.send(f"{author}'s Deathroll Losses: {losses}")

    # the original help command built into discord.py is being overwritten since it is set to none in main.py
    # if we did not want to overwrite the default help command, we should rename it
    @commands.command(name='help')
    async def help_command(self, ctx):
        help_message = """
        Help:
            /uptime - Display how long the bot has been online
            /roll - Roll a d20
            /roll [size] - Roll a die of the given size
            /deathroll [maxNum] - Start a deathroll game with the given maximum. First to roll a 1 loses!
            /deathroll - Continue a deathroll game or start a new one from 999
            /myrecords - Display your game scores since the bot has been online
            """
        await ctx.send(help_message)

def setup(bot):
    bot.add_cog(GameCog(bot))