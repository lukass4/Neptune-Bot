#Command template
#  if message.content.startswith(prefix + "command"):
#   await message.channel.send("message")

#imports

import os
import discord
import time
import random
import time
import asyncio

#getting the prefix

with open("prefix.txt", "r") as rf:

  prefixfile = rf.read()

#variables

client = discord.Client()
default_prefix = ("!!")
prefix = (prefixfile)
server = client.get_guild(813415238493405246)
messages = 0
joined = 0
logs_channel = client.get_channel(813768338404278332)
toolbox = False

#started up message

@client.event
async def on_ready():
  print("Bot is online! {0.user}".format(client))
  logs_channel = client.get_channel(813768338404278332)
  await logs_channel.send("The bot is online!")
  with open("online_offline_logs.txt", "a")as f:
    f.write("The bot is now online!\n")



#Message and member join log script

async def update_stats():
  await client.wait_until_ready()
  global messages, joined

  while not client.is_closed():
    try:
        with open ("stats.txt", "a") as f:
          f.write(f"""Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n""")
        logs_channel = client.get_channel(813768338404278332)
        await logs_channel.send(f"""Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n""")
        messages = 0
        joined = 0
        await asyncio.sleep(60)
    except Exception as e:
      print(e)
      await asyncio.sleep(60)



#nickname

@client.event
async def on_member_update(before, after): 
  print("")




#commands amd 'bad words'

@client.event
async def on_message(message):
  global messages
  messages += 1
  server = client.get_guild(813415238493405246)
  if message.author == client.user:
    return

  bad_words = ["Dynoob", "ded"]
  staff_ping = ["<@&813415785690955818>", "<@&813415755093377094>", "<@&813770998498983956>", "<@&813415769903464459>", "<@&813770937220333578>", "<@&814147036872966144>", "<@&813768249023528991>", "<@&813415785690955818>", "<@&813770900250951721>", ]

  for word in bad_words:
    if message.content.count(word)> 0:
      print(f"""{message.author} send a bad word in #{message.channel}. The message was '{message.content}'""")
      await message.channel.purge(limit=1)
      await message.channel.send("Dont say that word :angry:")
      logs_channel = client.get_channel(813768338404278332)
      await logs_channel.send(f"""{message.author} send a bad word in #{message.channel}. The message was '{message.content}'""")

  for word in staff_ping:
    if message.content.count(word)> 0:
      print(f"""{message.author}({message.author.id}) send a pinged staff in #{message.channel}. The message was '{message.content}'""")
      await message.channel.send("NOTE: Make sure to only ping staff when necessary!")
      logs_channel = client.get_channel(813768338404278332)
      await logs_channel.send(f"""{message.author} send a pinged staff in #{message.channel}. The message was '{message.content}'""")

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

  if message.content.startswith(prefix + "whoami"):
    await message.channel.send(message.author)

  if message.content.startswith(prefix + "members"):
    await message.channel.send(f"""This server has `{server.member_count}` members!""")

  if message.content.startswith(prefix + "info"):
    await message.channel.send(f"""Hi, this is The Noob Clan this is a Discord server about a youtube channel that LJ and DyNoob own. If you want the channel link you run the command `{prefix}subscribe`!""")

  if message.content.startswith(prefix + "restart"):
    await message.channel.purge(limit=1)
    await message.channel.send("<@562711070242766850> someone shut the bot down.")
    time.sleep(1)
    with open("online_offline_logs.txt", "a")as f:
      f.write(f"""{message.author} shut down the bot.\n""")
    logs_channel = client.get_channel(813768338404278332)
    await logs_channel.send(f"{message.author} shutdown the bot.")
    await client.close()

  if message.content.startswith(prefix + "purge"):
    global toolbox
    if toolbox == True:
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=125)
      await message.channel.purge(limit=1)
      await message.channel.send("1875 messages purged!")
      logs_channel = client.get_channel(813768338404278332)
      await logs_channel.send(f"#{message.channel} was purged by {message.author}. A maximum of 1875 messages were purged as the toolbox was enabled.")
    if toolbox == False:
      await message.channel.purge(limit=51)
      await message.channel.send("50 messages purged!")
      logs_channel = client.get_channel(813768338404278332)
      await logs_channel.send(f"#{message.channel} was purged by {message.author}. A maximum of 50 messages were purged as the toolbox was disabled.")



  if message.content.startswith(prefix + "toolbox"):
    if toolbox == False:
      toolbox = True
      await message.channel.send("Toolbox enabled!")
      logs_channel = client.get_channel(813768338404278332)
      await logs_channel.send(f"""{message.author} enabled the toolbox.""")
    else:
      toolbox = False
      await message.channel.send("Toolbox disabled!")
      logs_channel = client.get_channel(813768338404278332)
      await logs_channel.send(f"""{message.author} disabled the toolbox.""")



#staff commands

  #if message.



client.loop.create_task(update_stats())
client.run("ODE0MTAyMDYxOTIyMTIzODM2.YDY9oA.rcel_4RUzVB5Kxa076ZYJmDPvDw")