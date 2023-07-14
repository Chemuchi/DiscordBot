import discord
from discord.ext import commands
from tokens import token1
import os
import asyncio

client = commands.Bot(command_prefix=".",intents=discord.Intents.all())
guild_id = 1127150995013640194
owner_id = 298745336506220545
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

@client.hybrid_command(name="강제종료",description="개발자 전용", guild=discord.Object(id=guild_id))
async def force_off(ctx: commands.Context):
    if ctx.author.id == owner_id:
        await ctx.reply("봇을 강제로 종료합니다.")
        await client.close()
    await ctx.reply("개발자가 아닙니다.")



@client.hybrid_command(name="아이디",description="본인의 디스코드 고유번호 를 확인합니다.", guild=discord.Object(id=guild_id))
async def user_id(ctx: commands.Context):
    await ctx.reply(ctx.author.id)






async def main():
    async with client:
        await load()
        await client.start(token1())

asyncio.run(main())