import discord
from discord.ext import commands
from setting import guild_id

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
    await client.add_cog(delete(client),guilds=[discord.Object(id=guild_id())])