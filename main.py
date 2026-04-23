import data
import discord.ext.commands
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
channels: dict[int, list[int]] = {}

@bot.event
async def on_ready():
	print("Bot is online")

@bot.command(name='setup roles', description='Sets up role assignment message in channel')
async def SetupRoles(ctx: discord.ext.commands.Context):
	# save channel command was called in
	channels[ctx.channel.id] = []
	await ctx.send('React with an emoji below to receive your desired role. Remove your reaction to remove the role!') # Send instructions

	roleGroups = data.GetRoles() 
	
	# For each group, build and send the related message
	for (groupName, roles) in roleGroups.items():
		# Build message
		msgText = f'**{groupName}**'
		for role in roles:
			msgText += f'\n{role.Emoji} {role.Name}: {role.Description}'
		
		# Send message
		msg = await ctx.send(msgText)

		# Save message id for tracking
		channels[ctx.channel.id].append(msg.id) 

		# Add reactions to message
		for role in roles:
			await ctx.message.add_reaction(role.Emoji)

@bot.event
async def on_reaction_add(reaction, user):
	return

@bot.event
async def on_reaction_remove(reaction, user):
	return

