import discord
from Imgur_API import get_random_image, random_words
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument, CommandInvokeError


class Imgur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Imgur Cog 로드함.')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f'len{fmt}개의 커맨드가 싱크되었습니다.')
        return


    @commands.hybrid_command(name='랜덤이미지',description='imgur 에서 랜덤한 이미지를 가져옵니다.')
    async def imgur_random_word(self,ctx: commands.Context):
        image_url = get_random_image(random_words())
        search_word = str(random_words())
        await ctx.reply(image_url)


    @commands.hybrid_command(name='imgur',description='imgur 에서 이미지를 검색합니다.')
    async def imgur_random_image(self, ctx: commands.Context, 검색어: str):
        text = ' '.join(검색어)
        image_url = get_random_image(text)
        await ctx.reply(image_url)
async def setup(bot):
    await bot.add_cog(Imgur(bot),guilds=[discord.Object(id=913302339518103572)])