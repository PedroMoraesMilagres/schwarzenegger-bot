import discord
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # Comando para o bot repetir algo
    async def echo(self, ctx, *args):
        output = ''
        for word in args:
            output += word
            output += ' '
        await ctx.send(output)

    @commands.command()
    async def kill(self, ctx, member: discord.Member):
        await ctx.send(f'Hasta la vista {member.mention}!')


def setup(bot):
    bot.add_cog(Fun(bot))
