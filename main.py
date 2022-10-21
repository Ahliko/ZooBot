import discord
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config")
TOKEN = os.getenv("TOKEN")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.channel.name == 'test-bot':
            print(f'Message from {message.author}: {message.content}')
            if message.author.id != self.user.id:
                if message.content.startswith("!hello"):
                    await message.channel.send("Hello **" + message.author.name + "**")


intents = discord.Intents.all()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
