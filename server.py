import discord
import youtube_dl
import json
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from crypto import GetFinancialInfo
import os

load_dotenv(dotenv_path="credentials")

bot = commands.Bot(command_prefix="?")

finance = GetFinancialInfo()

@bot.event
async def on_ready():
    print("The bot is ready !")

@bot.command(name='clear')
async def clear_channel(ctx, nb_clear: int):
    msgs = await ctx.channel.history(limit= nb_clear + 1).flatten()

    for msg in msgs:
        await msg.delete()

@bot.command(name="crypto")
async def get_crypto(ctx):
    await ctx.channel.send(finance.get_crypto_price())

@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

try:
    bot.run(str(os.getenv("ACCESS_TOKEN")))
except:
    print("Bad Token / Bot already used !")
    exit(1)