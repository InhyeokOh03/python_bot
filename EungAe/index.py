import discord
from datetime import datetime
from discord.ext import commands

with open('secret.txt', 'rt') as f:
    TOKEN = f.readline()

intents = discord.Intents.all()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix='!', intents=intents)
now = datetime.now()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print("============================================")
    ch = client.get_channel(1017384471231741972)
    await ch.send(f"응애~ \n응애짱이 {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초에 태어났습니다.")



client.run(TOKEN)