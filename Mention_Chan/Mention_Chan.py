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

def binomial(p):
    return random.random() < p

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print("===============================================")

@bot.command()
async def 야(ctx, message=None, count: int = 1):
    if message is None:
        await ctx.send('뭐')
    elif count >= 100:
        await ctx.send("좆까라")
    else:
        for i in range(count):
            if i > 10 and binomial(1/(100 - count)):
                await ctx.send("씨발 더러워서 못해먹겠네.")
                break
            await ctx.send(message)
        
@bot.command()
async def 웅기발작(ctx):
    for _ in range(10):
        temp = random.choice(["야", "웅기", "ㅖㅏ", "긍가?"])
        await ctx.send(temp)


bot.run(TOKEN)