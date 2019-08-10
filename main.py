import discord
import os
from keep_alive import keep_alive

#create discord client, but what is a client?
client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.content == '.fish':
        await message.channel.send('You typed fish. :fish:')
    elif message.content == '.cast':
        channel = client.get_channel(608815074622046211)
        await channel.send('You casted your rod.')
#    elif message.author != client.user: #was part of tutorial
#        await message.channel.send(message.content[::-1]) #different from tutorial bc it's either using a rewrite or the versions are different


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)


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
