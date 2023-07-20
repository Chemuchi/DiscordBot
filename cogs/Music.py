import asyncio

import discord
import yt_dlp as youtube_dl
from yt_dlp import YoutubeDL
from discord.ext import commands

from tokens import guild_id

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.queue = []

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    def play_next(self, ctx, player):
        self.queue[0] = player

        i = 0
        while i < len(self.queue):
            try:
                ctx.voice_client.play(self.queue[i], after=lambda e: print('Player error: %s' % e) if e else None)

            except:
                pass
            i += 1

    @commands.hybrid_command(name='재생', aliases=['p', 'ㅔ'], description='노래를 재생합니다.')
    async def stream(self, ctx: commands.Context, url: str):
        """Streams from a url (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            if len(self.queue) == 0:
                self.play_next(ctx.voice_client, player)
                await ctx.reply(f'지금 재생중: {player.title}')
            else:
                self.queue[len(self.queue)] = player
                await ctx.reply(f'지금 재생중: {player.title}')




    @commands.hybrid_command(name='볼륨', aliases=['v', 'ㅂ'], description='볼륨을 조정합니다.')
    async def volume(self, ctx: commands.Context, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.reply(f"볼륨을 {volume}% 로 조정합니다.")

    @commands.hybrid_command(name='종료', aliases=['stop', 'leave', 'l'], description='노래를 종료하고 내보냅니다.')
    async def stop(self, ctx: commands.Context):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()
        await ctx.reply("노래를 종료하고 방에서 나갑니다.")



    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__}이 성공적으로 로드됨.")


async def setup(client):
    await client.add_cog(music(client), guilds=[discord.Object(id=guild_id())])
