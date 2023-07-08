from typing import List

import discord
from API.Translate_API import *
from discord.ext import commands
from discord import app_commands

from tokens import guild_id


class translator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")

    @commands.hybrid_command(name='번역', description='선택한 언어로 번역합니다.')
    async def translator(self, ctx: commands.Context, 문장: str, 언어: str):
        text = " ".join(문장)
        await ctx.reply(translate(text, 언어))
    @translator.autocomplete("언어")
    async def translator_autocomplete(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        cur = ['ko', 'en', 'ja', 'zh-CN', 'zh-TW', 'ru']
        return [
            app_commands.Choice(name=cur, value=cur)
            for cur in cur if current.lower() in cur.lower()
        ]


async def setup(client):
    await client.add_cog(translator(client), guilds=[discord.Object(id=guild_id())])