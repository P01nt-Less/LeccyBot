#Discord imports
import discord
from discord.ext import commands
#Others
import traceback # Error tracing
import random # Randomizing
from random import randint # (I don't normally use but also I want this)
import aiohttp # Never requests library
import sys # for system-specific paramaters and functions
import re # for regular expression operations
import json # self-explanatory
import time # self-explanatory
import asyncio # tasks
import os # operating system stuff and also heroku lel
from os import listdir
from os.path import isfile, join
import datetime#self-explanatory
import logging #logging

description = 'A multi-purpose bot made with Discord.py in the Async library.'
prefix = '!'


bot = commands.Bot(command_prefix=prefix,description=description)

def pointcheck(ctx):
    return ctx.message.author.id == '276043503514025984' #checks if @Pointless#1278 is the author of the command

@bot.event
async def on_ready():
    print('Successful logging in.')
    print('https://discordapp.com/oauth2/authorize?client_id=449301359578316811&scope=bot&permissions=2146958591')
    await LoadCogs()

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

async def LoadCogs():
    for extension in [f.replace('.py', '') for f in listdir('cogs') if isfile(join('cogs', f))]:
        try:
            if not "__init__" in extension:
                print("Loading {}...".format(extension))
                bot.load_extension('cogs.' + extension)
        except Exception as e:
            print('Failed to load cog {}'.format(extension))
            traceback.print_exc()
def Main():
    logging.basicConfig(level=logging.INFO)
    if not os.environ.get('TOKEN'):
        print("No token was found.")
    bot.run(os.environ.get('TOKEN').strip('"'))

if __name__ == '__main__':
    Main()