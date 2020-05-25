import discord
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        member = ctx.message.author.mention

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{member} informe todos os parametros.')

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{member} voce nao tem permissao para fazer isso.')

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f'{member}, este comando nao existe.')


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))

