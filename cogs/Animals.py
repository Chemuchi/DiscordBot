import os

import discord
from API.Animal_API import *
from discord.ext import commands

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


class animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='고양이',description='랜덤한 고양이 사진을 불러옵니다.')
    async def cat(self, ctx: commands.Context):
        await ctx.reply (cat())

    @commands.hybrid_command(name='강아지', description='랜덤한 강아지 사진을 불러옵니다.')
    async def dog(self, ctx: commands.Context):
        await ctx.reply(dog())


async def setup(client):
    await client.add_cog(animals(client),guilds=[discord.Object(id=guild_id)])