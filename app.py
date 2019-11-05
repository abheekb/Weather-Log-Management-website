from flask import Flask,flash, render_template, request,redirect,url_for
from flask_mysqldb import MySQL
import os

import json 
import requests
  
# urllib.request to make a request to api 
import urllib.request

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abheek123'
app.config['MYSQL_DB'] = 'weather'

db = MySQL(app)
app.secret_key = 'random string'




@app.route('/',methods=['GET','POST'])
# def index():
#         return render_template('index.html')

def login():
        
	if request.method=='GET':
		return render_template('index.html')
	else:
                username = request.form.get('Email').strip()
                pwd = request.form.get('pass').strip()
                cur = db.connection.cursor()
                cur.execute("SELECT * from Users;")
                db.connection.commit()
                l = cur.fetchall()
                for i in l:
                        if i[2]==username and i[3]==pwd:
                                city=i[4]
                                print(city)
                                #api = '951dcc5caf8c9b74aa0fc1e7c9894659'
                                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=951dcc5caf8c9b74aa0fc1e7c9894659'
                                r = requests.get(url.format(city)).json()
                                weather = {
                                'city' : city,
                                'temperature' : r['main']['temp'],
                                'humidity' : r['main']['humidity'],
                                'windspeed' : r['wind']['speed'],
                                }
                                print(weather)
                                cur.close()
                                return render_template('home.html',weather=weather)
                        else:        
                                #flash('Invalid email or password')
                                return render_template('login_error.html')
                                error='invalid email or password'
                        return render_template('index.html',error=error)

@app.route('/home',methods=['GET','POST'])

def home():
        return render_template('home.html')

@app.route('/ChangeCity',methods=['GET','POST'])

def Update_profile():
        if request.method=='GET':
                return render_template('ChangeCity.html')
        else:
                flag=0
                username = request.form.get('Email').strip()
                pwd = request.form.get('pass').strip()
                city = request.form.get('City')
                cur = db.connection.cursor()
                cur.execute("SELECT * from Users;")
                db.connection.commit()
                l = cur.fetchall()
                for i in l:
                        if i[2]==username and i[3]==pwd:
                                flag=1
                
                if(flag==1):                                    
                
                        cur.execute("Update Users set city = %s where E_mail = %s",(city,username))
                        db.connection.commit()

                else :
                        return render_template('ChangeCity.html')
        return render_template('Weather_history.html')

@app.route('/Registration',methods=['GET','POST'])

def Registration():
        if request.method=='GET':
                return render_template('Registration.html')
        else:
                Email=request.form.get('Email')
                Name = request.form.get('Name')
                pwd = request.form.get('pass')
                confpwd= request.form.get('Confirm Password')
                city = request.form.get('City')
                if(pwd!=confpwd):
                        return render_template('Registration.html')
                cur = db.connection.cursor()
                cur.execute("insert into Users (Name,E_mail, Password, City) values(%s,%s,%s,%s)",(Name,Email,pwd,city))
                db.connection.commit()
                return render_template('Weather_history.html')



# @app.route('/currentWeather', methods=['GET', 'POST'])
# def CurrentWeather():

#         cur = db.connection.cursor()
#         cur.execute("SELECT * from Chennai")
#         db.connection.commit()
#         data=cur.fetchall()
#         return render_template('CurrentWeather.html',data=data)

@app.route('/Weather_history', methods=['GET', 'POST'])
def ChooseCity():
		return render_template('Weather_history.html')

