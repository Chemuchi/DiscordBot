import discord
import requests
from API.Naver_API import *
from discord.ext import commands
from setting import guild_id

class facts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='tmi', description='입력한 숫자에 대한 TMI를 알려줍니다.')
    async def facts(self, ctx: commands.Context, 숫자: int):
        number = 숫자
        response = requests.get(f'http://numbersapi.com/{number}')
        trans = translate(response.text, "ko")
        fact_embed = discord.Embed(title=f'{number} 에 대한 TMI')
        fact_embed.add_field(name=trans, value=response.text)
        await ctx.reply(embed=fact_embed)

async def setup(client):
    await client.add_cog(facts(client), guilds=[discord.Object(id=guild_id())])