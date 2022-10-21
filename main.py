import discord as di
from discord.ext import commands

intents = di.Intents.default()



#zooBot = commands.Bot(command_prefix="!", description="Ouh ouh ah ah !")

#@zooBot.event
#async def on_ready():
#    print("I'm ready to be used !")

#@zooBot.commands
#async def hello(context,message):
#    await context.send('Hello {0.author.mention}'.format(message))

#zooBot.run("MTAzMjk4Nzc2ODk5MDc0NDU3Ng.GZ8jJ0.uClXTgvZRwlAZQewRjM5Veq4LNR-rnCZvevDk8")


class MyClient(di.Client(intents=intents)):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))


client = MyClient()
client.run("MTAzMjk4Nzc2ODk5MDc0NDU3Ng.GZ8jJ0.uClXTgvZRwlAZQewRjM5Veq4LNR-rnCZvevDk8")
