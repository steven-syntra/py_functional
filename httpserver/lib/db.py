import mysql.connector as mysql


def GetConfig():
    return {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'covid19',
        'raise_on_warnings': True,
    }


def GetData( sql ):

    config = GetConfig()
    cnx = mysql.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)

    data = []
    for row in cursor:
        data.append(row)

    cursor.close()
    cnx.close()

    return data


def DBInsert( sql ):
    config = GetConfig()
    cnx = mysql.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)

    cnx.commit()

    # print( f"Record with id {cursor.lastrowid} inserted.")

    cursor.close()
    cnx.close()

    return cursor.lastrowid


def DBUpdate( sql ):
    config = GetConfig()
    cnx = mysql.connect(**config)
    cursor = cnx.cursor(dictionary=True)

    try:
        cursor.execute(sql)
        cnx.commit()
        aantal_records_geupdated = cursor.rowcount
        cursor.close()
        cnx.close()
        return True
    except:
        return False





