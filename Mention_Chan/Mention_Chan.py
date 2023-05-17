import discord
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
    for _ in range(10):
        await ctx.send(message)


bot.run(TOKEN)