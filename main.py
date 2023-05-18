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
        await message.channel.send('안녕하세요!')
    if message.content.startswith('$삭제'):
        deleted = await message.channel.purge(limit=100)
        await message.channel.send(f'{len(deleted)}개의 메세지를 삭제했어요!')


client.run('MTEwODYyNDA1NzYzNDY1MjI0MA.GQfF3E.mTfdsRpzto18dKahoFg5AVp5-548R5phxiXeT4')
