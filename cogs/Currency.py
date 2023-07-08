from typing import List

import discord
from currency_converter import CurrencyConverter

from discord.ext import commands
from discord import app_commands

from tokens import guild_id



class currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='환율',description='실시간 환율로 계산을 해줍니다.')
    async def currency(self, ctx: commands.Context, 기준_통화: str, 목표_통화: str, 금액: int):
        c = CurrencyConverter()
        amount = c.convert(금액, 기준_통화, 목표_통화)
        currency_embed = discord.Embed(title="환율 계산",description="",color= 0x7F7F7F)
        currency_embed.add_field(name=f"{금액:,.0f}", value=기준_통화, inline = True)
        currency_embed.add_field(name=":currency_exchange:" , value="", inline=True)
        currency_embed.add_field(name=f"{amount:,.2f}", value=목표_통화, inline=True)
        currency_embed.set_footer(text=f"1 {기준_통화} = {c.convert(1, 기준_통화, 목표_통화):,.7f} {목표_통화}")
        await ctx.reply(embed=currency_embed)

    @currency.autocomplete("기준_통화")
    async def currency_autocomplete1(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        cur = ['CAD', 'ISK', 'PHP', 'LVL', 'PLN', 'MTL', 'JPY', 'USD', 'KRW', 'RUB', 'TRY', 'HRK', 'HKD', 'EUR', 'CZK',
               'IDR', 'NZD', 'ZAR', 'CYP', 'HUF', 'CNY', 'SEK', 'DKK', 'AUD', 'GBP']
        return [
            app_commands.Choice(name=cur, value=cur)
            for cur in cur if current.lower() in cur.lower()
        ]

    @currency.autocomplete("목표_통화")
    async def currency_autocomplete2(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        cur = ['CAD', 'ISK', 'PHP', 'LVL', 'PLN', 'MTL', 'JPY', 'USD', 'KRW', 'RUB', 'TRY', 'HRK', 'HKD', 'EUR', 'CZK',
               'IDR', 'NZD', 'ZAR', 'CYP', 'HUF', 'CNY', 'SEK', 'DKK', 'AUD', 'GBP']
        return [
            app_commands.Choice(name=cur, value=cur)
            for cur in cur if current.lower() in cur.lower()
        ]




async def setup(client):
    await client.add_cog(currency(client), guilds=[discord.Object(id=guild_id())])

