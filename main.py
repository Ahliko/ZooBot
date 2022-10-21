import discord as di
#from discord.ext import commands

intents = di.Intents.default()

#zooBot = commands.Bot(command_prefix="!", description="Ouh ouh ah ah !", intents= di.Intents.default())

#@zooBot.event
#async def on_ready():
#    print("I'm ready to be used !")
#
#@zooBot.command()
#async def Hey(context, message): # Lancement d'une conversation avec le bot            (IA de dialog)
#    await context.send('Hello {0.author.mention}'.format(message))
#
#@zooBot.command()
#async def explainMe(context, message): # Permet de poser une question au bot qui ira chercher la réponse pour la renvoyer                (IA de recherche)
#    await context.send("I can't explain it to your for moment")
#
#@zooBot.command()
#async def giveMeCodeFor(context, fonction, language):  # Permet de poser demander le code d'une fonction qu'il renverra dans le langage demandé
#    await context.send("I can't give you this code for moment")
#
#@zooBot.command()
#async def addRole(context, name, emote):
#    message = f'Hey, a new role was add !\nUse : {emote} to get it !'
#    await context.send(message)
#
#@zooBot.command()
#async def Help(context):
#    await context.send("**Ouh ouh ah ah !**\nI'm zooBot, to use me commands enter **![command]**\n\n**Command's List : **\n- !addRole [name] [emote] : *Create a new role named [name], and it's possible to get it with [emote] reaction\n- !creatMessKey [name] : *Init a key's for encoding your message*\n- !useMessKey[name] : *Init key decoding for read coding message with the key's*")

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
