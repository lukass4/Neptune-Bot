import os
import discord

client = discord.Client()

default_prefix = ("$")
prefix = (default_prefix)

@client.event
async def on_ready():
  print("Bot is online! ({0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(prefix + "hello"):
    await message.channel.send("You just said hello to a bot. Get some friends.")

client.run(os.getenv("TOKEN"))