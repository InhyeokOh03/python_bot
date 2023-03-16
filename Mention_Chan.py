import discord
# import time
from discord.ext.commands import Bot
from discord.ext import commands

TOKEN = "MTAyNTYzOTQ4MjAxMzI3MDA0Ng.G-6fzL.7Enxsk2n9DjiND7A1VwsOuhpcQVmcDNoe6s6Zc"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def 야(ctx, *, message):
    if message == '안녕':
        for i in range(10):
            await ctx.send('안녕')

@bot.event
async def on_message(message):
    if message == '멘션쨩~':
        await message.channel.send('왜 불렀어용~?')

    await bot.process_commands(message)

bot.run(TOKEN)