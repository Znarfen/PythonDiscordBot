import discord
import api
import setup

Bot = discord.Client()

prefix = setup.prefix
token = setup.token

try:
    @Bot.event
    async def on_ready():
        print('Bot is logged in as {0.user}'.format(Bot))

except:
    print('Bot faild to login!')

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return

    if message.content.startswith(prefix + 'search'):
        print(str(message.author) + ": " + str(message.content))

        user_msg = str(message.content).split(" ") # msg => is the message the bot gives
        try:
            try:
                msg = api.Games(user_msg[1], user_msg[2]).search()
            except:
                msg = api.Games(user_msg[1]).search()
        except:
            msg = "no input"
            
        await message.channel.send(msg)

try:
    Bot.run(token)

except:
    print("Token does not exist!")
