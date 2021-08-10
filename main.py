import discord
from discord.ext import commands
from dotenv import load_dotenv

import os

load_dotenv('.env')

# def read_file(filename):
#     with open(filename, 'r') as f:
#         return f.read()

# def get_token():
#     return read_file('token.txt')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('Bot is Ready.')

@bot.command()
async def embed(ctx, title="Sample Title", description="Sample Description"):
    embed = discord.Embed(
        title=title,
        description=description,
        color=0xFF5733
    )
    await ctx.message.delete()
    await ctx.send(embed=embed)

bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
