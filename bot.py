import discord


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

    if message.content.startswith(''):
        print(str(message.author) + ": " + str(message.content))
        for i in range(len(str(message.content) * 30)):
            print(i +1)
            await message.author.send("Hej, " + str(message.author) + "\n\nDitt medelande var:" + str(message.content) + "\n\n" + str(i +1) + "/" + str(len(str(message.content) * 30)) + "\n\n.")
        

Bot.run('NzY4NTU0NzM4NTA5NDE0NDIx.X5CKYA.o8PwUccc7YKYFgOkUqvCmynh388')
