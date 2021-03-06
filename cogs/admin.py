import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events

    # Commands

    # Comando para limpar o chat
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{amount} Messages deleted.')

    # Comando para banir um usuario
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None, delete_message_days=1):
        await member.ban(reason=reason, delete_message_days=delete_message_days)
        await ctx.send('Hasta la vista baby!')
        await ctx.send(f'{member.mention} foi banido. \nMotivo: {reason}')

    # Comando para desbanir um usuario
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def pardon(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name and user.discriminator) == (member_name and member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name}#{user.discriminator} foi desbanido.')

    # Comando para kickar um usuario
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} foi kickado. \nMotivo: {reason}')
        return


def setup(bot):
    bot.add_cog(Admin(bot))
