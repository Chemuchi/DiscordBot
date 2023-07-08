import discord
from discord.ext import commands
from tokens import token1
import os
import asyncio

client = commands.Bot(command_prefix=".",intents=discord.Intents.all())
guild_id = 913302339518103572

@client.event
async def on_ready():
    await client.tree.sync(guild=discord.Object(id=guild_id))
    print('성공: 봇이 정상적으로 디스코드에 연결되었습니다.')



async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f'cogs.{filename[:-3]}')

@client.hybrid_command(name="핑",description="봇의 핑을 확인합니다.", guild=discord.Object(id=guild_id))
async def ping(ctx: commands.Context):
    await ctx.reply(f"{round(client.latency * 1000)}ms.")

@client.hybrid_command(name="강제종료",description="봇을 강제로 종료합니다. 특별한 역할이 필요합니다.", guild=discord.Object(id=guild_id))
async def force_off(ctx: commands.Context):
    role = discord.utils.get(ctx.guild.roles, name='서버관리')
    if role in ctx.author.roles :
        await ctx.reply('봇을 강제로 종료합니다.')
        await client.close()
    else :
        await ctx.reply('권한이 없습니다.')
async def main():
    async with client:
        await load()
        await client.start(token1())

asyncio.run(main())