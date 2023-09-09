import json
import os
from typing import List

import discord
from currency_converter import CurrencyConverter

from discord.ext import commands
from discord import app_commands

# 현재 스크립트 파일의 경로를 얻습니다.
script_dir = os.path.dirname(os.path.abspath(__file__))
# 상위 폴더의 경로를 얻습니다.
parent_dir = os.path.dirname(script_dir)
# config.json 파일의 경로를 생성합니다.
config_path = os.path.join(parent_dir, 'config.json')

# 파일을 읽어올 때 config_path를 사용합니다.
with open(config_path, 'r') as f:
    config = json.load(f)
guild_id = config['guild_id']['id']



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
    await client.add_cog(currency(client), guilds=[discord.Object(id=guild_id)])

