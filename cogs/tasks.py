import discord
from discord.ext import commands, tasks


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

def setup(bot):
    bot.add_cog(Tasks(bot))
