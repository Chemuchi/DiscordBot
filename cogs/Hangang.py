import json
import os

import discord

from discord.ext import commands
from API.Hangang_API import hangang_temp

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

class hangang(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name="한강", description="코인이라도 떨어지셨나? 호호~")
    async def hangang(self, ctx: commands.Context):
        temp = hangang_temp()
        if temp == '점검중':
            await ctx.reply("현재 시스템이 점검중입니다.")
        elif temp == '온도 정보를 불러오지 못했습니다.':
            await ctx.reply("API 에서 온도 정보를 불러오지 못했습니다.")
        else:
            await ctx.reply(f"현재 한강수온은 {temp}도 입니다.")


async def setup(client):
    await client.add_cog(hangang(client), guilds=[discord.Object(id=guild_id)])