import discord
import random
client = discord.Client()
#bot log in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#message command
@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:

        return

    if message.content.startswith('u!hello') or message.content.startswith('u!hi'):
        if str(message.author) == "snoopy#4548":
            box1 = await random_message()
            await message.channel.send(box1)
        else:
            box = await random_message1()
            await message.channel.send(box)

    if message.content.startswith('!ping'):
        await message.channel.send("pong!")

#list1
async def random_message():
    ind = random.randint(0,5)

    list1 = ["hello master snoopy","hey snoopy","hey senpai","hi snoopy","hey is it snoop!!!!!!","hey why are u amazing snoopy"]

    choose = list1[ind]
    return choose


#list2
async def random_message1():
    ind1 = random.randint(0, 9)

    list2 = ["and who are you", "dont talk to me human ", "shut up", "hey now fooood!!!!!! ", "who u dont talk to me", "hey shhh tim tired", "u not my parent dont need to answer you","pfft","hi do you have cola and chips","hey"]

    choose1 = list2[ind1]
    return choose1

client.run ("ODA0MDY4OTc3MTgxNDU4NDQy.YBG9lw.j66e7eH8qsLO6pMSpcS9LDs7f6k")