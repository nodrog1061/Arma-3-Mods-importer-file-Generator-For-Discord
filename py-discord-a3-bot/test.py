import discord
from discord.ext import commands
import makeHtml
import getWorkshop
from decouple import config

description = '''A bot that is used for generating information about the TFM mod collection.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def collection(ctx, colectionId = config('DEFAULT-COLLECTION-ID')):
    """sends the steam collection"""
    # responce = json.dumps(steamtest.getColection(colectionId), indent=0).replace('{', '').replace('}', '')

    makeHtml.generateHtml(colectionId)
    print("file requested")

    await ctx.send("Generating Mod import file from collection", file=discord.File(r'results/'+config('MOD-COLLECTION-FILENAME')+'.html'))

@bot.command()
async def howmany(ctx, colectionId = config('DEFAULT-COLLECTION-ID')):
    """tells you how many items are in the colection"""

    collection = getWorkshop.getColection(colectionId)
    print("number of mods requested")

    await ctx.send("The Mod Collection is "+collection['itemcount']+" mods")



bot.run(config('DISCORD-BOT-KEY'))
