import discord
from discord.ext import commands
import time


class Utility(commands.Cog):

    def __innit__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("'Utility' module has been loaded")
    

    @commands.command(aliases=["purge", "delete", "del", "clean",])
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount+1)
        if amount == 1:
            await ctx.send(f"A message was removed")
            time.sleep(1)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send(f"Up to {amount} messages were removed")
            time.sleep(1)
            await ctx.channel.purge(limit=1)







        

def setup(client):
    client.add_cog(Utility(client))