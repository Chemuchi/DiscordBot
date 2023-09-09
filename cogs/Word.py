import discord
from discord.ext import commands
from API.Word_API import *

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

class s_word(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='사전',description='단어의 뜻을 검색합니다.')
    async def search_word(self,ctx: commands.Context, 단어: str):
        search = 단어
        data = word(search)
        word_embed = discord.Embed(title=f':book: {search}',description='',color=0x7F7F7F)
        for i, definition in enumerate(data):
            word_embed.add_field(name=" ", value=f"**【{i + 1}】** {definition}", inline=False)
        await ctx.reply(embed = word_embed)



async def setup(client):
    await client.add_cog(s_word(client),guilds=[discord.Object(id=guild_id)])