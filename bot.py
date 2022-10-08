#import pynacl
import random
import asyncio
from discord.ext.commands import Bot
import discord
from discord.ext import commands,tasks 
import time
import random

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


@client.command(name='test',  # test
                description="just a test",
                brief="test",
                aliases=['t'],
                pass_context=True)
async def test(ctx):
#   possible_responses = [
#        'this worked!'
#        'this worked 2!'
#    ]
    await ctx.channel.send('this finally works!!!!') # has no attribute say???? #fixedish #! need to fix the command not picking a random choice the command: random.choice(possible.responses)

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
    await ctx.channel.send("the owner of the bot is AngelLoves8008s#6969")

@client.command(name='tol',
                description="tells you if it's a lie or if it's the truth",
                brief="truth or lie")
async def tol(ctx):
    tol = ["the True", "a Lie"]
    await ctx.channel.send(f"What you said is: {random.choice(tol)}")

@client.event
async def on_ready():
    print('bot is up and running')

client.run(TOKEN)