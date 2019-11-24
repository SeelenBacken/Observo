def getGuildIDs(cursor):
    return select(cursor, 'ID', 'Guild')

def getChannelIDs(cursor):
    return select(cursor, 'ID', 'Channel')

def getRoleIDs(cursor):
    return select(cursor, 'ID', 'Role')

def getColorIDs(cursor):
    return select(cursor, 'ID', 'Color')

def getColorID(cursor, r, g, b):
    cursor.execute('SELECT ID FROM Color WHERE r={} AND g={} AND b={};')
    return cursor.fetchall()


def select(cursor, column, table):
    cursor.execute('SELECT {} FROM {}'.format(column, table))
    return cursor.fetchall()
