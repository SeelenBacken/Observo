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
# discordObserver = Apprentice()

client = discord.Client()


@client.event
async def on_ready():
    print(getTimeString() + 'Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    messageList = getMessageList(message)
    if message.author == client.user:
        return
    elif message.content == '$test':
        await message.channel.send('Erfolg du Fotze')
    else:
        print('')

def getTimeString():
    now = datetime.datetime.now()
    return '[{}.{}.{}-{}:{}:{}] '.format(now.year, now.month, now.day, now.hour, now.minute, now.second)

def getMessageList(message):
    return {
        'guildID': message.guild.id,
        'guildName': message.guild.name,
        'channelID': message.channel.id,
        'channelName': message.channel.name,
        'roleID': message.author.roles[-1].id,
        'roleName': message.author.roles[-1].name,
        'datetime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }


client.run(conf.getToken())
