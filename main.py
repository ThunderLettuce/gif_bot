import discord
from discord.ext import commands

client = discord.Client()
BOT_TOKEN = "NjM3MDYzMTMwNDkyNTY3NTUy.XbItYA.2Yzh7FtyxMPlsW2ieb-ppyF5UfI"
bot = commands.Bot(command_prefix='@')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@bot.command
async def test(ctx):
    pass


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('yeee boiii! YEET')


# Bot token
client.run(BOT_TOKEN)
