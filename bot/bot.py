import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
#Made by Sano
bot = discord.Client()
@bot.event
async def on_ready():
    print("Name: " + bot.user.name)
    print("ID: " + bot.user.id)
    print("----------------------")

@bot.event
async def on_member_join(member):
    welcome_message = "Welcome, please relieve yourself of your sins to me and I will share them to the server in confidence"
    for channel in member.server.channels:
        if channel.name == 'confessions':
            #get id of member
            client = await bot.get_user_info(member.id)
            await bot.send_message(client,welcome_message)
            #add a role
            await bot.add_roles(member, discord.utils.get(member.server.roles, name='Sinner'))

@bot.event
async def on_message(message):
    if(str(message.channel.type) == "private"):
        lines = ["It's okay my son","Go on my son","I forgive your sins","Your sins have been lifted","Forgive yourself before I can start forgiving you"]
        blacklist = ["blacklisted peoples id"]
        lowermessage = message.content.lower()
        BannedWords = ["fuck"]
        server_channel = discord.Object("channel id")
        #open file
        file= open("sins.txt","a+")
        #get id of author
        client = await bot.get_user_info(message.author.id)
        for i in range(0,len(BannedWords)):
            if BannedWords[i] in lowermessage:
                await bot.send_message(client, "This is a christian server")
                return
        if client in blacklist:
            await bot.send_message(client, "You have been blacklisted for a non-determained amount of time")
            return
        #check if bot speaks
        if message.author == bot.user:
            return
        #send to dm after message was sent
        rand = random.randrange(len(lines))
        await bot.send_message(client, lines[rand])

        if(server_channel == message.channel):
            return
        #saving what people said
        print("{}: {}\n".format(client,message.content))
        file.write("{}: {}\n".format(client,message.content))      
        #send it to a server
        confession_message = "Anonymous: " + message.content
        await bot.send_message(server_channel,confession_message)
            
bot.run("Token");
    
