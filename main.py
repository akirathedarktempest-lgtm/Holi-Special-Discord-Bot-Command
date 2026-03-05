import discord
from discord.ext import commands
import asyncio
import random

intents=discord.Intents.all()
bot=commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print("The bot is ready!!!")
    await bot.tree.sync()

colo=["Red","Green","Blue"]

@bot.command()
async def attack(ctx, member:discord.Member, color:str|None=None):
    if color is not None:
        color=color.lower()
        if color=="green":
            role=discord.utils.get(member.guild.roles, name="Green")
            await member.add_roles(role)
            await ctx.send(f"Colored {member} with Green")
            await asyncio.sleep(5)
            await member.remove_roles(role)
        elif color=="blue":
            role=discord.utils.get(member.guild.roles, name="Blue")
            await member.add_roles(role)
            await ctx.send(f"Colored {member} with Blue")
            await asyncio.sleep(5)
            await member.remove_roles(role)
        elif color=="red":
            role=discord.utils.get(member.guild.roles, name="Red")
            await member.add_roles(role)
            await ctx.send(f"Colored {member} with Red")
            await asyncio.sleep(5)
            await member.remove_roles(role)
        else:
            await ctx.send("Wrong color")
    elif color is None:
        col=random.choice(colo)
        role=discord.utils.get(member.guild.roles, name=col)
        await member.add_roles(role)
        await ctx.send(f"Colored {member} with {col}")
        await asyncio.sleep(5)
        await member.remove_roles(role)
    else:
        await ctx.send("Wrong command!") 

bot.run("YOUR_TOKEN")
