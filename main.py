import discord
from discord.ext import commands
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

@client.tree.command(name="핑",description="봇의 핑을 확인합니다.", guild=discord.Object(id=guild_id))
async def ping(interacton: discord.Interaction):
    await interacton.response.send_message(f"{round(client.latency * 1000)}ms.")

@client.tree.command(name="강제종료",description="봇을 강제로 종료합니다. 특별한 역할이 필요합니다.", guild=discord.Object(id=guild_id))
async def force_off(interaction: discord.Interaction):
    role = discord.utils.get(interaction.guild.roles, name='서버관리')
    if role in interaction.user.roles :
        await interaction.response.send_message('봇을 강제로 종료합니다.')
        await client.close()
    else :
        await interaction.response.send_message('권한이 없습니다.')
async def main():
    async with client:
        await load()
        await client.start("MTEwODYyNDA1NzYzNDY1MjI0MA.G_2ycs.82ybDHUHuUekP0lZ4fH5TIg9nYyL7aJ_4PFRak")

asyncio.run(main())