import discord
from discord.ext import commands

# Create a new bot instance
bot = commands.Bot(command_prefix='!')

# Event that runs when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to greet the user
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

# Run the bot
bot.run('YOUR_BOT_TOKEN')