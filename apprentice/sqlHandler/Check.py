import apprentice.sqlHandler.Select as dbSelect

def hasColor(cursor, color):
    result = dbSelect.getColorID(cursor, color.r, color.g, color.b)
    if result is not None:
        return True
    else:
        return False
    
def hasRole(cursor, roleID):
    result = dbSelect.getRole(cursor, roleID)
    if result is not None:
        return True
    else:
        return False
