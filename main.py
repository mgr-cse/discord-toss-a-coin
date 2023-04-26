import discord
import os
import random
import fortune

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

client.run(os.getenv('TOKEN'))