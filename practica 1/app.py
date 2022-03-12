from crypt import methods
import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/busca_mayor')
def buscaMayor():
    return render_template('busca_mayor.html', verificado=False)


@app.route('/max', methods=['POST'])
def max():
    maximo = 0
    numeros = []
    numeros.append(int(request.form['n1']))
    numeros.append(int(request.form['n2']))
    numeros.append(int(request.form['n3']))
    numeros.append(int(request.form['n4']))
    numeros.append(int(request.form['n5']))
    numeros.append(int(request.form['n6']))
    numeros.append(int(request.form['n7']))
    numeros.append(int(request.form['n8']))
    numeros.append(int(request.form['n9']))
    numeros.append(int(request.form['n10']))
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    print(maximo)
    return render_template('busca_mayor.html', verificado=True, max=str(maximo))


@app.route('/solucionador_cuadraticas')
def solucionadorCuadraticas():
    return render_template('cuadraticas.html', verificado=False)


@app.route('/solucionador_cuadraticas/solucion', methods=['POST'])
def solucion():
    A = int(request.form['a'])
    B = int(request.form['b'])
    C = int(request.form['c'])
    x1= 0
    x2= 0
    solucion = False

    if ((B**2)-4*A*C) < 0:
        solucion = False
    else:
        x1 = (-B+math.sqrt(B**2-(4*A*C)))/(2*A)
        x2 = (-B-math.sqrt(B**2-(4*A*C)))/(2*A)
        solucion = True

    return render_template('cuadraticas.html', verificado=True, solucion=solucion, x1=x1, x2=x2)


@app.route('/repeticiones_input')
def repeticionesInput():
    return render_template('busca_input.html', verficado=False)


@app.route('/repeticiones_input/solucion', methods=['POST'])
def encuentraRepeticionesInput():
    palabras = request.form['lienzo'].split()
    repeticiones = 0
    
    for palabra in palabras:
        if palabra == 'input':
            repeticiones = repeticiones + 1
    
    return render_template('busca_input.html', verificado=True, repeticiones=repeticiones)


if __name__=='__main__':
    app.run(debug=True)