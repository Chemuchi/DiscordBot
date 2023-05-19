import discord
import random
from discord.app_commands import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup


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
    if message.content.startswith('$안녕'):
        await message.channel.send('안녕하세요!')
    #소개
    if message.content.startswith('$소개'):
        await message.channel.send('저는 디스코드 봇이에요.')
    #메세지 삭제
    if message.content.startswith('$삭제'):
        deleted = await message.channel.purge(limit=100)
        await message.channel.send(f'{len(deleted)}개의 메세지를 삭제했어요!')
    #가위바위보
    if message.content.startswith('$가위'):
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            await message.channel.send('가위!')
            await message.channel.send('아 비겼네요~')
        elif bot_response == 2:
            await message.channel.send('바위!')
            await message.channel.send('하하 제가 이겼어요~')
        elif bot_response == 3:
            await message.channel.send('보!')
            await message.channel.send('이런 제가 졌네요..')
    if message.content.startswith('$바위'):
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            await message.channel.send('바위!')
            await message.channel.send('아 비겼네요~')
        elif bot_response == 2:
            await message.channel.send('보!')
            await message.channel.send('하하 제가 이겼어요~')
        elif bot_response == 3:
            await message.channel.send('가위!')
            await message.channel.send('이런 제가 졌네요..')
    if message.content.startswith('$보'):
        bot_response = random.randint(1, 3)
        if bot_response == 1:
            await message.channel.send('보!')
            await message.channel.send('아 비겼네요~')
        elif bot_response == 2:
            await message.channel.send('가위!')
            await message.channel.send('하하 제가 이겼어요~')
        elif bot_response == 3:
            await message.channel.send('바위!')
            await message.channel.send('이런 제가 졌네요..')
    asdf = urlopen("https://hangang.ivlis.kr/")
    bsObject = BeautifulSoup(asdf, "html.parser")
    if message.content.startswith('$한강'):
        await message.channel.send(bsObject.head.title)


client.run('MTEwODYyNDA1NzYzNDY1MjI0MA.GQfF3E.mTfdsRpzto18dKahoFg5AVp5-548R5phxiXeT4')


