import discord
import requests
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
    await client.add_cog(facts(client), guilds=[discord.Object(id=guild_id)])