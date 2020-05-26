import discord
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cogs.{extension}')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f'cogs.{extension}')


def setup(bot):
    bot.add_cog(Owner(bot))
