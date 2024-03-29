import discord
import api # from api.py
import setup # from setup.py

bot = discord.Client()

prefix = setup.prefix
token = setup.token

try:
    @bot.event
    async def on_ready():
        print('Bot is online as {0.user}'.format(bot))

except:
    print('Bot faild to go online!')
    # somthing went wrong
    # exampel: no internet

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(prefix + 'help'):
        # msg => is the message the bot gives

        msg = prefix + "help\n"
        msg += "Show a list of comands\n\n"

        msg += prefix + "search\n"
        msg += "Let you search for a game,"
        msg += "exampel: " + prefix + "search [the game] [console] "
        msg += "Note that it takes the last word as the console/platform)\n"

        await message.channel.send(msg)

    if message.content.startswith(prefix + 'search'):
        print(str(message.author) + ": " + str(message.content))

        user_msg = str(message.content).split(" ")
        # msg => is the message the bot gives

        try:
            try:
                msg = api.Games(user_msg[1], user_msg[2]).search()
            except:
                msg = api.Games(user_msg[1]).search()
        except:
            msg = "no input"
            # did not locate the game

        await message.channel.send(msg)

# trying the token
try:
    bot.run(token)
except:
    print("Token does not exist!")
    
# Test
