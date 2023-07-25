import discord
from discord.ext import commands
from tokens import guild_id

class qr_gen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='qr',description='입력한 링크로 연결되는 QR코드를 만들어줍니다.')
    async def cat(self, ctx: commands.Context, url: str):
        await ctx.reply(f"https://chart.apis.google.com/chart?cht=qr&chs=250x250&chl={url}")



async def setup(client):
    await client.add_cog(qr_gen(client),guilds=[discord.Object(id=guild_id())])