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
import datetime#self-explanatory

description = 'A multi-purpose bot made with Discord.py in the rewrite library.'
prefix = '!'
startup_extensions = []

bot = commands.Bot(command_prefix=prefix,description=description)

def pointcheck(ctx):
    return ctx.message.author.id == '276043503514025984' #checks if @Pointless#1278 is the author of the command

@bot.event
async def on_ready():
    print('Successful logging in.')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

if not os.environ.get('TOKEN'):
    print("No token was found.")
bot.run(os.environ.get('TOKEN').strip('"'))