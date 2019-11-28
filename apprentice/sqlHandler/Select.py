def getGuildIDs(cursor):
    return select(cursor, 'ID', 'Guild')

def getChannelIDs(cursor):
    return select(cursor, 'ID', 'Channel')

def getRoleIDs(cursor):
    return select(cursor, 'ID', 'Role')

def getColorIDs(cursor):
    return select(cursor, 'ID', 'Color')

def getLastID(cursor, table='Message'):
    return cursor.execute('SELECT ID From {} ORDER BY ID DESC LIMIT 1'.format(table))

def getColorID(cursor, color):
    r = color.r
    g = color.g
    b = color.b
    cursor.execute('SELECT ID FROM Color WHERE r={} AND g={} AND b={};'.format(r, g, b))
    return cursor.fetchall()

def select(cursor, column, table):
    cursor.execute('SELECT {} FROM {}'.format(column, table))
    return cursor.fetchall()
