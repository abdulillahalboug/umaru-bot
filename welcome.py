import discord

from discord.ext import commands

TOKEN = "ODA0MDY4OTc3MTgxNDU4NDQy.YBG9lw.j66e7eH8qsLO6pMSpcS9LDs7f6k"
PREFIX = "!"

intents = discord.Intents().default()
intents.members = True # Enable the member Privileged Intent

# Add the intents to the bot object
client = commands.Bot(command_prefix = PREFIX, case_insensitive = True, intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):

   await client.get_channel(768450587909554219).send(f"{member.mention} has joined")

client.run ("ODA0MDY4OTc3MTgxNDU4NDQy.YBG9lw.j66e7eH8qsLO6pMSpcS9LDs7f6k")
