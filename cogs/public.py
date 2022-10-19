import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3
import os
import time
from collections import OrderedDict, deque, Counter
import math
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
from io import BytesIO
import requests
import aiohttp
from .utils import checks
import traceback


class Public(commands.Cog, name='Rank'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bot', aliases=['info', 'botinfo'])
    async def _bot(self, ctx):
        embed = discord.Embed(title='Bot Information', description='Created by Jared#5984', color=0xff003d)

        embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/gf8sjTwr0DCWMKpYuNd8yXlzvywht43aRWh6QjnMPw0/%3Fsize%3D128/https/cdn.discordapp.com/avatars/648362865048420373/bf8b2c1ed038e8d19f8863db3fba526c.png')
        embed.set_footer(text='Leveling', icon_url='https://images-ext-2.discordapp.net/external/gf8sjTwr0DCWMKpYuNd8yXlzvywht43aRWh6QjnMPw0/%3Fsize%3D128/https/cdn.discordapp.com/avatars/648362865048420373/bf8b2c1ed038e8d19f8863db3fba526c.png')

        embed.add_field(name='**Total Guilds**', value=f'`{len(list(self.bot.guilds))}`', inline=True)
        embed.add_field(name='**Total Users**', value=f'`{len(list(self.bot.users))}`', inline=True)
        channel_types = Counter(isinstance(c, discord.TextChannel) for c in self.bot.get_all_channels())
        text = channel_types[True]
        embed.add_field(name='**Total Channels**', value=f'`{text}`', inline=True)
        embed.add_field(name='**Python Version**', value='`3.7`', inline=True)
        embed.add_field(name='**Discord.py Version**', value='`1.2.5`', inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    
    
    @commands.command(name='help')
    async def _help(self, ctx):
        embed = discord.Embed(title="Bot Help", description="Created by Jared#5984", color=0xff003d)

        embed.set_footer(text='Leveling', icon_url='https://images-ext-2.discordapp.net/external/gf8sjTwr0DCWMKpYuNd8yXlzvywht43aRWh6QjnMPw0/%3Fsize%3D128/https/cdn.discordapp.com/avatars/648362865048420373/bf8b2c1ed038e8d19f8863db3fba526c.png')
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_field(name="**Ranks**", value="`lv.ranks` - Shows info for ranks commands\n lv.ranks list` - Lists all current ranks")
        embed.add_field(name="**Leveling**", value="`lv.leveling` - Shows info for leveling commands")
        embed.add_field(name="**General**", value="`lv.rank <@user>` - Shows rank info for a user\n`?leaderboard` - Shows top 5 leaderboard")

        await ctx.send(embed=embed)
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
            error_ch = self.bot.get_channel(1011469317822496858)
            if isinstance(error, discord.ext.commands.errors.MissingPermissions):
                embed = discord.Embed(title=":x: 失敗 -MissingPermissions", description=f"実行者の必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
                embed.set_footer(text="お困りの場合はBot管理者までお問い合わせください")
                await ctx.send(embed=embed)
                e = discord.Embed(title='エラー情報', description='',  timestamp=ctx.message.created_at, color=discord.Colour.red())
                e.add_field(name='エラーが発生したサーバー', value=ctx.message.guild.name, inline=False)
                e.add_field(name='エラーが発生したチャンネル', value=ctx.message.channel.name, inline=False)
                e.add_field(name='エラーid', value=ctx.message.id, inline=False)
                e.add_field(name='エラーが発生したコマンド', value=ctx.message.content, inline=False)
                e.add_field(name='エラーを発生させた人', value=ctx.author, inline=False)
                e.add_field(name='エラー内容', value=error, inline=False)
                await error_ch.send(embed=e)
            elif isinstance(error, discord.ext.commands.errors.NotOwner):
                embed = discord.Embed(title=":x: 失敗 -MissingPermissions", description=f"実行者の必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
                embed.set_footer(text="お困りの場合はBot管理者までお問い合わせください")
                await ctx.send(embed=embed)
                e = discord.Embed(title='エラー情報', description='',  timestamp=ctx.message.created_at, color=discord.Colour.red())
                e.add_field(name='エラーが発生したサーバー', value=ctx.message.guild.name, inline=False)
                e.add_field(name='エラーが発生したチャンネル', value=ctx.message.channel.name, inline=False)
                e.add_field(name='エラーid', value=ctx.message.id, inline=False)
                e.add_field(name='エラーが発生したコマンド', value=ctx.message.content, inline=False)
                e.add_field(name='エラーを発生させた人', value=ctx.author, inline=False)
                e.add_field(name='エラー内容', value=error, inline=False)
                await error_ch.send(embed=e)
            elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
                embed = discord.Embed(title=":x: 失敗 -BotMissingPermissions", description=f"Botの必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
                embed.set_footer(text="お困りの場合はBot管理者までお問い合わせください")
                await ctx.send(embed=embed)
                e = discord.Embed(title='エラー情報', description='',  timestamp=ctx.message.created_at, color=discord.Colour.red())
                e.add_field(name='エラーが発生したサーバー', value=ctx.message.guild.name, inline=False)
                e.add_field(name='エラーが発生したチャンネル', value=ctx.message.channel.name, inline=False)
                e.add_field(name='エラーid', value=ctx.message.id, inline=False)
                e.add_field(name='エラーが発生したコマンド', value=ctx.message.content, inline=False)
                e.add_field(name='エラーを発生させた人', value=ctx.author, inline=False)
                e.add_field(name='エラー内容', value=error, inline=False)
                await error_ch.send(embed=e)
            elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
                embed = discord.Embed(title=":x: 失敗 -CommandNotFound", description=f"不明なコマンドもしくは現在使用不可能なコマンドです。", timestamp=ctx.message.created_at, color=discord.Colour.red())
                embed.set_footer(text="お困りの場合はBot管理者までお問い合わせください")
                await ctx.send(embed=embed)
                e = discord.Embed(title='エラー情報', description='',  timestamp=ctx.message.created_at, color=discord.Colour.red())
                e.add_field(name='エラーが発生したサーバー', value=ctx.message.guild.name, inline=False)
                e.add_field(name='エラーが発生したチャンネル', value=ctx.message.channel.name, inline=False)
                e.add_field(name='エラーid', value=ctx.message.id, inline=False)
                e.add_field(name='エラーが発生したコマンド', value=ctx.message.content, inline=False)
                e.add_field(name='エラーを発生させた人', value=ctx.author, inline=False)
                e.add_field(name='エラー内容', value=error, inline=False)
                await error_ch.send(embed=e)
            elif isinstance(error, discord.ext.commands.errors.MemberNotFound):
                embed = discord.Embed(title=":x: 失敗 -MemberNotFound", description=f"指定されたメンバーが見つかりません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
                embed.set_footer(text="お困りの場合はBot管理者までお問い合わせください")
                await ctx.send(embed=embed)
                e = discord.Embed(title='エラー情報', description='',  timestamp=ctx.message.created_at, color=discord.Colour.red())
                e.add_field(name='エラーが発生したサーバー', value=ctx.message.guild.name, inline=False)
                e.add_field(name='エラーが発生したチャンネル', value=ctx.message.channel.name, inline=False)
                e.add_field(name='エラーid', value=ctx.message.id, inline=False)
                e.add_field(name='エラーが発生したコマンド', value=ctx.message.content, inline=False)
                e.add_field(name='エラーを発生させた人', value=ctx.author, inline=False)
                e.add_field(name='エラー内容', value=error, inline=False)
                await error_ch.send(embed=e)
            elif isinstance(error, discord.ext.commands.errors.BadArgument):
                embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数がエラーを起こしているため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
                embed.set_footer(text="お困りの場合はBot管理者までお問い合わせください")
                await ctx.send(embed=embed)
                e = discord.Embed(title='エラー情報', description='',  timestamp=ctx.message.created_at, color=discord.Colour.red())
                e.add_field(name='エラーが発生したサーバー', value=ctx.message.guild.name, inline=False)
                e.add_field(name='エラーが発生したチャンネル', value=ctx.message.channel.name, inline=False)
                e.add_field(name='エラーid', value=ctx.message.id, inline=False)
                e.add_field(name='エラーが発生したコマンド', value=ctx.message.content, inline=False)
                e.add_field(name='エラーを発生させた人', value=ctx.author, inline=False)
                e.add_field(name='エラー内容', value=error, inline=False)
                await error_ch.send(embed=e)
            elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
                embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数が足りないため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
                embed.set_footer(text="お困りの場合はBot管理者までお問い合わせください")
                await ctx.send(embed=embed)
                e = discord.Embed(title='エラー情報', description='',  timestamp=ctx.message.created_at, color=discord.Colour.red())
                e.add_field(name='エラーが発生したサーバー', value=ctx.message.guild.name, inline=False)
                e.add_field(name='エラーが発生したチャンネル', value=ctx.message.channel.name, inline=False)
                e.add_field(name='エラーid', value=ctx.message.id, inline=False)
                e.add_field(name='エラーが発生したコマンド', value=ctx.message.content, inline=False)
                e.add_field(name='エラーを発生させた人', value=ctx.author, inline=False)
                e.add_field(name='エラー内容', value=error, inline=False)
                await error_ch.send(embed=e)
            else:
                embed = discord.Embed(title=":x: 失敗", description=f'不明なエラーが発生しました', timestamp=ctx.message.created_at, color=discord.Colour.red())
                embed.add_field(name='お問い合わせの際', value=f'お問い合わせる際にはこちらのidもお持ちください。{ctx.message.id}')
                embed.set_footer(text="お困りの場合はBot管理者までお問い合わせください")
                await ctx.send(embed=embed)
                e = discord.Embed(title='エラー情報', description='',  timestamp=ctx.message.created_at, color=discord.Colour.red())
                e.add_field(name='エラーが発生したサーバー', value=ctx.message.guild.name, inline=False)
                e.add_field(name='エラーが発生したチャンネル', value=ctx.message.channel.name, inline=False)
                e.add_field(name='エラーid', value=ctx.message.id, inline=False)
                e.add_field(name='エラーが発生したコマンド', value=ctx.message.content, inline=False)
                e.add_field(name='エラーを発生させた人', value=ctx.author, inline=False)
                e.add_field(name='エラー内容', value=error, inline=False)
                await error_ch.send(embed=e)
                orig_error = getattr(error, "original", error)
                error_msg  = ''.join(traceback.TracebackException.from_exception(orig_error).format())
                await error_ch.send('エラー全文')
                await error_ch.send(error_msg)

async def setup(bot):
    await bot.add_cog(Public(bot))
    print('Public is Loaded')
