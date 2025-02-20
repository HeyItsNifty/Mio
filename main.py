import json
import discord
import random

from discord.ext import commands

f = open("Mios.json", "r")
settings = json.load(f)
f.close()

intents = discord.Intents.all()
Mio = commands.Bot(command_prefix = settings["prefix"], intents = intents)

@Mio.event
async def on_ready():
	print("[+] Mio is ready!")
	await Mio.change_presence(
		activity = discord.Activity(
			type = discord.ActivityType.watching,
			name = "over The Sleeping Fox Inn!"
		)
	)

@Mio.event
async def on_message(message):
	if message.author == Mio.user:
		return
	await Mio.process_commands(message)

@Mio.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		return
	raise error

@Mio.event
async def on_member_join(member: discord.Member):
	try:
		roles = []
		roles.append(discord.utils.get(member.guild.roles, name = "Wanderer"))
		roles.append(discord.utils.get(member.guild.roles, name = "Traveler"))
		roles.append(discord.utils.get(member.guild.roles, name = "Adventurer"))
		random.shuffle(roles)
		await member.add_roles(roles[0])
		roles.clear()
		await member.send(f"Welcome to The Sleeping Fox Inn, {member.mention}!")
	except Exception as e:
		print(e)
		print("[-] Could not add role to member!")

