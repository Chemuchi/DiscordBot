import discord
from discord.ext import commands
from setting import guild_id, embed_color

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
        del_embed = discord.Embed(title=f':scissors:메세지 삭제:scissors:', color=embed_color())
        if role:
            await ctx.channel.purge(limit=num)
            del_embed.add_field(name=f'{num}개의 메세지가 삭제되었습니다.',value=f'삭제자 : {ctx.author.mention}')
            await ctx.send(embed=del_embed)
        else:
            del_embed.add_field(name="권한이 없습니다.", value=f'실행자 : {ctx.author.mention}')
            await ctx.send(embed=del_embed)


async def setup(client):
    await client.add_cog(delete(client),guilds=[discord.Object(id=guild_id())])