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





client.run()
