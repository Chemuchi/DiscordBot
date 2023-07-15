import discord
from discord.ext import commands
from API.Word_API import word
from tokens import guild_id

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
    await client.add_cog(s_word(client),guilds=[discord.Object(id=guild_id())])