from flask import Flask,render_template,url_for,request,redirect,flash
import hashlib
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/cart.html')
def cart():
    return render_template('cart.html')

@app.route('/pay.html')
def pay():
    return render_template('pay.html')

@app.route('/shop.html')
def shop():
    return render_template('shop.html')






#------------------------------------------------------------------------------------------------------------

#this function connects to database
def connect_sql():
    #libraries to connect mysql
    import mysql.connector
    from mysql.connector import Error

    try:
        #this code connects database
        connection = mysql.connector.connect(host='kaijo-db',
                                            database='KBase',
                                            user='luka',
                                            password='luka')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)


#this function adds data in database
def add_data_in_accounts(table, username, email, password):
    import mysql.connector
    from mysql.connector import Error
    try:
        #this is sql script to add data in database
        statement = "INSERT INTO accounts (Username, Email, PasswordHash) VALUES (%s, %s, %s);"
        
        connection = mysql.connector.connect(host='kaijo-db',
                                            database='KBase',
                                            user='luka',
                                            password='luka')
        cursor = connection.cursor()
        data = (username, email, password)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except Error as e:
        print(f"Error adding entry to database: {e}")


#this function gets data from database
def get_data_from_account(table, username, email, password):
    import mysql.connector
    from mysql.connector import Error

    connection = mysql.connector.connect(host='kaijo-db',
                                            database='KBase',
                                            user='luka',
                                            password='luka')
    mycursor = connection.cursor()
    mycursor.execute("SELECT username FROM accounts WHERE Username='%s' and Email='%s' and PasswordHash='%s'" %(username, email, password))
    if mycursor == username:
        return True
    else:
        return False

@app.route('/favicon.ico')
def favicon():
    return render_template('favicon.ico')

@app.route("/logo.png")
def image():
    return render_template("logo.png")

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/img_avatar2.png')
def png():
    return render_template('img_avatar2.png')    

@app.route('/')
def home():
    connect_sql()
    return render_template('home.html')

@app.route('/home.html', methods=['GET','POST'])
def h():
    return render_template('home.html')    

@app.route('/sign.html', methods=['GET', 'POST'])
def sign():
    return render_template('sign.html')

@app.route('/account.html', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        result = request.form
        name = result.get('uname')
        passowrd = result.get('psw').encode('UTF-8')
        hashed_pass = hashlib.sha256(passowrd).hexdigest()
        mail = result.get('semail')

        """file = open('database.txt')
        read_file = file.read()"""

        if get_data_from_account('accounts', name, mail, hashed_pass):
            return render_template('account.html', user=name)
        else:
            return render_template('not_account.html', user=name)

    #return render_template('account.html')


@app.route('/not_account.html')
def not_acc():
    return render_template('not_account.html')

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/reg_account.html', methods=['GET', 'POST'])
def reg_acc():
    if request.method == 'POST':
        result = request.form
        username = result.get('username')
        email = result.get('email')
        if result.get('passw') == result.get('psw-repeat'):
            password = result.get('psw-repeat').encode('UTF-8')
            hashed_pass = hashlib.sha256(password).hexdigest()


            """with open('database.txt','a') as file:
               file.write(f'\n{username}/{email}/{hashed_pass}')
               file .close()"""


            connect_sql()
            add_data_in_accounts('accounts',username,email,hashed_pass)

            return render_template('reg_account.html',user=username)
        
        return render_template('reg_account.html',user=username)        

@app.route('/error.html')
def error():
    return render_template('error.html')

@app.route('/privacy.html')
def privasy():
    return render_template('privacy.html')

if __name__ == '__main__':
    app.run(debug=True)






