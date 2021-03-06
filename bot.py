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
    #await ctx.send("Noxu bot is being developed by <@124964742371475458>, and is still in alpha stages.")
    embed = discord.Embed(
        title = "Noxu Bot", description = "Noxu bot is still in development, and not released for public servers. Coded by <@124964742371475458>.", colour = discord.Colour.blue())
    message = ctx.message ## Reference to message
    await ctx.channel.send(embed=embed) # Send the message
    await message.delete() ## Delete The message

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send("My ping is {ping}ms")

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)
    await ctx.message.delete()

@bot.command()
async def mentionme(ctx):
    await ctx.send('{0.mention}, Testing!'.format(ctx.author))
    await ctx.message.delete()


bot.run('NTEzMDI4MTI2MDAzOTUzNjc1.XKdDxQ.c  JO-X1AsmFW05h8TpPl3-wZFtZY')
