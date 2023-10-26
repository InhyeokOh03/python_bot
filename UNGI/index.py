import random
import discord
import datetime
import pytz

# import requests
# import json

# import os
# import google.oauth2.credentials
# import google_auth_oauthlib.flow
# import googleapiclient.discovery

with open('secret.txt', 'rt') as f:
    TOKEN = f.readline()

client = discord.Client(intents=discord.Intents.all())
guild_id = 1012347803185446982

# # ============================================================================================ 
# # Google API 설정
# SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
# API_SERVICE_NAME = "youtube"
# API_VERSION = "v3"
# # Google API 인증 설정
# flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
# credentials = flow.run_local_server(port=0)
# # Google API 클라이언트 생성
# youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
# previous_video_id = ""
# # ============================================================================================ 


###functions
def binomial(p):
    return random.random() < p

def waruguchi():
    first_words = ["아니", "진짜", "미친", "시발"]
    last_words = ["졌노", "좆같노", "하아"]
    return random.choice(first_words) + " " + random.choice(last_words)

def rps(user_move, bot_move):
    if user_move not in ["가위", "바위", "보"]:
        return random.choice(["제대로 쳐내 씹련아 ㅋㅋ", "뭐하냐 시발아"])
    elif user_move == bot_move:
        return random.choice(["ㄲㅂ", "다시 ㄱ", "ㅋㅋㅋRe"])
    elif user_move == "가위" and bot_move == "보":
        return waruguchi()
    elif user_move == "보" and bot_move == "바위":
        return waruguchi()
    elif user_move == "바위" and bot_move == "가위":
        return waruguchi()
    else:
        return random.choice(["병신ㅋ", "허접ㅋ", "좆밥새기ㅋ"])
###

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print("============================================")

    
@client.event
async def on_message(message):
    # print(message.content)
    # print(message)
    
    # if "안녕" in message.content:
    #     await message.channel.send(f"{message.author.mention} ㄱㄴ")
    

    
    # 확률적으로 터지는 것
    if 'ㅋㅋ' in message.content:
        if message.author != client.user:  # 봇이 보낸 메시지는 무시합니다
            if binomial(1/5):
                await message.channel.send(':owl:')
    if message:
        if binomial(1/40):
            await message.channel.send('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
            
    if message.attachments:
        for attachment in message.attachments:
            if attachment.url.endswith(('.png', '.jpeg', '.jpg', '.gif')):
                if binomial(1/10):
                    await message.channel.send(f"{message.author.mention} ㄱㄴ")
    
    if message:
        if binomial(1/200):
            await message.channel.send('박노윤 가슴 졸라큼')
        
    if '?' in message.content:
        messages = ['조까슈', '조까', 'ㅈㄲ', 'ㅈㄲㅅ']
        temp = random.choice(messages)
        if binomial(1/100):
            await message.channel.send(temp)
    
    # 확률적으로 특수한 경우
    # print(message.author.id)
    if message.author.id == 412232201204137995:
        if binomial(1/10):
            his_id = 412232201204137995
            await message.channel.send(f'<@{his_id}> ?')

    # 무조건 터지는 것
    ## 저스트
    if message.content == '야':
        await message.channel.send('왜')
    if message.content == '웅기':
        await message.channel.send('딱좋노')
    if message.content == 'ㅖㅏ':
        await message.channel.send(':koala:')
    if message.content == '긍가?':
        await message.channel.send('그정둔가?')
        
    ## 논저스트
    if '안녕' in message.content:
        await message.channel.send('반갑노')
    if '섹스' in message.content:
        await message.channel.send('웅기잇')
    if '퍽' in message.content:
        await message.channel.send('하응~')
    if '페이커' in message.content:
        await message.channel.send('1557!! 1557!!')
    if '진짜' in message.content:
        await message.channel.send('어 맞아, 놀랍게도 그건 사실이야.')

    # 특수 명령어
    if message.content == '멤버목록':
        content = ", ".join([member.name for member in message.guild.members if not member.bot])
        await message.channel.send(content)

    if message.content.startswith("가위바위보!"):
        moves = ["가위", "바위", "보"]
        bot_move = random.choice(moves)
        user_move = message.content[7:]        
        word = rps(user_move, bot_move)
        await message.channel.send(bot_move)
        await message.channel.send(word)
        
    if message.content.startswith("!시간"):
        now = datetime.datetime.now(pytz.timezone("Asia/Seoul"))
        await message.channel.send("지금 {}월 {}일 {}시 {}분임 ㅅㄱ".format(now.month, now.day, now.hour, now.minute))


    # 임베드
    if message.content == '디지스트 귀요미 두명':
        embed = discord.Embed(colour=discord.Colour.red(), title = message.content, description='손선빈과 김웅기')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1092728620683907213/1098876075804741725/image0.jpg")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1092728620683907213/1098656061545775124/image0.jpg")
        embed.set_footer(text=message.author, icon_url=message.author.avatar.url)
        # embed.add_field(name="field title", value='field description', inline=False)
        await message.channel.send(embed=embed)
    
    if message.content == '내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(colour=discord.Colour.blue(), title = f'{user.name}의 정보', description=f'디스코드 가입일 : {date.year}/{date.month}/{date.day}')
        embed.set_image(url=user.avatar.url)
        await message.channel.send(embed=embed)


    ## 개발중

    # if message.content == "김웅기":
    #     member = discord.utils.find(lambda m: m.name == "D붕이#0266", message.guild.members)
    #     await message.channel.send(member.mention)
        
    # if message.content == '멤버닉네임':
    #     content = ", ".join([member.nick for member in message.guild.members if not member.bot])
    #     await message.channel.send(content)

# # ============================================================================================ 
# async def check_youtube():
#     global previous_video_id

#     # 감지할 유튜버의 채널 ID
#     channel_id = "UCw0IGX_bljfR34qvhKZ04Sw"

#     # 새로운 동영상 정보 가져오기
#     request = youtube.search().list(
#         part="snippet",
#         channelId=channel_id,
#         type="video",
#         eventType="completed",
#         maxResults=1,
#         order="date"
#     )

#     response = request.execute()

#     # 새로운 동영상 ID 가져오기
#     video_id = response["items"][0]["id"]["videoId"]

#     # 이전에 가져온 동영상 ID와 비교하여 새로운 동영상이 있다면 알림 전송
#     if previous_video_id != video_id:
#         # 새로운 동영상의 제목 가져오
#         title = response["items"][0]["snippet"]["title"]

#         # Discord 봇으로 알림 전송
#         channel = client.get_channel(guild_id)
#         await channel.send(f"{title} 동영상이 새로 업로드되었습니다! https://www.youtube.com/watch?v={video_id}")

#         previous_video_id = video_id

# client.loop.create_task(check_youtube())
# # ============================================================================================ 
client.run(TOKEN)