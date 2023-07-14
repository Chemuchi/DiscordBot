import discord
import requests
from API.Naver_API import *
from discord.ext import commands
from discord import app_commands

from tokens import guild_id


class facts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='팩트', description='입력한 숫자에 대한 재밌는 사실을 알려줍니다.')
    async def facts(self, ctx: commands.Context, 숫자: int):
        number = 숫자
        response = requests.get(f'http://numbersapi.com/{number}')
        await ctx.reply(translate(response.text, "ko"))

async def setup(client):
    await client.add_cog(facts(client), guilds=[discord.Object(id=guild_id())])