import os
import discord
import time

client = discord.Client()

default_prefix = ("~")
prefix = (default_prefix)

@client.event
async def on_ready():
  print("Bot is online! {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(prefix + "hello"):
    await message.channel.send("You just said hello to a bot. Get some friends.")

  if message.content.startswith(prefix + "nuke"):
    await message.channel.send("**BOOM!**")
    time.sleep(2)
    await message.channel.send("__**The server has been deleted!**__")
    print("Someone tried to delete the server.")

  if message.content.startswith("@{0.user}".format(client)):
    await message.channel.send("Hi I am neptune bot. My prefix is `" + prefix + "`. Try `" + prefix + "help` to get started!")

client.run("ODE0MTAyMDYxOTIyMTIzODM2.YDY9oA.rcel_4RUzVB5Kxa076ZYJmDPvDw")