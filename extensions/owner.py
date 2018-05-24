import main

class Owner():
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Owner(bot))