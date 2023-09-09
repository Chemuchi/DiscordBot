import discord
from discord.ext import commands
import os
import asyncio
import json

with open("config.json","r") as f:
    config = json.load(f)
owner_id = config['owner_id']['id']
guild_id = config['guild_id']['id']
command_prefix = config['command_prefix']['value']
delete_rule = config['delete_rule']['rule']

client = commands.Bot(command_prefix=command_prefix,intents=discord.Intents.all())



token = input("실행을 위해 봇 토큰을 입력해주세요. >> ")
print("토큰이 확인되었습니다.")
print("연결중입니다..")

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
    await ctx.reply(f"봇의 현재 핑은 {round(client.latency * 1000)}ms 입니다.")

@client.hybrid_command(name="강제종료",description="봇 관리자 전용", guild=discord.Object(id=guild_id))
async def force_off(ctx: commands.Context):
    if ctx.author.id == owner_id:
        await ctx.reply("봇을 강제로 종료합니다.")
        await client.close()
    await ctx.reply("봇 관리자가 아닙니다.")

@client.hybrid_command(name="아이디",description="본인의 디스코드 고유번호 를 확인합니다.", guild=discord.Object(id=guild_id))
async def user_id(ctx: commands.Context):
    await ctx.reply(ctx.author.id)

@client.hybrid_command(name='정보',description='봇의 정보를 확인합니다.',guild=discord.Object(id=guild_id))
async def info(ctx: commands.Context):
    embed = discord.Embed(color=0xFFFFFF,title='개인 프로젝트용 디스코드봇',)
    embed.set_author(name='UselessBot')
    embed.add_field(name='하이브리드 커맨드를 지원합니다.',value=f'command prefix는 config 에서 변경 가능합니다.\n현재 설정은 {command_prefix} 입니다.',inline=False)
    embed.add_field(name='현재 서버의 봇 관리자는 config 에 디스코드 아이디를 기입해주세요.',value='봇 관리자만이 디스코드 내에서 봇 강제종료가 가능합니다.',inline=False)
    embed.add_field(name='명령어 확인은 채팅창에 / 입력후 나오는 UselessBot 아이콘을 눌러주세요.',value='지원하는 명령어들과 설명을 확인 가능합니다.',inline=False)
    embed.add_field(name='몇몇 명령어들은 토큰을 발급 받은 후 사용가능합니다.',value='각각 발급받은 토큰들은 config 파일 알맞은 곳에 입력해주세요.')
    await ctx.reply(embed=embed)





async def main():
    async with client:
        await load()
        await client.start(token)

asyncio.run(main())