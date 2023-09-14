import discord
from API.Animal_API import *
from discord.ext import commands
from setting import guild_id

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
    await client.add_cog(animals(client),guilds=[discord.Object(id=guild_id())])