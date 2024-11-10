import discord
from third import tokenn

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('information, please'):
        await message.channel.send("you know nature was polluted, so I will give you some informathion to save nature: 1. recycle ; 2. buy thing that you need ; 3. use electric cars ; 4.don't burn trash")
    elif message.content.startswith('what can we do?'):
        await message.channel.send("let's choose pratical idea! And make it true")
    elif message.content.startswith('hello'):
        await message.channel.send("Hi ,I am nature,I am going to tell you about nature!") 
    else:
        await message.channel.send(message.content)    
    
client.run(tokenn)
