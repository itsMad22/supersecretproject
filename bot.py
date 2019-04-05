import discord
import time
import asyncio

from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get

#extensions = ['admin']

#bot = discord.bot() #Initialise bot
bot = commands.Bot(command_prefix = "$", status=discord.Status.idle, activity=discord.Game(name="Developed by Toast!")) #Initialise bot bot

@bot.event
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server
    print("Noxu is now active.")
    #bot.load_extension("admin")
    print("Loaded Admin Module")

@bot.command()
async def info(ctx):
    await ctx.send("Noxu bot is being developed by <@124964742371475458>, and is still in alpha stages.")

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"My ping is {ping}ms")

bot.run('NTEzMDI4MTI2MDAzOTUzNjc1.XKdDxQ.c  JO-X1AsmFW05h8TpPl3-wZFtZY')
