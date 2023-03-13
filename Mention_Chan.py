import discord
import time
from discord.ext.commands import Bot

### inmemory cord


### discord py
TOKEN = "MTAyNTYzOTQ4MjAxMzI3MDA0Ng.G-6fzL.7Enxsk2n9DjiND7A1VwsOuhpcQVmcDNoe6s6Zc"
intents = discord.Intents.all()

# !로 시작하면 명령어로 인식
bot = Bot(command_prefix='!', intents = intents)

atetime = 0


@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')
  
@bot.command()
async def 리셋(ctx):
  global atetime
  atetime = time.time()
  await ctx.send('리셋됨!')
  print('0',atetime)
  

# !hello 명령어 처리
@bot.command()
async def 마라(ctx):
  global atetime
  print('1',atetime)
  nowtime = time.time()
  period = nowtime-atetime
  period = round(period,3)
  await ctx.send(f'차돌짬뽕 안먹은지 {period}초째!!!')
  atetime = time.time()
  print('2',atetime)

bot.run(TOKEN)