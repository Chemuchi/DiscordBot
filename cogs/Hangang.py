import discord

from discord.ext import commands
from API.Hangang_API import hangang_temp
from setting import guild_id, embed_color

class hangang(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name="한강", description="코인이라도 떨어지셨나? 호호~")
    async def hangang(self, ctx: commands.Context):
        temp = hangang_temp()
        han_embed = discord.Embed(title=f"한강 수온:thermometer:", color=embed_color())
        if temp == '점검중':
            han_embed.add_field(name=f"현재 시스템이 점검중입니다.",value="나중에 시도해주세요.",inline=False)
            await ctx.send(embed=han_embed)
            print(temp)
        elif temp == '온도 정보를 불러오지 못했습니다.':
            han_embed.add_field(name="API 에서 온도 정보를 불러오지 못했습니다.",value='나중에 시도해주세요.',inline=False)
            await ctx.send(embed=han_embed)
            print(temp)
        else:
            han_embed.add_field(name=f"현재 한강의 수온은 {temp}도 입니다.",value='',inline=False)
            await ctx.send(embed=han_embed)
            print(temp)


async def setup(client):
    await client.add_cog(hangang(client), guilds=[discord.Object(id=guild_id())])