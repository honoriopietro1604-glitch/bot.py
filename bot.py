import discord
from config import TOKEN
from discord.ext import commands
from bot_logic import gen_pass
import os
import random




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot. command()
async def passaword (ctx, size = 10):
    await ctx.send(gen_pass(size))
@bot.command()
async def memes(ctx):
    escolha = random.choice(os.listdir('memes'))
    with open(f'memes/{escolha}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def Back_in_black(ctx):
    text= "rock"
    with open('sounds/back_in_black.mp3', 'rb') as f:
        sound = discord.File(f)
        await ctx.send(text, file=sound)
bot.run(TOKEN)