import discord

from API.Imgur_API import *
from discord.ext import commands
from discord import app_commands

from tokens import guild_id


class Imgur(commands.Cog):
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
    await client.add_cog(Imgur(client),guilds=[discord.Object(id=guild_id())])