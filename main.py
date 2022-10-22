import discord
from dotenv import load_dotenv
import os

import main

load_dotenv(dotenv_path="config")
TOKEN = os.getenv("TOKEN")


class MyClient(discord.Client):
    #def __init__(self, intents):
    #    self.ChID = 0
    #    self.Role_Emote = {}                                                       Le dico est la mais dès que l'on decommente le code fonctionne plus a cause de la init
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        if message.channel.name == 'test-bot':
            print(f'Message from {message.author}: {message.content}')
            if message.author.id != self.user.id:
                if message.content.startswith("!hello"):
                    await message.channel.send("Hello **" + message.author.name + "**")

                if message.content.startswith("!createRole"):
                    arg = message.content.split()
                    #self.Role_Emote[arg[1]] = arg[2]                              Pour stocker il nous faudrait un dico
                    await message.channel.send(f"{arg[1]} {arg[2]}")

                if message.content.startswith("!removeRole"):
                    await message.channel.send("[name]")

    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.name == 'test-bot':
            if reaction == ":grin:":   # <- Marche pas
                await reaction.message.channel.send("Une reaction a eu lieu : " + str(reaction))
            if reaction.emoji == "👍":  # <- Marche
                await reaction.message.channel.send("Une reaction a eu lieu : " + str(reaction))

intents = discord.Intents.all()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
