import discord

from Imgur_API import *
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

    @app_commands.command(name='랜덤이미지', description='imgur 에서 랜덤한 이미지를 가져옵니다.')
    async def imgur_random_word_image(self, interaction: discord.Interaction) :
        image_url = get_random_image(random_words())
        search_word = str(random_words())
        await interaction.response.send_message(image_url)

    @app_commands.command(name='imgur', description='imgur 에서 입력한 단어로 이미지를 검색합니다.')
    async def imgur_search_image(self, interaction: discord.Interaction, 검색어: str) :
        text = ' '.join(검색어)
        image_url = search_imgur(text)
        await interaction.response.send_message(image_url)

async def setup(client):
    await client.add_cog(Imgur(client),guilds=[discord.Object(id=guild_id())])