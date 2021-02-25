import discord


client = discord.Client()

#katarinas log in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#message command
@client.event
async def on_message(message):

    message.content = message.content.lower()

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):

        if str(message.author) == "snoopy#4548":
            await message.channel.send("Hello " + "snoopy" + "!")
        else:
            await message.channel.send("hello there")


    if message.content.startswith('!ping'):

        await message.channel.send("pong!")


    if message.content.startswith("!whos"):
        if str(message.author) == "snoopy#4548":
            await message.channel.send ("ofc you are" +"snoopy!")
        else:
            await message.channel.send("its master snoopy u idiot")






#delete message in pic channel
    if str(message.channel) == "pics" and message.content != "":
        await message.channel.purge(limit=1)





@client.event
async def on_member_join(member):
    name = member.mention
    channel = client.get_channel('768450587909554219')

    await channel.send(f"Welcome, {name}.")



client.run('ODA0MDY1NjU0MjE5MDc5NzEw.YBG6fg.nexzZkfBSqTqvdxVrWGosesquSM')
