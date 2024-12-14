import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('Images'))
    with open(f'Images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def notice(ctx):
    not_name = random.choice(os.listdir('notice'))
    with open(f'notice/{not_name}', 'rb') as f:
        ambiente = discord.File(f)
        await ctx.send(file=ambiente)


bot.run()