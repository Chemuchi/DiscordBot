import discord

from API.Imgur_API import *
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


class imgur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='랜덤이미지', description='imgur 에서 랜덤한 이미지를 가져옵니다.')
    async def imgur_random_word_image(self, ctx: commands.Context) :
        image_url = get_random_image(random_words())
        await ctx.reply(image_url)

    @commands.hybrid_command(name='imgur', description='imgur 에서 입력한 단어로 이미지를 검색합니다.')
    async def imgur_search_image(self, ctx: commands.Context, 검색어: str) :
        text = ' '.join(검색어)
        image_url = get_random_image(text)
        await ctx.reply(image_url)

async def setup(client):
    await client.add_cog(imgur(client),guilds=[discord.Object(id=guild_id)])