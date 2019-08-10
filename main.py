import discord
import os
import random
from keep_alive import keep_alive

#create discord client, but what is a client?
client = discord.Client()
#bot = commands.Bot('.') #bot can do everything client does

fishPossible = ['You caught a :fish:!',
                'Hey that\'s a :crab:!',
                'Fancy catch! A :tropical_fish:!',
                ':blowfish: are poisonous, but sell for a lot!',
                'Oh no! You caught a :dolphin:!',
                'Wow you must be skilled to catch a :whale:!',
                ':whale2: are hard to catch, but you got one!',
                ':shrimp: nice one!',
                ':squid: It looks really angry at you!',
                'Oh dear. You caught a :shell:']

fishWeight = ['You caught a :fish:!'] * 50 + ['Hey that\'s a :crab:!']* 10 +  ['Fancy catch! A :tropical_fish:!']* 5 + [':blowfish: are poisonous, but sell for a lot!']* 5 +  ['Oh no! You caught a :dolphin:!']* 1 +  ['Wow you must be skilled to catch a :whale:!']* 1 +  [':whale2: are hard to catch, but you got one!']* 1 + [':shrimp: nice one!']* 2 + [':squid: It looks really angry at you!']* 5 +  ['Oh dear. You caught a :shell:']* 20

#:crab: :tropical_fish: :fish: :blowfish: :dolphin: :whale: :whale2: :shrimp: :squid: :shell: 
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.content == '.fish':
        for i in range(10):
          await message.channel.send(fishPossible[random.randint(0, len(fishPossible) - 1)])
    elif message.content == '.fish1':
      await message.channel.send(fishPossible)
    elif message.content == '.fish2':
      for i in range(10):
        await message.channel.send(random.choice(fishWeight))
    elif message.content == '.cast':
        channel = client.get_channel(608815074622046211)
        await channel.send('You casted your rod.')
#    elif message.author != client.user: #was part of tutorial
#        await message.channel.send(message.content[::-1]) #different from tutorial bc it's either using a rewrite or the versions are different


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
bot.run(token)

from discord.ext import commands


bot = commands.Bot(command_prefix='!')

@bot.command()
async def test(ctx):
    await ctx.send('I heard you! {0}'.format(ctx.author))

bot.run('token')

# from discord.ext.commands import Bot
# bot = Bot("!")

# @bot.command()
# async def test(ctx):
#     await ctx.send("Command executed")

# await bot.run("TOKEN")
