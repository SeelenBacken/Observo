from apprentice import Apprentice
from terminator import Terminator
from confuzius import Confuzius
import discord
import datetime

'''A bot for User analysis or some other stuff I don't know about yet.

    He runs on a local server and is private use only currently. As soon as the project is ready he becomes available
    for everyone, if possible ofc. (ToC or smth, idk)
    '''
configs = {
    'name': 'Observo',
    'prefix': 'Osrv'
}

print('------Welcome to Observo------')
# term = Terminator()
conf = Confuzius()
client = discord.Client()


@client.event
async def on_ready():
    """ Called when succesfully logged in through discord auth token."""
    print(getTimeString() + 'Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    """ Called when a message is send."""
    if message.author == client.user:
        return
    elif message.content == '$month':
        await message.channel.send('Noch ein Erfolg')
    elif message.content == '$week':
        await message.channel.send('Erfolg')
    else:
        apprentice = Apprentice.Apprentice(conf.getDBHost(),\
                                           conf.getDBUsername(),\
                                           conf.getDBPassword(), conf.getDB())
        apprentice.newMessage(message)

def getTimeString():
    """ This is just here for the Console output."""
    now = datetime.datetime.now()
    return '[{}.{}.{}-{}:{}:{}] '.format(now.year, now.month, now.day, now.hour, now.minute, now.second)


client.run(conf.getToken())
