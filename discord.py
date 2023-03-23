
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
        reply=prediction_logic.predict(message)
        await message.channel.send(reply)

client.run('MTA4ODA5MjgwMDQ0NjM4NjE4Nw.GRxAzj.sVFWtqTv4d9ABgl2I1ljPl0cWvla9aOoYbHzbs')

