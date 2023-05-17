#import pynacl
import random
import asyncio
from discord.ext.commands import Bot
import discord
from discord.ext import commands,tasks 
import time
import random
#import praw
from requests import get
#import json
from discord import app_commands, Intents, Client, Interaction

#reddit = praw.Reddit(
#    client_id="7SzpmyJiLnHwZ7GoglcIsw",
#    client_secret="3p6fzi8bEWfze_J0WSEBJcm-xEfn_A",
#    password="",
#    user_agent="meme thing by u/MyPictureIsACat",
#    username="MyPictureIsACat",
#)

BOT_PREFIX = "`"
TOKEN = "MTAyNjQ5NzMyMjAwMTEwOTAyMg.GOiYn2.JQend8HmDRgnUAGzA6rYGPSMjYVfKbEtmeEVJk"

intents = discord.Intents().all()

client = Bot(command_prefix=BOT_PREFIX, intents = intents)

@client.command(name='ping',  # ping
                description="kinda shows what latency the bot has",
                brief="base ping command",
                aliases=['pp'])
async def ping(ctx):
    await ctx.channel.send(f'Pong! Responded in {round(client.latency * 1000)} ms')


#@client.command(name='working with tol',  # test
#                description="just a test",
#                brief="test",
#                aliases=['t'],
#                pass_context=True)
#async def test(ctx):
#   possible_responses = [
#        'this worked!'
#        'this worked 2!'
#    ]
#    await ctx.channel.send('this finally works!!!!') # has no attribute say???? #fixedish #! need to fix the command not picking a random choice the command: random.choice(possible.responses)

@client.command(name='ding',  # ding lmao
                description="another form for the ping command",
                brief="other form of ping",
                aliases=['dd'])
async def ding(ctx):
    await ctx.channel.send(f'dong! Responded in {round(client.latency * 1000)} ms')

@client.command(name='pinger', # pinger 
                description="pings you lmao",
                brief="pings you",
                aliases=['pmp'])
async def pinger(ctx):
    await ctx.channel.send(ctx.message.author.mention + ' get pinged fucker')

@client.command(name='owner',
                desciption="tells you who the owner of the bot is",
                brief="tells who the bot owner is")
async def owner(ctx):
    await ctx.channel.send("the owner of the bot is <@!946431916553412678>")

@client.command(name='tol',
                description="tells you if it's a lie or if it's the truth",
                brief="truth or lie")
async def tol(ctx):
    tol = ["the Truth", "a Lie"]
    await ctx.channel.send(f"What you said is: {random.choice(tol)}")

@client.command(name='math',
                description="does math for you",
                brief="math")
async def calc(ctx):
    def check(m):
        return len(m.content) >= 1 and m.author != client.user

    await ctx.send("Number 1: ")
    number_1 = await client.wait_for("message", check=check)
    await ctx.send("Operator: ")
    operator = await client.wait_for("message", check=check)
    await ctx.send("number 2: ")
    number_2 = await client.wait_for("message", check=check)
    try:
        number_1 = float(number_1.content)
        operator = operator.content
        number_2 = float(number_2.content)
    except:
        await ctx.send("invalid input")
        return
    output = None
    if operator == "+":
        output = number_1 + number_2
    elif operator == "-":
        output = number_1 - number_2
    elif operator == "/":
        output = number_1 / number_2
    elif operator == "*":
        output = number_1 * number_2
    else:
        await ctx.send("invalid input")
        return
    await ctx.send("Answer: " + str(output))

@client.command(name="playlist?",
                description="gives u a playlist me and two other people made lol",
                brief="yes")
async def playlist(ctx):
    await ctx.send("https://open.spotify.com/playlist/0ar8hbT78OOYRC5edj7sxE?si=b36cec771d4a4dbd")

@client.command(name="angel",
                description="test",
                brief="something")
async def angel(ctx):
    await ctx.channel.send(ctx.message.author.mention)

@client.command(name="test",
                description="another test thing",
                brief="yeah",
                category="test")
async def test(ctx):
    luck = ["<https://4ng3l.is-raping.me/AcM985JX>", "<https://4ng3l.gorgeous.wtf/ctVH3j0I>", "<https://4ng3l.is-raping.me/aQYp03La>"]
    await ctx.send(f"test your luck {random.choice(luck)}")
    

#@client.command(name="meme",     # these don't work for some dumb ass reason
#                description="sends random memes or something idk",
#                brief="memes woho")
#async def meme(ctx):
#    content = get("https://meme-api.herokuapp.com/gimme").text
#    data = json.loads(content,)
#    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
#    await ctx.reply(embed=meme)

@client.event
async def on_ready():
    print('bot is up and running')