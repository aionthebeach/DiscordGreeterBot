# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send((f"Welcome to AI on the Beach, {member.name}!\n"
                                "Can you tell us a little about yourself and how you found out about us? \n"))

    await member.create_dm()
    await member.dm_channel.send((
        f"Here's some more information to help you get started:\n"
        "Website: https://aionthebeach.com/ \n"
        "Github: https://bit.ly/aionthebeach-code \n"
        "Quilt: https://bit.ly/aionthebeach-data"
        ))

client.run(TOKEN)