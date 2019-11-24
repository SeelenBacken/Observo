from datetime import datetime
import mysql.connector
from apprentice.sqlHandler import Select as dbSelect
from apprentice.sqlHandler import Insert as dbInsert
from apprentice.sqlHandler import Check as dbCheck

class Apprentice:

    def newMessage(self, message):
        mL = getMessageList(message)
        dbInsert.insertGuild(self.cursor, mL['guildID'], mL['icon'], ml['ownerID'], mL['guildName'])
        dbInsert.insertChannel(self.cursor, mL['channelID'], mL['channelName'])
        if dbCheck.hasColor(self.cursor, mL['color']):
            dbInsert.insertColor(self.cursor, )



    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database,
            autocommit=True
        )
        self.cursor = self.db.cursor(buffered=True)

def getMessageList(message):
    return {
        'guildID': message.guild.id,
        'guildName': message.guild.name,
        'channelID': message.channel.id,
        'channelName': message.channel.name,
        'roleID': message.author.top_role.id,
        'roleName': message.author.top_role.name,
        'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'icon': message.guild.icon,
        'ownerID': message.guild.owner,
        'color': message.author.top_role.color
        }