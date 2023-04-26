import discord
import os
import random
import fortune
from deep_translator import GoogleTranslator

print(os.getenv('TOKEN'))
intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):  
    if message.author == client.user:
        return

    if message.content.startswith('$toss'):
        toss = random.randint(0, 1)
        if toss: 
            await message.channel.send('You\'ve got Heads!')
        else:
            await message.channel.send('You\'ve got Tails!')

    if message.content.startswith('$fortune'):
        fort = fortune.get_random_fortune('/usr/share/games/fortunes/fortunes')
        await message.channel.send(fort)
    
    if message.content.startswith('$tr '):
        content = message.content[4:]
        translation = GoogleTranslator(source='auto', target='en').translate(content)
        await message.channel.send(translation)

    if message.content.startswith('$fr '):
        content = message.content[4:]
        translation = GoogleTranslator(source='auto', target='fr').translate(content)
        await message.channel.send(translation)
        
        

client.run(os.getenv('TOKEN'))