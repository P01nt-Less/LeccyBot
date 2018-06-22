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
import os # operating system stuff and also heroku
from os import listdir #cogs
from os.path import isfile, join #cogs
import datetime#self-explanatory
import logging #logging

description = 'A multi-purpose bot made with Discord.py in the Async library.'
prefix = '.'


bot = commands.Bot(command_prefix=prefix,description=description)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Successful logging in.')
    print('https://discordapp.com/oauth2/authorize?client_id=449301359578316811&scope=bot&permissions=2146958591')
    bot.session = aiohttp.ClientSession()
    presence=['!help | May the Leccy be with us.','!help | Python > Javascript','!help | OOF ~ Noob - 2006','!help | Press \'L\' to pay for my electricity bills.','!help | My friend told me how electricity is measured and I was like \'Watt?!?\'','!help | If you plant a light bulb in your garden, does it grow into a power plant?','!help | OOH ~ Old Steve - 2011','!help | https://discord.gg/c8vNvfR is where you should really go.','!help | Heroku doesn\'t suck!','!help | Made by @Pointless#1278','!help | Hello there.','!help | Quite strange, isn\'t it?','!help | BEEP BOOP','!help | Why are you reading these?','!help | Press F to pay respects.','!help | 9 + 10 = 21','!help | The Illuminati is watching.','!help | R.I.P Harambe 2016','!help | Somebody Toucha My Leccy!','!help | Faster than Windows 1.0!','!help | ?','!help | !','!help | Welp...','!help | print(party() + \'!\')','!help | Gotta go fast!']
    while True:
        await bot.change_presence(game=discord.Game(name=random.choice(presence)))
        await asyncio.sleep(5)

@bot.command()
async def help(helpc: str = None,ctx):
    '''Test'''
    if helpc == None:
        embed=discord.Embed(title='Test', color=0x0000ff)
        embed.add_field(name='Test', value='Test', inline=False)
        await ctx.send(embed=embed)
    if helpc:
        getcommand = bot.get_command(helpc)
        await bot.say(f'{helpc}: {getcommand.help}\nUsage: .{getcommand.signature}')
    elif helpc is None:
        await bot.say('That command doesn\'t exist.')

if not os.environ.get('TOKEN'):
    print("No token found!")
bot.run(os.environ.get('TOKEN').strip('"'))