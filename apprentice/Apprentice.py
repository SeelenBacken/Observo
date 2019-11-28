from datetime import datetime
import mysql.connector
from apprentice.sqlHandler import Select as dbSelect
from apprentice.sqlHandler import Insert as dbInsert
from apprentice.sqlHandler import Check as dbCheck

class Apprentice:
    """ Apprentice is handling everything having to do with the database.
    
        When a new entry or search request is made, a new Apprentice should
        be initialized. This way he connects, executes order 66
        and goes for spontaneous non-human combustion. 
        
        My brain doesn't work this early.
    
    """

    def newMessage(self, message):
        mL = message(message)
        if not dbCheck.hasGuild(self.cursor, mL.guildID):
            dbInsert.insertGuild(self.cursor, mL.guildID, mL.icon,\
                                 mL.ownerID, mL.guildName)
        
        dbInsert.insertChannel(self.cursor, mL.channelID, mL.channelName)
        
        if not dbCheck.hasColor(self.cursor, mL.color):
            dbInsert.insertColor(self.cursor, mL.color)
            
        dbInsert.insertMessage(self.cursor, mL.dateTime, mL.guildID,\
                               mL.channelID)
        
        if not dbCheck.hasRole(self.cursor, mL.roleID):
            dbInsert.insertRole(self.cursor, mL.roleID, mL.roleName,\
                            dbSelect.getColorID(self.cursor, mL.color))
            
        dbInsert.insertRoleList(self.cursor, dbSelect.getLastID(self.cursor),\
                                mL.roleID)

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database,
            autocommit=True
        )
        self.cursor = self.db.cursor(buffered=True)
    
class message:
    def __init__(self, message):
        self.guildID = message.guild.id
        self.guildName = message.guild.name
        self.channelID = message.channel.id
        self.channelName = message.channel.name
        self.roleID = message.author.top_role.id
        self.roleName = message.author.top_role.name
        self.datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.icon = message.guild.icon
        self.ownerID = message.guild.owner
        self.color = message.author.top_role.color