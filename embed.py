import datetime
from dis import disco
import random
from turtle import color
from unicodedata import name
import discord
from discord.ext import commands
from matplotlib.pyplot import text, title
import os


gender_embed = discord.Embed(title=f"Welcome!").set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
gender_embed.add_field(name="Choose a gender role", value=f"All roles come with their specific perks\
\nYou can only choose one role ", inline=True)
gender_embed.add_field(name="", value=f"👦- if u man\n 👧 -if u a woman")
gender_embed.set_footer(icon_url=f"{member.guild.icon_url}", text=f"-")