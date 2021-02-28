import discord
from discord.ext import commands

class Fun(commands.Cog):

    def __innit__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("'Fun' module has been loaded")

    @commands.command()
    async def deeznuts(self, ctx):
        await ctx.send("https://cdn.slangit.com/img/slang/deez_nuts_4727.jpg")
        
    @commands.command()
    async def ily(self, ctx, member : discord.Member):
        await ctx.send(f"I love you {member.mention}! Do you love me?")

    @commands.command()
    async def f(self, ctx,):
        await ctx.send("idek what just happened but big **f**")

def setup(client):
    client.add_cog(Fun(client))