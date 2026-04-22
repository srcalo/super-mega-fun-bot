import discord
from bot import bot
'''
	Commands
		/role-setup: Sends role selection message in channel its used in and begins (admin-only)
'''

'''
	Things happening
		Reaction add: Apply role associated with the reacted emoji to the correct user
		Reaction remove: Remove role associated with the reacted emoji to the correct user
'''

'''
	Notes
		Roles can be in groups
		Keep track of last time user applied specific role and role group
		Allow cooldown for each role and role group that prevents user from re-adding that role
'''


@bot.event
async def on_ready():
	print("Bot is online")

@bot.command(name='setup roles', description='Sets up role assignment message in channel')
async def SetupRoles(ctx):
	return





