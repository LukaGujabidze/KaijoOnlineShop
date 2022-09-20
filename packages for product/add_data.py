def add_data(table, row, data):
    import mysql.connector
    from mysql.connector import Error
    try:
        statement = f"INSERT INTO {table} ({row}) VALUES (%s, %s)"
        data = (row)
        connection = mysql.connector.connect(host='kaijo-db',
                                            database='KBase',
                                            user='luka',
                                            password='luka')
        cursor = connection.cursor()
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except Error as e:
        print(f"Error adding entry to database: {e}")
