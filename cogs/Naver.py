from typing import List

import discord
from API.Naver_API import *
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


class translator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='번역', description='선택한 언어로 번역합니다.')
    async def translator(self, ctx: commands.Context, 문장: str, 언어: str):
        text = " ".join(문장)
        await ctx.reply(translate(text, 언어))
    @translator.autocomplete("언어")
    async def translator_autocomplete(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        cur = ['ko', 'en', 'ja', 'zh-CN', 'zh-TW', 'ru']
        return [
            app_commands.Choice(name=cur, value=cur)
            for cur in cur if current.lower() in cur.lower()
        ]

    @commands.hybrid_command(name='백과사전', description='입력한 단어를 네이버 백과사전에 검색합니다.')
    async def dict(self, ctx: commands.Context, 단어: str):
        await ctx.reply(dic(단어))

    @commands.hybrid_command(name="단축링크",description='입력한 url을 짧게 줄여줍니다.')
    async def short_url(self, ctx: commands.Context, 링크: str):
        await ctx.reply(short_url(링크))


async def setup(client):
    await client.add_cog(translator(client), guilds=[discord.Object(id=guild_id)])