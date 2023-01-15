async def showCommands(message):

    commands = ['1. hi', '2. help']

    response = 'Hi, I am jake the bot and I can understand following commands 😄 - \n\n' + '\n'.join(commands)

    await message.channel.send(response)
