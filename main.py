import asyncio
import os

import discord
import requests

from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument, CommandInvokeError

from tokenp import token1
from Translate import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="&",intents=discord.Intents.all())

embed_color = 0x7F7F7F


@bot.hybrid_command(name='테스트',description='봇이 작동중인지 확인합니다.')
async def hello(ctx):
    await ctx.reply(f'봇 {bot.user.mention} 정상 작동중 입니다.')

@bot.hybrid_command(name='강제종료',description='봇을 강제로 종료합니다.')
async def force_off(ctx):
    role = discord.utils.get(ctx.guild.roles, name='서버관리')
    if role in ctx.author.roles:
        await ctx.reply('봇을 강제로 종료합니다.')
        await bot.close()
    else:
        await ctx.reply('권한이 없습니다.')

@bot.hybrid_command(name='팩트',description='입력한 숫자에 대한 재밌는 사실을 알려줍니다.')
async def fact(ctx,숫자: int):
    number = 숫자
    fact_embed = discord.Embed(title=f'{number}에 대한 사실',description='',color=embed_color)
    response = requests.get(f'http://numbersapi.com/{number}')
    fact_embed.add_field(name=translate(response.text, 'ko'),value='', inline=False)
    sent_message = await ctx.reply(embed=fact_embed)
@fact.error
async def fact_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        embed = discord.Embed(title="숫자에 대한 사실", description=" ", color=embed_color)
        embed.add_field(name='숫자를 입력해주세요.', value=' ', inline=False)
        await ctx.reply(embed=embed)

@bot.event
async def on_ready():
    print('온라인')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('작동'))
    await bot.tree.sync(guild=discord.Object(id=913302339518103572))
async def setup():
    print('시작하는중..')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await setup()
    await load()
    await bot.start(token1())

asyncio.run(main())