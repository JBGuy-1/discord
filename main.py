import datetime
from dis import disco
import random
from turtle import color
from unicodedata import name
import discord
from discord.ext import commands
from matplotlib.pyplot import text, title
import os


prefix= "-"
intents= discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"The {bot.user} bot is online!")

# @bot.command()
# async def hi(ctx):
#     await ctx.send("heya, its the hangar bot!")

# @bot.command()
# async def embed(ctx):
#     my_fav_color = discord.colour.Color.from_rgb(123,109,114)
#     myembed = discord.Embed(title="embed title", color=my_fav_color).set_author(name="hangar bot")
#     myembed.a@bot.eventdd_field(name = "feild1", value = "this is line 1")
#     await ctx.send(embed= myembed)
@bot.event
async def on_member_join(member):
    colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
    # Welcome message channel id
    wlc_channel = bot.get_channel(953593435695251506)
    
    # Role we want to add automatically
    wlc_role = "OG"
    role = discord.utils.get(member.guild.roles, name=wlc_role)
    await member.add_roles(role)

   
    embed = discord.Embed(title=f"Welcome {member.name}!", color = random.choice(colors)).set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.add_field(name="Thank you for joining the server!", value=f"You gotta check <#953710369996685342> to verify your acc before getting full access to the server\
    \nCan't wait to meet you in <#953583957579026444> ", inline=True)
    embed.set_footer(icon_url=f"{member.guild.icon_url}", text=f"You are member number {member.guild.member_count}!")
    await wlc_channel.send(embed=embed)
    # msg = await wlc_channel.send(f"{member.mention}")
    
@bot.event
async def on_raw_reaction_add(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)

    if payload.emoji.name == "😎" and payload.message_id == 964930101290610778 :
        role = discord.utils.get(guild.roles, name="homies")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
# Remove roles
@bot.event
async def on_raw_reaction_remove(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)

    if payload.emoji.name == "😎" and payload.message_id == 964930101290610778:
        role = discord.utils.get(guild.roles, name="homies")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)

@bot.command()
async def verify(ctx):
    verify_embed = discord.Embed(title="Welcome to the hangar!").set_author(name="")
    verify_embed.add_field(name="let's get you started", value=f"Click the 😎 emoji to get full access to this server ")
    verify_embed.set_footer(text=f"")

    react_messasge = await ctx.send(embed=verify_embed)
    await react_messasge.add_reaction(emoji="😎")


bot.run(os.getenv('token'))

#verify 953710369996685342
#main chat 953583957579026444 