@app.route('/Mumbai', methods=['GET', 'POST'])
def ChooseMumbai():

        cur = db.connection.cursor()
        cur.execute("SELECT * from Mumbai")
        db.connection.commit()
        data=cur.fetchall()
        ppt_mon=data[0][1]
        ws_mon=data[0][2]
        temp_mon=data[0][4]
        
        ppt_tue=data[1][1]
        ws_tue=data[1][2]
        temp_tue=data[1][4]
        
        ppt_wed=data[2][1]
        ws_wed=data[2][2]
        temp_wed=data[2][4]
        
        ppt_thu=data[3][1]
        ws_thu=data[3][2]
        temp_thu=data[3][4]
        
        ppt_fri=data[4][1]
        ws_fri=data[4][2]
        temp_fri=data[4][4]
        
        ppt_sat=data[5][1]
        ws_sat=data[5][2]
        temp_sat=data[5][4]
        
        ppt_sun=data[6][1]
        ws_sun=data[6][2]
        temp_sun=data[6][4]

        return render_template('Mumbai.html',ppt_mon=ppt_mon,ppt_tue=ppt_tue,ppt_wed=ppt_wed,ppt_thu=ppt_thu,ppt_fri=ppt_fri,ppt_sat=ppt_sat,ppt_sun=ppt_sun,
                temp_mon=temp_mon,temp_tue=temp_tue,temp_wed=temp_wed,temp_thu=temp_thu,temp_fri=temp_fri,temp_sat=temp_sat,temp_sun=temp_sun,
                ws_mon=ws_mon,ws_tue=ws_tue,ws_wed=ws_wed,ws_thu=ws_thu,ws_fri=ws_fri,ws_sat=ws_sat,ws_sun=ws_sun)

        

@app.route('/Bangalore', methods=['GET', 'POST'])
def ChooseBangalore():

        cur = db.connection.cursor()
        cur.execute("SELECT * from Bangalore")
        db.connection.commit()
        data=cur.fetchall()
        ppt_mon=data[0][1]
        ws_mon=data[0][2]
        temp_mon=data[0][4]
        
        ppt_tue=data[1][1]
        ws_tue=data[1][2]
        temp_tue=data[1][4]
        
        ppt_wed=data[2][1]
        ws_wed=data[2][2]
        temp_wed=data[2][4]
        
        ppt_thu=data[3][1]
        ws_thu=data[3][2]
        temp_thu=data[3][4]
        
        ppt_fri=data[4][1]
        ws_fri=data[4][2]
        temp_fri=data[4][4]
        
        ppt_sat=data[5][1]
        ws_sat=data[5][2]
        temp_sat=data[5][4]
        
        ppt_sun=data[6][1]
        ws_sun=data[6][2]
        temp_sun=data[6][4]

        return render_template('Bangalore.html',ppt_mon=ppt_mon,ppt_tue=ppt_tue,ppt_wed=ppt_wed,ppt_thu=ppt_thu,ppt_fri=ppt_fri,ppt_sat=ppt_sat,ppt_sun=ppt_sun,
                temp_mon=temp_mon,temp_tue=temp_tue,temp_wed=temp_wed,temp_thu=temp_thu,temp_fri=temp_fri,temp_sat=temp_sat,temp_sun=temp_sun,
                ws_mon=ws_mon,ws_tue=ws_tue,ws_wed=ws_wed,ws_thu=ws_thu,ws_fri=ws_fri,ws_sat=ws_sat,ws_sun=ws_sun)

@app.route('/Chennai', methods=['GET', 'POST'])
def ChooseChennai():

        cur = db.connection.cursor()
        cur.execute("SELECT * from Chennai")
        db.connection.commit()
        data=cur.fetchall()
        ppt_mon=data[0][1]
        ws_mon=data[0][2]
        temp_mon=data[0][4]
        
        ppt_tue=data[1][1]
        ws_tue=data[1][2]
        temp_tue=data[1][4]
        
        ppt_wed=data[2][1]
        ws_wed=data[2][2]
        temp_wed=data[2][4]
        
        ppt_thu=data[3][1]
        ws_thu=data[3][2]
        temp_thu=data[3][4]
        
        ppt_fri=data[4][1]
        ws_fri=data[4][2]
        temp_fri=data[4][4]
        
        ppt_sat=data[5][1]
        ws_sat=data[5][2]
        temp_sat=data[5][4]
        
        ppt_sun=data[6][1]
        ws_sun=data[6][2]
        temp_sun=data[6][4]

        return render_template('Bangalore.html',ppt_mon=ppt_mon,ppt_tue=ppt_tue,ppt_wed=ppt_wed,ppt_thu=ppt_thu,ppt_fri=ppt_fri,ppt_sat=ppt_sat,ppt_sun=ppt_sun,
                temp_mon=temp_mon,temp_tue=temp_tue,temp_wed=temp_wed,temp_thu=temp_thu,temp_fri=temp_fri,temp_sat=temp_sat,temp_sun=temp_sun,
                ws_mon=ws_mon,ws_tue=ws_tue,ws_wed=ws_wed,ws_thu=ws_thu,ws_fri=ws_fri,ws_sat=ws_sat,ws_sun=ws_sun)

