import discord
from discord.ext import commands
import os
import random
import asyncio
from keep_alive import keep_alive

# Reminders to a future self/internet fellow:
# If possible, use bot instead of client. Bot is a subclass of client and can do everything client does (or it's supposed to but sometimes feels like it doesn't)
# message.channel.send() will reply, channel.send() will reply to specific channel
#if internet example of bot.run('token') has quotes, remove the quotes as it DNW

#create discord client, but what is a client?
#client = discord.Client() 
bot = commands.Bot(command_prefix='.') 

fishPossible = ['You caught a :fish:!',
                'Fancy catch! A :tropical_fish:!',
                ':blowfish: are poisonous, but sell for a lot!',
                'Oh dear. You caught a :shell:',
                'Not even a nibble...']


fishWeight = ['You caught a :fish:!'] * 50 + ['Fancy catch! A :tropical_fish:!']* 5 + [':blowfish: are poisonous, but sell for a lot!']* 5 + ['Oh dear. You caught a :shell:']* 10 + ['Not even a nibble...'] * 100

channel = bot.get_channel(608815074622046211) #this forces all responses to a certain channel, but every async can't find it

@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)

# @bot.event
# async def on_message(message):
#     if message.author != bot.user: #was part of tutorial
#        await message.channel.send(message.content[::-1]) #different from tutorial bc it's either using a rewrite or the versions are different

@bot.command()
async def fish(ctx): #gets channel, displays "bot is typing", waits for a random time, prints random string
    channel = bot.get_channel(608815074622046211)
    await channel.trigger_typing()
    await asyncio.sleep(random.randint(0,10))
    await channel.send(fishPossible[random.randint(0, len(fishPossible) - 1)])

@bot.command() #prints the list
async def fish1(ctx):
    channel = bot.get_channel(608815074622046211)
    await channel.send(fishPossible)

@bot.command()
async def fish2(ctx):
    channel = bot.get_channel(608815074622046211)
    await channel.trigger_typing()
    await asyncio.sleep(random.randint(0,10))
    await channel.send(random.choice(fishWeight))

@bot.command()
async def cast(ctx):
    channel = bot.get_channel(608815074622046211)
    await channel.send('You casted your rod.')

@bot.command()
async def helper(ctx): #figure out how to change the .help cmd
    channel = bot.get_channel(608815074622046211)
    await channel.send('You fool. Help does nothing.')

@bot.command() #waiting example
async def wait(ctx):
    channel = bot.get_channel(608815074622046211)
    await channel.trigger_typing()
    await asyncio.sleep(random.randint(0,10))
    await channel.send('beep boop waiting')


# @bot.event
# async def on_ready():
#     print("I'm ready.")
#     global target_channel
#     target_channel = bot.get_channel("608815074622046211")
# @bot.command()
# async def send(*, message):
#     global target_channel
#     await bot.send_message(channel, message)

@bot.command()
async def test(ctx):
    await ctx.send('I heard you! {0}'.format(ctx.author))

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')


keep_alive() #web server that keeps bot alive until an hour of inactivity, use uptimerobot if desire 24/7 active

token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
#client.run(token) #archaic

