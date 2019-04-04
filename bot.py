import discord
import time
import asyncio

from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get



Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot


@client.event 
async def on_ready():    
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server
    print("Noxu is now active.")
    
@client.event
async def on_message(message):
    #if message.content == "cookie":
    #   await client.send_message(message.channel, ":cookie:")
    if message.content.upper() == "BADWORD":
        await client.delete_message(message)
        userID = message.author.id
        tempc = await client.send_message(message.channel, "<@%s> Please refrain from saying that here." % (userID) )
        time.sleep(3)
        await client.delete_message(tempc)
    
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID) )

    if message.content.upper().startswith('!SAY'):
        if message.author.id == "124964742371475458":
            args = message.content.split(" ")
            await client.delete_message(message)
            await client.send_message(message.channel, "%s" % (" ".join(args[1:]))) # Say after array pos 1
        else:
            userID = message.author.id
            tempc = await client.send_message(message.channel, "<@%s> You have insufficient permissions to run that command." % (userID) )
            time.sleep(3)
            await client.delete_message(message)
            await client.delete_message(tempc)
            
    if message.content.upper().startswith('!SC'):
            if "506131078017318913" in [role.id for role in message.author.roles]:
                userID = message.author.id
                tempc = await client.send_message(message.channel, "<@%s> Staff check returned true." % (userID) )
                time.sleep(3)
                await client.delete_message(message)
                await client.delete_message(tempc)
            else:
                userID = message.author.id
                tempc = await client.send_message(message.channel, "<@%s> You have insufficient permissions to run that command." % (userID) )
                time.sleep(3)
                await client.delete_message(message)
                await client.delete_message(tempc)
#
#     <@&391655322885816332> - Staff Role ID
#     <@&506131078017318913> - Management Role ID
            


client.run('NTEzMDI4MTI2MDAzOTUzNjc1.DtCErQ.c9Uw69qZdSswR3VyPR3USmWfnsk')
