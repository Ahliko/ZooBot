import discord
from dotenv import load_dotenv
import os

TOKEN = os.getenv("TOKEN")
load_dotenv(dotenv_path="config")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.channel.name == 'test-bot':
            print(f'Message from {message.author}: {message.content}')
            if message.author.id != self.user.id:
                await message.channel.send(message.content)


intents = discord.Intents.all()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
