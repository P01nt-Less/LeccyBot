import discord
from discord.ext import commands
import random

class owner():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, *choices : str):
        """Chooses between multiple choices."""
        await self.bot.say(random.choice(choices))
        
def setup(bot):
    bot.add_cog(owner(bot))