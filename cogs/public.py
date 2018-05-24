import discord
from discord.ext import commands
class Public(object):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='oof')
    async def oof(self,ctx):
        await self.bot.say('hi!')
def setup(bot):
    bot.add_cog(Public(bot))