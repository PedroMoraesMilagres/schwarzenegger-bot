import discord
import requests
import json
from discord.ext import commands


request = requests.get('https://economia.awesomeapi.com.br/json/all')

cotacao = json.loads(request.text)

cotacao_usd = cotacao['USD']

name = cotacao_usd['name']
compra = cotacao_usd['bid']


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dolar(self, ctx):
        await ctx.send(f"{name} \nCompra: {compra}")


def setup(bot):
    bot.add_cog(Economy(bot))
