 import discord
from discord.ext import commands
from third import tokenn

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi ,I am {bot.user},I am going to tell you about nature!')

@bot.command()
async def meme(ctx):
    with open('images/meme1.jpg' , 'rb') as f:
        picture=discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def learningpicture(ctx):
    with open('images/meme2.jpg' , 'rb') as f:
        picture=discord.File(f)
        await ctx.send(file=picture)


bot.run(tokenn)

