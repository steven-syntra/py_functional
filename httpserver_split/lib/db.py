import mysql.connector as mysql


def GetData( sql ):

    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'sakila',
        'raise_on_warnings': True,
    }

    cnx = mysql.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)

    data = []
    for row in cursor:
        data.append(row)

    cursor.close()
    cnx.close()

    return data

