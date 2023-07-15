import discord, random
from discord.ext import commands
from API.Word_API import *
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

    #역량 부족
    '''@commands.hybrid_command(name='끝말잇기', description='AI와 끝말잇기를 합니다.')
    async def wordchain(self,ctx: commands.Context):
        thread = await ctx.channel.create_thread(
            name=f"{ctx.author}의 {random.randint(1,100000)}번 끝말잇기 쓰레드",
            type=discord.ChannelType.private_thread,
        )
        await thread.add_user(ctx.author)
        await ctx.send(f"{thread.name} 에서 이동후 진행해주세요.")
        await thread.send("제시어를 입력해주세요.")
        def check(m):
            m.channel == thread and m.author == ctx.author
            return

        while True :
            message = await self.bot.wait_for('message', check=check)
            word = message.content
            if not is_valid_word(word) :
                await thread.send("잘못된 단어입니다. 다시 입력하세요.")
                continue
            last_word = word[-1]
            word = choose_next_word(last_word)
            if not word :
                await thread.send("AI가 이겼습니다!")
                break
            await thread.send(f"AI의 단어: {word}")
            last_word = word[-1]
            await thread.send(f"다음 단어를 입력하세요 ({last_word}): ")'''






async def setup(client):
    await client.add_cog(s_word(client),guilds=[discord.Object(id=guild_id())])