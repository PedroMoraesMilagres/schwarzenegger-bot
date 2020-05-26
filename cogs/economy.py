import discord
import requests
import json
from discord.ext import commands

request = requests.get('https://economia.awesomeapi.com.br/json/all/USD-BRL,USDT-BRL,EUR-BRL,BTC-BRL')
cotacao = json.loads(request.text)


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dolar(self, ctx):
        await ctx.send(f"{cotacao['USD']['name']}\n\tCompra: {cotacao['USD']['bid']}\n\tVenda: {cotacao['USD']['ask']}"
                       f"\n\tVariacao:{cotacao['USD']['varBid']}\n\tAlta: {cotacao['USD']['high']}"
                       f"\n\tBaixa: {cotacao['USD']['low']}")

    @commands.command()
    async def dolart(self, ctx):
        await ctx.send(f"{cotacao['USDT']['name']}\n\tCompra: {cotacao['USDT']['bid']}\n\tVenda: {cotacao['USDT']['ask']}"
                       f"\n\tVariacao: {cotacao['USDT']['varBid']}\n\tAlta: {cotacao['USDT']['high']}"
                       f"\n\tBaixa: {cotacao['USDT']['low']}")

    @commands.command()
    async def bitcoin(self, ctx):
        await ctx.send(f"{cotacao['BTC']['name']}\n\tCompra: {cotacao['BTC']['bid']}\n\tVenda: {cotacao['BTC']['ask']}"
                       f"\n\tVariacao: {cotacao['BTC']['varBid']}\n\tAlta: {cotacao['BTC']['high']}"
                       f"\n\tBaixa: {cotacao['BTC']['low']}")

    @commands.command()
    async def euro(self, ctx):
        await ctx.send(f"{cotacao['EUR']['name']}\n\tCompra: {cotacao['EUR']['bid']}\n\tVenda: {cotacao['EUR']['ask']}"
                       f"\n\tVariacao: {cotacao['EUR']['varBid']}\n\tAlta: {cotacao['EUR']['high']}"
                       f"\n\tBaixa: {cotacao['EUR']['low']}")


def setup(bot):
    bot.add_cog(Economy(bot))
