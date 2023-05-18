# This example requires the 'message_content' intent.

import discord
from discord.app_commands import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$안녕'):
        await message.channel.send('살점은 쓸모없는 부품이다')

    if message.content.startswith('$삭제'):
        await message.channel.purge(limit=30)
        await message.chennel.send('최근 대화기록 30개를 삭제했어요.')



client.run('MTEwODYyNDA1NzYzNDY1MjI0MA.GQfF3E.mTfdsRpzto18dKahoFg5AVp5-548R5phxiXeT4')
