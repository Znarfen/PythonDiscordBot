import discord
import api

Bot = discord.Client()

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

    if message.content.startswith('>>search'):
        print(str(message.author) + ": " + str(message.content))

        msg = str(message.content).split(" ")
        try:
            try:
                msg = api.Games(msg[1], msg[2]).search()
            except:
                msg = api.Games(msg[1]).search()
        except:
            msg = "no input"
            
        await message.channel.send(msg)
        
Bot.run('dc_token')
