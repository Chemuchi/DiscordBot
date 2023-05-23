import discord
import random
import datetime
from user import *
from token import *
from discord.app_commands import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup

token = token1
intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user}실행 완료')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
@client.event#메세지 삭제
async  def on_message(message):
    if message.content == '$삭제':
        deleted = await message.channel.purge(limit=100)
        await message.channel.send(f'{len(deleted)}개의 메세지를 삭제했어요!',reference=message)
    if message.content == '$가위':
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            await message.channel.send('가위!\n아 비겼네요~',reference=message)
        elif bot_response == 2:
            await message.channel.send('바위!\n하하 제가 이겼어요~',reference=message)
        elif bot_response == 3:
            await message.channel.send('보!\n이런 제가 졌네요..',reference=message)
    if message.content == '$바위':
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            await message.channel.send('바위!\n아 비겼네요~',reference=message)
        elif bot_response == 2:
            await message.channel.send('보!하하 제가 이겼어요~',reference=message)
        elif bot_response == 3:
            await message.channel.send('가위!\n이런 제가 졌네요..',reference=message)
    if message.content == '$보':
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            await message.channel.send('보!\n아 비겼네요~',reference=message)
        elif bot_response == 2:
            await message.channel.send('가위!\n하하 제가 이겼어요~',reference=message)
        elif bot_response == 3:
            await message.channel.send('바위!\n이런 제가 졌네요..',reference=message)
    #내정보(이름,가입일자,아바타)
    if message.content == '$내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        year = str(date.year)
        month = str(date.month)
        day = str(date.day)
        embed = discord.Embed(title="유저정보",color =0x9CFF58)
        embed.add_field(name = user,value = "", inline = False)
        embed.add_field(name="디스코드 가입일", value=year+'년 '+month+'월 '+day+"일 ", inline=True)
        embed.set_image(url=user.display_avatar)
        await message.channel.send(embed=embed,reference=message)
    if message.content == '$?':
        embed = discord.Embed(title = "명령어 모음",description="모든 명령어는 $ 접미사를 사용합니다.\n",color =0x9CFF58)
        embed.add_field(name = '삭제',value='최근 메시지 100개를 삭제합니다.',inline=False)
        embed.add_field(name="가위,바위,보",value="$가위, $바위, $보 로 사용합니다. 말그대로 가위바위보를 합니다.",inline=False)
        embed.add_field(name="내정보", value="본인의 이름, 디스코드 가입일자, 아바타를 확인합니다.", inline=False)
        embed.add_field(name="?, 명령어", value="명령어 리스트를 확인합니다.", inline=False)
        await message.channel.send(embed=embed,reference=message)
    if message.content == '$명령어':
        embed = discord.Embed(title = "명령어 모음",description="모든 명령어는 $ 접미사를 사용합니다.\n",color =0x9CFF58)
        embed.add_field(name = '삭제',value='최근 메시지 100개를 삭제합니다.',inline=False)
        embed.add_field(name="가위,바위,보",value="가위, 바위 또는 보로 사용합니다.",inline=False)
        embed.add_field(name="내정보", value="본인의 이름및태그, 디스코드 가입일자, 아바타를 확인합니다.", inline=False)
        embed.add_field(name="?, 명령어", value="명령어 리스트를 확인합니다.", inline=False)
        await message.channel.send(embed=embed,reference=message)

    if message.content == '$회원가입':
        user = message.author
        signup(user.name, user.id)
        await message.channel.send("정보가 등록되었습니다.",reference = message)

    if message.content == '$유저정보 초기화':
        delete()
        await message.channel.send("Done..", reference=message)

client.run(token)


