import discord
import requests
import json

from discord.ext import commands
from discord import app_commands

from tokens import guild_id


class hangang(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name="한강", description="코인이라도 떨어지셨나? 호호~")
    async def hangang(self, ctx: commands.Context):
        response = requests.get('https://api.hangang.msub.kr/')
        data = json.loads(response.text)
        temp = data['temp']
        if temp == '점검중':
            await ctx.reply("현재 시스템이 점검중입니다.")
        elif temp == '온도 정보를 불러오지 못했습니다.':
            await ctx.reply("API 에서 온도 정보를 불러오지 못했습니다.")
        else:
            await ctx.reply(f"현재 한강수온은 {temp}도 입니다.")


async def setup(client):
    await client.add_cog(hangang(client), guilds=[discord.Object(id=guild_id())])