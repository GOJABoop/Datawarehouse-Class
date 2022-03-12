#García Ochoa José Alberto 
from crypt import methods
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import pymysql

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' #write the password
app.config['MYSQL_DB'] = 'world'

mysql = MySQL(app)


def obtener_conexion():
    return pymysql.connect(host='localhost', user='root', password='', db='world')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/read')
def read():
    return render_template('read.html')


@app.route('/read/country',  methods=['POST'])
def searchCountry():
    countryName = request.form['country']
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM country WHERE Name = (%s)''',(countryName,))
    countryFound = cursor.fetchone() 
    return render_template('read.html', verified=True, country=countryFound)


@app.route('/create')
def create():
    return render_template('create.html', added=False)


@app.route('/create/country',  methods=['POST'])
def addCountry():
    code = request.form['code']
    name = request.form['name']
    continent = int(request.form['continent'])
    region = request.form['region']
    surface = int(request.form['surface'])
    indepYear = int(request.form['indepYear'])
    population = int(request.form['population'])
    lifeExp = int(request.form['lifeExp'])
    gnp = int(request.form['gnp'])
    gnp_old = int(request.form['gnp_old'])
    local_name = request.form['local_name']
    gover_form = request.form['gover_form']
    head_of_state = request.form['head_of_state']
    capital = int(request.form['capital'])
    code2 = request.form['code2']

    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO country(Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Code2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (code,name,continent,region,surface,indepYear,population,lifeExp,gnp,gnp_old,local_name,gover_form,head_of_state,capital,code2))
    conexion.commit()
    conexion.close()
    return render_template('create.html', added=True)


@app.route('/delete')
def delete():
    return render_template('delete.html')


@app.route('/delete/country',  methods=['POST'])
def deleteCountry():
    countryName = request.form['country']
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM country WHERE Name = %s", (countryName,))
    conexion.commit()
    conexion.close()

    return redirect('/')


@app.route('/update')
def update():
    return render_template('update.html', updated=False)


@app.route('/update/country',  methods=['POST'])
def updateCountry():
    code = request.form['code']
    name = request.form['name']
    continent = int(request.form['continent'])
    region = request.form['region']
    surface = int(request.form['surface'])
    indepYear = int(request.form['indepYear'])
    population = int(request.form['population'])
    lifeExp = int(request.form['lifeExp'])
    gnp = int(request.form['gnp'])
    gnp_old = int(request.form['gnp_old'])
    local_name = request.form['local_name']
    gover_form = request.form['gover_form']
    head_of_state = request.form['head_of_state']
    capital = int(request.form['capital'])
    code2 = request.form['code2']

    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE country SET Name=%s, Continent=%s, Region=%s, SurfaceArea=%s, IndepYear=%s, Population=%s, LifeExpectancy=%s, GNP=%s, GNPOld=%s, LocalName=%s, GovernmentForm=%s, HeadOfState=%s, Capital=%s, Code2=%s WHERE Code=%s", (name,continent,region,surface,indepYear,population,lifeExp,gnp,gnp_old,local_name,gover_form,head_of_state,capital,code2,code))
    conexion.commit()
    conexion.close()
    return render_template('update.html', update=True)


if __name__=='__main__':
    app.run(debug=True)