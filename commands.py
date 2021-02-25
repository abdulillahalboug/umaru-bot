import discord
import random

known_users = ["snoopy#4548", "Shirito#0999", "𝓜𝓲𝓶𝓲#2001"]

client = discord.Client()

#bot log in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#message command
@client.event
async def on_message(message):
    message.content = message.content.lower()

    if not message.author.bot and message.content.startswith(PREFIX):
      content = message.content[PREFIX.length]

      if content.startswith('hello') or message.content.startswith('hi'):
         if str(message.author) in known_users:
           box1 = await random_message()
           await message.reply(box1)
         else:
           box = await random_message1()
           await message.reply(box)

      if content.startswith('u!what do you want too eat'):
        await message.channel.send(" eat pizza and drink cola!")

      if content.startswith('are you hungry'):
        await message.channel.send("yess! always hungry")



#list1
async def random_message():
    ind = random.randint(0,7)

    list1 = ["Hello master", "hey", "Hey senpai", "Hi snoopy", "Hey is it u !!!!!!", "Hey why are u amazing", "Hey me me hungry!!", " Hey UwU"]

    choose = list1[ind]
    return choose


#list2
async def random_message1():
    ind1 = random.randint(0, 9)

    list2 = ["and who are you", "dont talk to me human ", "shut up", "hey now fooood!!!!!! ", "who u dont talk to me", "hey shhh tim tired", "u not my parent dont need to answer you","pfft","hi do you have cola and chips","hey"]

    choose1 = list2[ind1]
    return choose1

client.run ("ODA0MDY4OTc3MTgxNDU4NDQy.YBG9lw.j66e7eH8qsLO6pMSpcS9LDs7f6k")
