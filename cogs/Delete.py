import json
import os

import discord
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

class delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name="삭제",description='메세지를 갯수만큼 삭제합니다.')
    async def delete_message(self, ctx: commands.Context, 갯수 : int):
        num = 갯수
        role = discord.utils.get(ctx.guild.roles, name="서버관리")
        if role:
            await ctx.channel.purge(limit=num)
            await ctx.channel.send(f'{ctx.author.mention}님! {num}개 만큼의 메세지가 삭제되었습니다.')
        else:
            await ctx.reply("권한이 없습니다.")

async def setup(client):
    await client.add_cog(delete(client),guilds=[discord.Object(id=guild_id)])