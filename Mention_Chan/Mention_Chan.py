import discord
# import time
# from discord.ext.commands import Bot
from discord.ext import commands

TOKEN = "MTAyNTYzOTQ4MjAxMzI3MDA0Ng.G-6fzL.7Enxsk2n9DjiND7A1VwsOuhpcQVmcDNoe6s6Zc"

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