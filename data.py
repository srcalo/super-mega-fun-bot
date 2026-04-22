from dataclasses import dataclass
from enum import Enum

@dataclass
class Role:
	Id: str
	Name: str
	Description: str
	Emoji: str
	Cooldown: int = 0

@dataclass
class RoleGroup:
	Name: str
	Rule: RoleGroupRule

class RoleGroupRule(Enum):
	NAN = 1
	XOR = 2

'''Returns dictionary with group names mapped to list of roles'''
def GetRoles():
	return {
		"General": [
			Role(
				Id="1479122344755724319",
				Name="Albanians",
				Description="If you live in Albany and would like to get @ed for Albany things.",
				Emoji="🌷"
			),
			Role(
				Id="1486557846102605834",
				Name="Grippers",
				Description="If you would like to recieve @s about climbing.",
				Emoji="🦶"
			),
			Role(
				Id="1477768593973186703",
				Name="purble",
				Description="If you would like to turn purple",
				Emoji="🍆"
			),
			Role(
				Id="1487342354217173013",
				Name="cat rot",
				Description="If you've been infected by the cat bot",
				Emoji="🙀"
			)
		],
		"Cat Bot": [
			Role(
				Id="1496296668952526888",
				Name="cats-1",
				Description="Grants access to <#1477485461537558641>.",
				Emoji="😸"
			),
			Role(
				Id="1496296835147370716",
				Name="cats-2",
				Description="Grants access to <#1496295851746660382>.",
				Emoji="😼"
			)
		]
	}

def GetGroups():
	return [
		RoleGroup(
			Name="General",
			Rule=RoleGroupRule.NAN
		),
		RoleGroup(
			Name="Cat Bot",
			Rule=RoleGroupRule.XOR
		)
	]

# Schema
# Role
#	Id
# 	Name
#	Description
#	Emoji
#	Cooldown (in minutes)

# RoleGroup
# 	Id
#	Name
#	Description
#	Cooldown (in minutes)

# RoleGroupUnion
# 	GroupId
# 	RoleId
