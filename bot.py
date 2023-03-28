
import discord
import prediction_logic

client=discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
        print('Logged on as',client.user)

@client.event
async def on_message(message):
        if message.author == client.user:
           return
        print('replied')
        
        await message.channel.send(prediction_logic.predict(str(message)))

client.run('token here')

