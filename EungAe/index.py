import discord
import time
from datetime import datetime
from discord.ext import commands

with open('secret.txt', 'rt') as f:
    TOKEN = f.readline()

start = None
end = None
OK = False

intents = discord.Intents.all()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix='!', intents=intents)
# 심계 2층
# ch = client.get_channel(1017384471231741972)

# test
ch = client.get_channel(1098141769352359997)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print("============================================")

@client.event
async def on_message(message):
    global start, end, OK
    if message.content == "읏읏아": # 봇 시작
        now = datetime.now()
        ch = client.get_channel(1098141769352359997)
        
        if OK != True:
            await ch.send(f"응애~ \n[응애짱이 {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초에 태어났습니다.]")
            start = time.time()
            OK = True
        else:
            await ch.send("우에에엥~")

    # 이후부터는 OK 가 True일 때만 작동
    if message.content == "폐기처분": # 봇 사망
        end = time.time()
        ch = client.get_channel(1098141769352359997)

        if start is not None:
            seconds = end - start
            await ch.send(f"응애가 죽었습니다. \n응애의 나이 : {seconds // 2592000}")
            OK = False







client.run(TOKEN)