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
from discord.ext import commands

#getting the prefix

with open("prefix.txt", "r") as rf:

  prefixfile = rf.read()

#variables
prefix = (prefixfile)
client = commands.Bot(command_prefix = "!!")
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
  
@client.command()
async def hello(ctx):
  await ctx.send("You just said hello to a bot. Get some friends.")

@client.command()
async def ping(ctx):
  await ctx.send(f"Ping pong your mother is gone! `{client.latency * 1000}ms`")

@client.command()
aysnc def clear(ctx, amount)

client.loop.create_task(update_stats())

run = True

if run == True:
  client.run("ODE0MTAyMDYxOTIyMTIzODM2.YDY9oA.rcel_4RUzVB5Kxa076ZYJmDPvDw")
