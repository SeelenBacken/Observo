def insertGuild(cursor, guildID, icon, ownerID, guildName):
    cursor.execute('INSERT INTO Guild (ID, icon, ownerID, name) VALUES ({}, {}, {}, {});'
                   .format(guildID, icon, ownerID, guildName))

def insertChannel(cursor, channelID, channelName):
    cursor.execute('INSERT INTO Channel (ID, name) VALUES ({}, {});'.format(channelID, channelName))

def insertRole(cursor, roleID, roleName, colorID):
    cursor.execute('INSERT INTO Role (ID, name, colorID) VALUES ({}, {}, {});'.format(roleID, roleName, colorID))

'''def insertMessage(cursor, messageID, dateTime, guildID, channelID):
    cursor.execute('INSERT INTO Message (ID, datetime, guildID, channelID) VALUES ({}, {}, {}, {});'
                   .format(messageID, dateTime, guildID, channelID))'''

def insertMessage(cursor, dateTime, guildID, channelID):
    cursor.execute('INSERT INTO Message (datetime, guildID, channelID) VALUES ({}, {}, {});'
                   .format(dateTime, guildID, channelID))

def insertColor(cursor, color):
    r, g, b = color.r, color.g, color.b
    cursor.execute('INSERT INTO Color (r, g, b) VALUES ({}, {}, {});'.format(r, g, b))

def insertRoleList(cursor, messageID, roleID):
    cursor.execute('INSERT INTO roleList (messageID, roleID) VALUES ({}, {});'.format(messageID, roleID))

