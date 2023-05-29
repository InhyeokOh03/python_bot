import discord
import random
# import time
# from discord.ext.commands import Bot
from discord.ext import commands

with open('secret.txt', 'rt') as f:
    TOKEN = f.readline()

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print("===============================================")

@bot.command()
async def 야(ctx, *, message):
    if message == '':
        await ctx.send('뭐')
    else:
        for _ in range(10):
            await ctx.send(message)
        
@bot.command
async def 웅기발작(ctx):
    for _ in range(10):
        temp = random.choice(["야", "웅기", "ㅖㅏ", "긍가?"])
        await ctx.send(temp)


bot.run(TOKEN)