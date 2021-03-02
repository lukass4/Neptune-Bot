import discord
from discord.ext import commands
import os
import random
import time
from discord.ext import tasks
import json
import asyncio

with open("prefix.txt", "r") as f:
    prefix = f.read()

client = commands.Bot(command_prefix = prefix)
bot = discord.Client()
statuses = ["Deez nuts", "I am neptune", "Don't ask questions", f"{prefix}help", "Mee6 more like Mee69", "I am king of all bots!", "Neptune > Jupiter", "Made by LJ_gaming#1224"]


@client.event
async def on_ready():
    print("Bot is online! {0.user}".format(client))
    logs_channel = client.get_channel(813768338404278332)
    await logs_channel.send("The bot is online!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(random.choice(statuses)))
    with open("online_offline_logs.txt", "a")as f:
        f.write("The bot is now online!\n")

@client.command()
async def enable(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"The '{extension}' module was enabled.")

@enable.error
async def enable_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please specify the module you would like to enable. Do {prefix}modules to see a list of all modules.")

@client.command()
async def disable(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"The '{extension}' module has been disabled.")

@disable.error
async def disable_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please specify the module you would like to disable. Do `{prefix}modules` to see a list of all modules.")

@client.command()
async def ping(self, ctx):
    await ctx.send(f"Ping pong your mother is gone! `{round(client.latency * 1000)}ms`")


@client.command()
async def modules(ctx):
    await ctx.send(f"""Here is a list of all modules.\n`fun`: Some fun commands\n`utility`: Some useful commands such as `{prefix}ping`\n*To enable or disable any of these modules do {prefix}enable/disbale <module name>*""")

@tasks.loop(minutes=15)
async def update_status():
    statuses = ["Deez nuts", "I am neptune", "Don't ask questions", f"{prefix}help", "Mee6 more like Mee69", "I am king of all bots!", "Neptune > Jupiter", "Made by LJ_gaming#1224"]
    await client.change_presence(status=discord.Status.online, activity=discord.Game(random.choice(statuses)))

@update_status.before_loop
async def before_some_task():
  await client.wait_until_ready()

@client.command()
@commands.has_permissions(administrator = True)
async def restart(ctx):
    update_status.stop()
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Resarting..."))
    await client.close()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"That is not a valid command. Use {prefix}help to see a list of commands!")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

update_status.start()
client.run("ODE0MTAyMDYxOTIyMTIzODM2.YDY9oA.rcel_4RUzVB5Kxa076ZYJmDPvDw")

