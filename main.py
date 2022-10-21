import discord

TOKEN = "MTAzMjk4Nzc2ODk5MDc0NDU3Ng.GEyMKg.u_bJtS2IqYZj-qmv-b_S156bNCBe8quR304WGY"

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
