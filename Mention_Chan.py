import discord
import time
from discord.ext.commands import Bot


TOKEN = "MTAyNTYzOTQ4MjAxMzI3MDA0Ng.G-6fzL.7Enxsk2n9DjiND7A1VwsOuhpcQVmcDNoe6s6Zc"
intents = discord.Intents.all()

bot = Bot(command_prefix='!', intents = intents)


@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')
  
@bot.command(name='야')
async def _mention(ctx, name):
    for i in range(10):
        await ctx.send(name)

bot.run(TOKEN)