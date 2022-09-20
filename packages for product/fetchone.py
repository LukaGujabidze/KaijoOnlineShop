import mysql.connector



connection = mysql.connector.connect(host='kaijo-db',
                                         database='KBase',
                                         user='luka',
                                         password='luka')


mycursor = connection.cursor()
query = "SELECT username FROM accounts WHERE email = %s"
email = "lukas.gujabidze@gmail.com"
mycursor.execute("SELECT username FROM accounts WHERE email = '%s'" %(email))
myresult = mycursor.fetchone()

if myresult[0] == 'luka':
    print('We have find your account')  
else:
    print('Oops, something went wrong!')    


