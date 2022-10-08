import random
import asyncio
from discord.ext.commands import Bot
import discord
from discord.ext import commands,tasks 
import time


class all_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

@commands.command(name='ping',  # ping
                description="kinda shows what latency the bot has",
                brief="base ping command",
                aliases=['pp'])
async def ping(ctx):
    await ctx.channel.send(f'Pong! Responded in {round(commands.latency * 1000)} ms')


@commands.command(name='test',  # test
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

@commands.command(name='ding',  # ding lmao
                description="another form for the ping command",
                brief="other form of ping",
                aliases=['dd'])
async def ding(ctx):
    await ctx.channel.send(f'dong! Responded in {round(commands.latency * 1000)} ms')

@commands.command(name='pinger', # pinger 
                description="pings you lmao",
                brief="pings you",
                aliases=['pmp'])
async def pinger(ctx):
    await ctx.channel.send(ctx.message.author.mention + ' get pinged fucker')


def setup(client):
    client.add_cog(all_commands(client))