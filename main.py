import discord
from discord.ext import commands
from dotenv import load_dotenv

import os

load_dotenv('.env')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('Bot is Ready.')

@bot.event
async def on_message(message):
    # embed = discord.Embed(
    #     title=title,
    #     description=description,
    #     color=0xFF5733
    # )
    # await ctx.message.delete()
    # await ctx.send(embed=embed)
    content = message.content
    if content.startswith('embed:'):
        kwargs = {}
        args = content.split('\n')
        del args[0]
        for arg in args:
            args_list = arg.split(':')
            arg_name = args_list[0]
            if arg_name == 'color':
                continue
            
            arg_content = args_list[1]
            if arg_content.startswith(' '):
                arg_content = arg_content[1:]
            kwargs[arg_name] = arg_content

        embed = discord.Embed(
            **kwargs,
            color=0xFF5733
        )
        await message.delete()
        await message.channel.send(embed=embed)

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
