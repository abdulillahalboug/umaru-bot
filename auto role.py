import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#katarinas log in
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


#message command
@client.event



async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id= 768451451348975627)
    await member.add_roles(role)





client.run('ODA0MDY4OTc3MTgxNDU4NDQy.YBG9lw.j66e7eH8qsLO6pMSpcS9LDs7f6k')
