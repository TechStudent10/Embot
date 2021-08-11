import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv

import os
import traceback

load_dotenv('.env')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('Bot is Ready.')

@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title="So... You want to use embeds?", description=f"""
    Well you've come to the right bot!
    I am Embot and I allow your members to send embeds. Pretty simple, right?
    Just make sure to tell your members that in order to send an embed, they have to use something like this:
    
    ```
embed:
title: This is a title
description: This is a description
    ```
    You can find more info on my GitHub page: https://github.com/TechStudent11/Embot.
    Thanks for using Embot.
    """, color=0xFF5733)
    channel = discord.utils.get(guild.text_channels, name="general")
    await channel.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('```Command Not Found.```')
    else:
        try:
            raise error
        except commands.CommandInvokeError:
            await ctx.send(f'''An error occured in BOT code:
```python
{traceback.format_exc()}
```
            ''')
    print(error)

@bot.event
async def on_message(message):
    # embed = discord.Embed(
    #     title=title,
    #     description=description,
    #     color=0xFF5733
    # )
    # await ctx.message.delete()
    # await ctx.send(embed=embed)

    await bot.process_commands(message)

    content = message.content
    if content.startswith('embed:'):
        kwargs = {}
        color = 0xFF5733
        args = content.split('\n')
        del args[0]
        for arg in args:
            args_list = arg.split(':')
            arg_name = args_list[0]
            
            names_that_arent_allowed = ['url']
            if arg_name in names_that_arent_allowed:
                continue
            
            if arg_name == 'color' or arg_name == 'colour':
                if hasattr(discord.Colour, arg_name):
                    color = getattr(discord.Colour, arg_name)()

            del args_list[0]

            arg_content = ':'.join(args_list)
            if arg_content.startswith(' '):
                arg_content = arg_content[1:]

            kwargs[arg_name] = arg_content

        if 'color' in kwargs:
            del kwargs['color']
        
        if 'colour' in kwargs:
            del kwargs['colour']

        if 'description' not in kwargs:
            await message.channel.send(embed=discord.Embed(description='HEY! Description is rquired!'))
            return

        embed = discord.Embed(
            **kwargs,
            color=color
        )

        # await message.delete()
        await message.channel.send(embed=embed)

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
