import discord
from discord.ext import commands
import time


class Utility(commands.Cog):

    def __innit__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("'Utility' module has been loaded")
    

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)
        if amount == 1:
            await ctx.send(f"{amount} message was purged")
            time.sleep(1)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send(f"{amount} message(s) were purged")
            time.sleep(1)
            await ctx.channel.purge(limit=1)
    




        

def setup(client):
    client.add_cog(Utility(client))