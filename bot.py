import discord
from discord.ext import commands
from config import *


bot = commands.Bot(command_prefix='smfb', description=BOT_DESCRIPTION, intents=discord.Intents(message_content=True))

bot.run(TOKEN)
