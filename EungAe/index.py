import discord

with open('secret.txt', 'rt') as f:
    TOKEN = f.readline()
    
client = discord.Client(intents=discord.Intents.all())
