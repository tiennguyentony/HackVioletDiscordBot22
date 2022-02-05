# bot.py
import os
import discord


from discord.ext import commands

# initialize bot with environment token, intents and prefix
intents = discord.Intents().all()

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')

bot = commands.Bot(command_prefix=PREFIX)

# load and unload bot cogs
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(ctx.author.id)

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

# loop through cogs and load them at start
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        print(file)
        bot.load_extension(f"cogs.{file[:-3]}")

# run bot
bot.run(TOKEN)