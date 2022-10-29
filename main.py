import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
import time

load_dotenv(dotenv_path="config")
TOKEN = os.getenv("TOKEN")

ChID = 0
Role_Emote = dict()

channelsList = []

intents = discord.Intents.all()
intents.message_content = True
prefix = '!'

bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    for guild in bot.guilds:
        for channel in guild.channels:
            channelsList.append(channel.name)
    if not "zoobot-channel" in channelsList:
        await bot.get_channel(1033131367317393550).clone(name="zooBot-Channel")


@bot.command()
async def hollo(ctx, arg):  # !hello
    if not arg:
        await ctx.send("Précise un argument")
    else:
        await ctx.send(arg)

@bot.command()
async def everyone(ctx):
    await ctx.send(content="@everyone", allowed_mentions=discord.AllowedMentions.all())

@bot.command()
async def ping(ctx, arg):
    user = discord.utils.get(bot.server.members, name=arg, discriminator=6885)
    await ctx.send(content=f"{user.mention}", allowed_mentions=discord.AllowedMentions.all())

# Problème à résoudre
#@bot.event
#async def on_message(ctx):
#    if ctx.channel.name == "test-bot":
#        if ctx.author != bot.user:
#            if 22 <= time.localtime().tm_hour <= 23:
#                await ctx.channel.send(f"Je pense qu'il serait temps d'aller se coucher **{bot.ctx.author.name}**  :zzz:")
#            if 23 < time.localtime().tm_hour < 7:
#                await ctx.channel.send(f"Alors... y'en a qui dorme, alors s'te plaît **{ctx.author.name}** fais moins de bruit  :shushing_face:")

bot.run(TOKEN)