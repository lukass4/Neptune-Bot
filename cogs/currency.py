from collections import UserList
import discord
from discord import embeds
from discord import flags
from discord import user
from discord.ext import commands
import json

class Currency(commands.Cog):


    def __innit__(self, client):
        self.client = client

    with open("prefix.txt", "r")as f:
        prefix = f.read()
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("\"Currency\" module has been loaded")

    @commands.command(aliases=["bal", "coins", "coin"])
    async def balance(self, ctx, user: discord.Member = None):
        data = json.load(open("coins.json", "r"))
        if not user:
            try:
                userBal = data[f"{ctx.author.id}"][0]
            except KeyError:
                data[f"{ctx.author.id}"] = [[]]
                data[f"{ctx.author.id}"][0] = 0

                userBal = data[f"{ctx.author.id}"][0]

            await ctx.send(f"You have **{userBal}** <:black_gem:808326519961288755>.")

            json.dump(data, open("coins.json", "w"))
        else:
            try:
                userBal = data[f"{user.id}"][0]
            except KeyError:
                data[f"{user.id}"] = [[]]
                data[f"{user.id}"][0] = 0

                userBal = data[f"{user.id}"][0]

            await ctx.send(f"`{user.display_name}` has **{userBal}** <:black_gem:808326519961288755>.")

            json.dump(data, open("coins.json", "w"))

    @commands.command(aliases=["givecoins", "addmoney"])
    @commands.has_permissions(administrator=True)
    async def give(self, ctx, user: discord.Member, amount):
        data = json.load(open("coins.json", "r"))
        try:
            data[f"{user.id}"][0] += int(amount)
        except KeyError:
            data[f"{user.id}"] = [[]]
            data[f"{user.id}"][0] = int(amount)

        json.dump(data, open("coins.json", "w"))

        await ctx.send(f"`{amount}` <:black_gem:808326519961288755> were given to `{user.display_name}`.")

    @commands.command(aliases=["store", "market"])
    async def shop(self, ctx):
        embed = discord.Embed(title="Neptune Store", description ="", color=discord.Color.purple())
        embed.add_field(name="VIP role for 1 week: **250 <:black_gem:808326519961288755>**", value="ID: `vip`", inline=False)
        embed.add_field(name="+1 level on arcane: **500 <:black_gem:808326519961288755>**", value="ID: `level`", inline=False)
        embed.add_field(name="LJ will friend you on namemc.com: **750 <:black_gem:808326519961288755>**", value="ID: `namemc`", inline=False)
        embed.add_field(name="Add an emoji to the server: **1,000 <:black_gem:808326519961288755>**", value="ID: `emoji`", inline=False)
        embed.add_field(name="Pixel Art Profile picture: **1,500 <:black_gem:808326519961288755>**", value="ID: `pfp`", inline=False)
        embed.add_field(name="1 million dank memer coins: **7,500 <:black_gem:808326519961288755>**", value="ID: `coins`", inline=False)
        embed.set_footer(text="Do `!!buy <id>` to request/purchase an item!")
        await ctx.send(embed=embed)

    @commands.command(aliases=["request", "purchase"])
    async def buy(self, ctx, item = None):
        data = json.load(open("coins.json", "r"))

        if item == "vip":
            try: # see if they have any money at all
                userBal = data[f"{ctx.author.id}"][0]
                if userBal >= 250: # see if they have enough money

                    vip = ctx.guild.get_role(802108600297979924)
                    if vip in ctx.author.roles: # check if they have vip already
                        await ctx.send("You already have this role.")
                    else: # if they dont already have vip
                        await ctx.author.add_roles(vip) # give them vip

                        await ctx.send("Congrats on `VIP role`!")

                        userBal = userBal - 250 # calc new balance
                        data[f"{ctx.author.id}"][0] = userBal # setting new balance

                        json.dump(data, open("coins.json", "w")) # dumping json
                else: # if they dont have enough money
                    await ctx.send("You do not have enough gems.")
            except KeyError: # if they dont have any money at all
                await ctx.send("You do not have enough gems.")

        elif item == "level":
            try: # see if they have any money
                userBal = data[f"{ctx.author.id}"][0]
                if userBal >= 500: # see if they have enough money

                    channel = ctx.bot.get_channel(846829141097578587)
                    await channel.send(f"{ctx.author.mention} requested `+1 level on arcane` ||<@562711070242766850>||") # send message in #requests
                    
                    await ctx.send("A message has been sent to the admins. You should recive your `+1 level on arcane` soon!")

                    userBal = userBal - 500 # calc new balance
                    data[f"{ctx.author.id}"][0] = userBal # setting new balance

                    json.dump(data, open("coins.json", "w"))

                else: # if they dont have enough money
                    await ctx.send("You do not have enough gems.")
            except KeyError: # if they dont have any money at all
                await ctx.send("You do not have enough gems.")

        elif item == "namemc":
            try: # see if they have any money
                userBal = data[f"{ctx.author.id}"][0]
                if userBal >= 750: # see if they have enough money

                    channel = ctx.bot.get_channel(846829141097578587)
                    await channel.send(f"{ctx.author.mention} requested `a friend add on namemc` ||<@562711070242766850>||") # send message in #requests
                    
                    await ctx.send("Create an 'other' ticket (<#819202472920219768>) and ping LJ with your minecraft name. He will respond after he has added you!")

                    userBal = userBal - 750 # calc new balance
                    data[f"{ctx.author.id}"][0] = userBal # setting new balance

                    json.dump(data, open("coins.json", "w"))

                else: # if they dont have enough money
                    await ctx.send("You do not have enough gems.")
            except KeyError: # if they dont have any money at all
                await ctx.send("You do not have enough gems.")
        
        elif item == "emoji":
            try: # see if they have any money
                userBal = data[f"{ctx.author.id}"][0]
                if userBal >= 1000: # see if they have enough money

                    channel = ctx.bot.get_channel(846829141097578587)
                    await channel.send(f"{ctx.author.mention} requested `to add an emoji to the server` ||<@562711070242766850>||") # send message in #requests
                    
                    await ctx.send("A message has been sent to the admins. Please DM LJ with your image. \nIf the emoji does not follow the rules, you will be asked for a different one or recive a refund.")

                    userBal = userBal - 1000 # calc new balance
                    data[f"{ctx.author.id}"][0] = userBal # setting new balance

                    json.dump(data, open("coins.json", "w"))

                else: # if they dont have enough money
                    await ctx.send("You do not have enough gems.")
            except KeyError: # if they dont have any money at all
                await ctx.send("You do not have enough gems.")
        
        elif item == "pfp":
            try: # see if they have any money
                userBal = data[f"{ctx.author.id}"][0]
                if userBal >= 1500: # see if they have enough money

                    channel = ctx.bot.get_channel(846829141097578587)
                    await channel.send(f"{ctx.author.mention} requested `a pixel art profile picture` ||<@562711070242766850>||") # send message in #requests
                    
                    await ctx.send("A message has been sent to the admins. LJ will make a ticket and invite you. Then he will make your custom profile!")

                    userBal = userBal - 1500 # calc new balance
                    data[f"{ctx.author.id}"][0] = userBal # setting new balance

                    json.dump(data, open("coins.json", "w"))

                else: # if they dont have enough money
                    await ctx.send("You do not have enough gems.")
            except KeyError: # if they dont have any money at all
                await ctx.send("You do not have enough gems.")    

        elif item == "coins":
            try: # see if they have any money
                userBal = data[f"{ctx.author.id}"][0]
                if userBal >= 7500: # see if they have enough money

                    channel = ctx.bot.get_channel(846829141097578587)
                    await channel.send(f"{ctx.author.mention} requested `1 mill dank memer coins` ||<@562711070242766850>||") # send message in #requests
                    
                    await ctx.send("A message has been sent to the admins. You should get your dank memer coins soon.")

                    userBal = userBal - 7500 # calc new balance
                    data[f"{ctx.author.id}"][0] = userBal # setting new balance

                    json.dump(data, open("coins.json", "w"))

                else: # if they dont have enough money
                    await ctx.send("You do not have enough gems.")
            except KeyError: # if they dont have any money at all
                await ctx.send("You do not have enough gems.")    

        else:
            await ctx.send("That is not a valid ID.")


def setup(client):
    client.add_cog(Currency(client))