@app.route('/Delhi', methods=['GET', 'POST'])
def ChooseDelhi():

        cur = db.connection.cursor()
        cur.execute("SELECT * from Delhi")
        db.connection.commit()
        data=cur.fetchall()
        ppt_mon=data[0][1]
        ws_mon=data[0][2]
        temp_mon=data[0][4]
        
        ppt_tue=data[1][1]
        ws_tue=data[1][2]
        temp_tue=data[1][4]
        
        ppt_wed=data[2][1]
        ws_wed=data[2][2]
        temp_wed=data[2][4]
        
        ppt_thu=data[3][1]
        ws_thu=data[3][2]
        temp_thu=data[3][4]
        
        ppt_fri=data[4][1]
        ws_fri=data[4][2]
        temp_fri=data[4][4]
        
        ppt_sat=data[5][1]
        ws_sat=data[5][2]
        temp_sat=data[5][4]
        
        ppt_sun=data[6][1]
        ws_sun=data[6][2]
        temp_sun=data[6][4]

        return render_template('Delhi.html',ppt_mon=ppt_mon,ppt_tue=ppt_tue,ppt_wed=ppt_wed,ppt_thu=ppt_thu,ppt_fri=ppt_fri,ppt_sat=ppt_sat,ppt_sun=ppt_sun,
                temp_mon=temp_mon,temp_tue=temp_tue,temp_wed=temp_wed,temp_thu=temp_thu,temp_fri=temp_fri,temp_sat=temp_sat,temp_sun=temp_sun,
                ws_mon=ws_mon,ws_tue=ws_tue,ws_wed=ws_wed,ws_thu=ws_thu,ws_fri=ws_fri,ws_sat=ws_sat,ws_sun=ws_sun)


##choose Kolkata

@app.route('/Kolkata', methods=['GET', 'POST'])
def ChooseKolkata():

        cur = db.connection.cursor()
        cur.execute("SELECT * from Kolkata")
        db.connection.commit()
        data=cur.fetchall()
        ppt_mon=data[0][1]
        ws_mon=data[0][2]
        temp_mon=data[0][4]
        
        ppt_tue=data[1][1]
        ws_tue=data[1][2]
        temp_tue=data[1][4]
        
        ppt_wed=data[2][1]
        ws_wed=data[2][2]
        temp_wed=data[2][4]
        
        ppt_thu=data[3][1]
        ws_thu=data[3][2]
        temp_thu=data[3][4]
        
        ppt_fri=data[4][1]
        ws_fri=data[4][2]
        temp_fri=data[4][4]
        
        ppt_sat=data[5][1]
        ws_sat=data[5][2]
        temp_sat=data[5][4]
        
        ppt_sun=data[6][1]
        ws_sun=data[6][2]
        temp_sun=data[6][4]

        return render_template('Kolkata.html',ppt_mon=ppt_mon,ppt_tue=ppt_tue,ppt_wed=ppt_wed,ppt_thu=ppt_thu,ppt_fri=ppt_fri,ppt_sat=ppt_sat,ppt_sun=ppt_sun,
                temp_mon=temp_mon,temp_tue=temp_tue,temp_wed=temp_wed,temp_thu=temp_thu,temp_fri=temp_fri,temp_sat=temp_sat,temp_sun=temp_sun,
                ws_mon=ws_mon,ws_tue=ws_tue,ws_wed=ws_wed,ws_thu=ws_thu,ws_fri=ws_fri,ws_sat=ws_sat,ws_sun=ws_sun)


if __name__ == '__main__':
        #app.secret_key = os.urandom(12)
	app.run(debug=True)	
