#Command template
#  if message.content.startswith(prefix + "command"):
#   await message.channel.send("message")

#imports

import os
import discord
import time
import random

#variables

client = discord.Client()
default_prefix = ("!!")
prefix = (default_prefix)
server = client.get_guild(813415238493405246)

#started up message

@client.event
async def on_ready():
  print("Bot is online! {0.user}".format(client))

#welcome message

@client.event
async def on_member_join(member):
  for channel in member.server.channels:
    if str(channel) == "welcomes-and-goodbyes":
      await client.send_message(f"""Hi, welcome to the server {member.mention} you are member number {server.member_count}!  """)

@client.event
async def on_message(message):
  server = client.get_guild(813415238493405246)
  if message.author == client.user:
    return

#Commands anyone can use
  
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

  if message.content.startswith(prefix + "commands"):
      await message.channel.send(f"""My commands are:
`{prefix}subscribe` Gives you our youtube channel link
`{prefix}members` Says how many members the server has
`{prefix}whoami` Gives you some info about... YOU!
`{prefix}nuke` Blows up the server
`{prefix}info` Shows info on the server""")


  if message.content.startswith(prefix + "whoami"):
    await message.channel.send(message.author)

  if message.content.startswith(prefix + "members"):
    await message.channel.send(f"""This server has `{server.member_count}` members!""")

  if message.content.startswith(prefix + "info"):
    await message.channel.send(f"""Hi, this is The Noob Clan this is a Discord server about a youtube channel that LJ and DyNoob own. If you want the channel link you run the command `{prefix}subscribe`!""")


#staff commands






client.run("ODE0MTAyMDYxOTIyMTIzODM2.YDY9oA.rcel_4RUzVB5Kxa076ZYJmDPvDw")