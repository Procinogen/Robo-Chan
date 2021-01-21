import discord
from discord.ext.commands import Bot
import asyncio

my_bot = Bot(command_prefix="Robochan! ")
client = discord.Client()

@client.event
async def on_message():
	print("foo")

@my_bot.event
async def on_read():
    print("Client logged in")

"""Test Commands"""
@my_bot.command()
async def Hello():
    return await my_bot.say("Hello, world!")

@my_bot.command()
async def Ping():
	return await my_bot.say("Pong!")

@my_bot.command()
async def QuoteMe():
	return await my_bot.say("I can't do that yet. :/")
	
"""I am lonely command"""
@my_bot.group()
async def I():
	return

@I.command()
async def am(str):
	import time
	if str == "lonely":
		await my_bot.say("Get a life, my man.")
	if str == "hungry":
		await my_bot.say("Then go get some food.")
		time.sleep(2)
		await my_bot.say("Fatty.")
	if str == "bored":
		await my_bot.say("So am I.")
		time.sleep(1)
		await my_bot.say("Wanna chat for a bit?")
	return


my_bot.run("[token here]")

