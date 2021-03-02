import discord
from discord.ext import commands
import random

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
    
    @commands.command()
    async def neverhaveiever(self, ctx,):
        with open("neverhaveiever.txt", "r")as f:
            questions = f.readlines()
        await ctx.send(f"Never have I ever {questions[random.randint(0, 12)]}")

    @commands.command()
    async def truthordare(self, ctx, member : discord.Member):
        await ctx.send(f"{member} truth or dare.\n {ctx.authour.mention} will ask you a question/give you a dare when you choose truth or dare.")  

def setup(client):
    client.add_cog(Fun(client))