import discord
from discord.ext import commands
from config import *


bot = commands.Bot(command_prefix='smfb', descsription=BOT_DESCRIPTION, intents=discord.Intents.default())

bot.run(TOKEN)
