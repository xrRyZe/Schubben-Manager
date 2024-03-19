import discord
from discord.ext import commands
import sys
sys.path.append('./data')
import dc_token as token
import dc_channel as channel
sys.path.append('./bot_loging')
import bot_loging as log
sys.path.append('./bot_utility')
import bot_utility as util

# console colors 
GREEN = '\033[92m'
LGREEN = '\033[92m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
LBLUE = '\033[96m'
END = '\033[0m'

# Create a new bot instance
bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())

# Event that runs when the bot is ready
@bot.event
async def on_ready():
    print(f'{GREEN}Bot ready! Logged in as{END} {LGREEN}{bot.user.name}{END}')
    log.logStartUp()
    print(f'{BLUE}StartUp Log done!{END}')

# Command to greet the user
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

# @bot.command()
# async def play(ctx, url):
#     if not util.url_in_list(url):

#     voice_channel = ctx.author.voice.channel
#     voice_client = await voice_channel.connect()
#     voice_client.play(discord.FFmpegPCMAudio(url))

@bot.command()
async def clear(ctx, amount):
    if type(amount) == int:
        await ctx.channel.purge(limit=amount)
    else:
        if amount == "a":
            await ctx.channel.purge(limit=None)
        else:
            await ctx.send("Invalid command! Use '#clear <amount_as_number>' or '#clear a' to clear all messages!")

# Run the bot
bot.run(token.getToken())

# Event that runs when the bot is shutting down

