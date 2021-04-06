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



@client.event
async def on_ready():
    print("Bot is online! {0.user}".format(client))
    logs_channel = client.get_channel(813768338404278332)
    await logs_channel.send("The bot is online!")
    with open("online_offline_logs.txt", "a")as f:
        f.write("The bot is now online!\n")
    with open("status.txt", "r") as f:
        current_status = f.read()
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=current_status))

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

async def disable_help():
    client.remove_command("help")

@client.command()
async def modules(ctx):
    await ctx.send(f"""Here is a list of all modules.\n`fun`: Some fun commands\n`utility`: Some useful commands such as `{prefix}ping`\n*To enable or disable any of these modules do {prefix}enable/disbale <module name>*""")

def is_bot_admin(ctx):
    if ctx.author.id == 562711070242766850 or ctx.author.id == 753552148167524422 or ctx.author.id == 705712254305173586:
        return


@client.command()
@commands.check(is_bot_admin)
async def restart(ctx):
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Resarting..."))
    await client.close()

@client.command(aliases=["slowmode", "delay"])
@commands.has_permissions(manage_messages = True)
async def sm(ctx, seconds : int=0):
    if seconds == 0:
        await ctx.channel.edit(slowmode_delay=0)
        await ctx.send(f"{ctx.author.mention} disabled slowmode.")
    else:
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Slowmode set to `{seconds}` by {ctx.author.mention}")



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"That is not a valid command. Use {prefix}help to see a list of commands!")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run("ODE0MTAyMDYxOTIyMTIzODM2.YDY9oA.rcel_4RUzVB5Kxa076ZYJmDPvDw")

