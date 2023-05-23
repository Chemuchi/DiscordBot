import discord
import random
import datetime
import openpyxl
import asyncio
from tokenp import *
from discord import Game
from datetime import datetime
from pytz import timezone

KST = timezone('Asia/Seoul')
token = token1()
intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user}실행 완료')
async def on_ready():
    await client.change_presence(activity=Game(name="$?, $명령어"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
@client.event#메세지 삭제
async  def on_message(message):
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
    #내정보 (이름,가입일자,아바타)
    if message.content == '$내정보':
        user = message.author
        date = datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        year = str(date.year)
        month = str(date.month)
        day = str(date.day)
        wb = openpyxl.load_workbook('userDB.xlsx')
        sheet = wb.active
        money = 1
        for row in sheet.iter_rows(values_only=True):
            if row[1] == hex(user.id):
                money = row[2]
                break
        embed = discord.Embed(title="유저정보",color =0x9CFF58)
        embed.add_field(name = user,value = "", inline = False)
        embed.add_field(name="디스코드 가입일", value=year+'년 '+month+'월 '+day+"일 ", inline=True)
        embed.add_field(name="소지금", value=str(money) + "원", inline=True)
        embed.set_image(url=user.display_avatar)
        await message.channel.send(embed=embed,reference=message)

    if message.content == '$?':
        embed = discord.Embed(title = "명령어 모음",description="모든 명령어는 $ 접미사를 사용합니다.\n",color =0x9CFF58)
        embed.add_field(name = '삭제 (number)',value='(number)만큼의 메세지를 삭제합니다.',inline=False)
        embed.add_field(name="가위,바위,보",value="$가위, $바위, $보 로 사용합니다. 말그대로 가위바위보를 합니다.",inline=False)
        embed.add_field(name="내정보", value="본인의 이름, 디스코드 가입일자, 아바타를 확인합니다.", inline=False)
        embed.add_field(name="?, 명령어", value="명령어 리스트를 확인합니다.", inline=False)
        embed.add_field(name="등록", value="사용자명, UUID, 돈을 저장할 공간을 만들어줍니다.", inline=False)
        await message.channel.send(embed=embed,reference=message)
    if message.content == '$명령어':
        embed = discord.Embed(title = "명령어 모음",description="모든 명령어는 $ 접미사를 사용합니다.\n",color =0x9CFF58)
        embed.add_field(name = '삭제 (number)',value='(number)만큼의 메세지를 삭제합니다.',inline=False)
        embed.add_field(name="가위,바위,보",value="가위, 바위 또는 보로 사용합니다.",inline=False)
        embed.add_field(name="내정보", value="본인의 이름및태그, 디스코드 가입일자, 아바타를 확인합니다.", inline=False)
        embed.add_field(name="?, 명령어", value="명령어 리스트를 확인합니다.", inline=False)
        embed.add_field(name="등록", value="사용자명, UUID, 돈을 저장할 공간을 만들어줍니다.", inline=False)
        await message.channel.send(embed=embed,reference=message)

    if message.content == "$등록":
        user = message.author
        name = user.name #사용자 정보 가져오기
        user_id = hex(user.id)
        money = int(10000) #기본값
        # Excel 파일 불러오기 또는 생성
        try:
            wb = openpyxl.load_workbook('userDB.xlsx')
            sheet = wb.active
        except FileNotFoundError:
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.append(['이름', 'ID', '돈'])
        #중복값 확인
        for row in sheet.iter_rows(values_only=True):
            if row[1] == user_id:
                embed = discord.Embed(title="유저 등록", description=" \n", color=0x3AE9E9)
                embed.add_field(name='이미 등록되어있는 유저입니다 ✅ ', value=" ", inline=False)
                embed.set_footer(text=message.author.name, icon_url=message.author.display_avatar)
                await message.channel.send(embed=embed, reference=message)

                return
        # 사용자 정보를 Excel 파일에 추가하기
        sheet.append([name, hex(user.id), money])
        wb.save('userDB.xlsx')
        embed = discord.Embed(title = "유저 등록",description="",color =0x3AE9E9)
        embed.add_field(name = message.author.name, value= message.author.id, inline= False)
        embed.set_thumbnail(url = message.author.display_avatar)
        embed.set_footer(text=message.author.name, icon_url=message.author.display_avatar)
        await message.channel.send(embed=embed,reference = message)

    if message.content.startswith("$삭제"):
        # 숫자 파싱
        try:
            num_messages = int(message.content.split()[1])
        except (IndexError, ValueError):
            await message.channel.send("잘못된 입력입니다. $삭제 (number) 형식으로 입력해주세요.",reference = message)
            return

        # 봇이 메시지를 보냄
        bot_message = await message.channel.send("정말 삭제하시겠습니까? 기록으로 남게될것입니다.\n삭제하실려면 아래 이모지를 10초 이내로 클릭해주세요.",reference = message)

        # 체크 표시 이모지 추가
        await bot_message.add_reaction("✅")

        # 체크 표시 이모지 대기
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == "✅"

        try:
            reaction, user = await client.wait_for("reaction_add", timeout=5, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("확인 시간이 초과 되었습니다.",reference = message)
        else:
            # 메시지 삭제
            await message.channel.purge(limit=num_messages + 2)  # +2 커맨드 메세지 + 봇 메세지 포함
            embed = discord.Embed(title="🚧대화내역 삭제🚧", description="", color=0xDF2E2E)
            embed.add_field(name=f"메세지 {num_messages}개가 삭제되었습니다!! ", value="", inline=False)
            embed.set_footer(text=f"삭제자 : {message.author.name}", icon_url=message.author.display_avatar)
            await message.channel.send(embed=embed)
    if message.content == "$돈":
        user = message.author

        wb = openpyxl.load_workbook("userDB.xlsx")
        sheet = wb.active

        money = None
        #돈관련 함수
        for row in sheet.iter_rows(values_only=True):
            if row[1] == hex(user.id):
                money = row[2]
                break
        await message.channel.send(f"{user.name}님의 잔액은 {money}원 입니다.")


client.run(token)


