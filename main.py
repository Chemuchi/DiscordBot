import discord
import random
import datetime
from discord.app_commands import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup

token = 'MTEwODYyNDA1NzYzNDY1MjI0MA.GQfF3E.mTfdsRpzto18dKahoFg5AVp5-548R5phxiXeT4'
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
    #인사
    if message.content == '$안녕':
        await message.channel.send('안녕하세요!',reference=message)
    #소개
    if message.content == '$소개':
        await message.channel.send('저는 디스코드 봇이에요.',reference=message)
    #메세지 삭제
    if message.content == '$삭제':
        deleted = await message.channel.purge(limit=100)
        await message.channel.send(f'{len(deleted)}개의 메세지를 삭제했어요!',reference=message)
    #가위바위보
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


client.run(token)


