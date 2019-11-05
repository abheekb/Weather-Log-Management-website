from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abheek123'
app.config['MYSQL_DB'] = 'weather'

db = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('templates/login.html')
    else:
        username = request.form.get('uname')
        pwd = reqeust.form.get('pwd')
        cur = db.connection.cursor()
        cur.execute("SELECT EmpID from EMPLOYEE WHERE Username='%s' AND EmpPassword='%s';".format(username,pwd))
        db.commit()
        l = cur.fetchall()
        if len(l)==1:
            cur.close()
            return l[0]
        return False
    # if request.method == "POST":
    #     details = request.form
    #      = details['']
    #     lastName = details['lname']
    #     cur = mysql.connection.cursor()
    #     cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
    #     mysql.connection.commit()
    #     cur.close()
    #     return 'success'
    # return 'Hello World'



if __name__ == '__main__':

    app.run()
