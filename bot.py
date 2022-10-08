#import pynacl
import discord
from discord.ext import commands
from discord.ext.commands import Context

BOT_PREFIX = "`"
TOKEN = "MTAyNjQ5NzMyMjAwMTEwOTAyMg.GOiYn2.JQend8HmDRgnUAGzA6rYGPSMjYVfKbEtmeEVJk"

intents = discord.Intents().all()

client = commands.Bot(command_prefix=BOT_PREFIX, intents = intents)

@client.command()
async def load(ctx: Context, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Loaded Cog")

@client.command()
async def unload(ctx: Context, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("Unloaded Cog")

@client.command()
async def reload(ctx: Context, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Reloaded Cog")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[0:-3]}')

@client.event
async def on_ready():
    print('bot is up and running')

client.run(TOKEN)