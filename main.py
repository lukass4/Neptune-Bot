#Command template
#  if message.content.startswith(prefix + "command"):
#   await message.channel.send("message")
import os
import discord
import time
import random

client = discord.Client()

default_prefix = ("~")
prefix = (default_prefix)

@client.event
async def on_ready():
  print("Bot is online! {0.user}".format(client))



@client.event
async def on_message(message):
  server = client.get_guild(813415238493405246)
  if message.author == client.user:
    return

  if message.content.startswith(prefix + "hello"):
    await message.channel.send("You just said hello to a bot. Get some friends.")

  if message.content.startswith(prefix + "subscribe"):
    await message.channel.send("Go subscribe to our YT channel! https://www.youtube.com/channel/UCClRI1bqkIsYfWQGebcV4cg?guided_help_flow=5")

  if message.content.startswith(prefix + "youtube"):
    await message.channel.send("Go subscribe to our YT channel! https://www.youtube.com/channel/UCClRI1bqkIsYfWQGebcV4cg?guided_help_flow=5")

  if message.content.startswith(prefix + "YT"):
    await message.channel.send("Go subscribe to our YT channel! https://www.youtube.com/channel/UCClRI1bqkIsYfWQGebcV4cg?guided_help_flow=5")

  if message.content.startswith(prefix + "nuke"):
    await message.channel.send("**BOOM!**")
    time.sleep(2)
    await message.channel.send("__**The server has been deleted!**__")
    print("Someone tried to delete the server.")

  if message.content.startswith(prefix + "help"):
    await message.channel.send("Hi I am neptune bot. My prefix is `" + prefix + "`. Try `" + prefix + "commands` to get started!")

  if message.content.startswith(prefix + "whoami"):
    await message.channel.send(message.author)

  if message.content.startswith(prefix + "members"):
    await message.channel.send(f"""This server has `{server.member_count}` members!""")






client.run("ODE0MTAyMDYxOTIyMTIzODM2.YDY9oA.rcel_4RUzVB5Kxa076ZYJmDPvDw")