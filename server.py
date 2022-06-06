import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv(dotenv_path="credentials")

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print("The bot is ready !")

@bot.command(name='clear')
async def clear_channel(ctx, nb_clear: int):
    msgs = await ctx.channel.history(limit= nb_clear + 1).flatten()

    for msg in msgs:
        await msg.delete()

try:
    bot.run(str(os.getenv("ACCESS_TOKEN")))
except:
    print("Bad Token / Bot already used !")
    exit(1)