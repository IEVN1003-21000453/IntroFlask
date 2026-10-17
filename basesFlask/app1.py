
from flask import Flask, render_template, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "Pagina de Inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template("index.html", titulo=titulo, listado=listado)

@app.route("/operabas", methods=["GET", "POST"])
def operabas():
    n1 = 0
    n2 = 0
    res = 0

    if request.method == 'POST':
        n1 = float(request.form.get('n1', 0))
        n2 = float(request.form.get('n2', 0))
        operacion = request.form.get('operacion')

        if operacion == 'sumar':
            res = n1 + n2
        elif operacion == 'restar':
            res = n1 - n2
        elif operacion == 'multiplicar':
            res = n1 * n2

    return render_template(
        "operabas.html",
        n1=n1,
        n2=n2,
        res=res
    )

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    px1 = 0
    py1 = 0
    px2 = 0
    py2 = 0
    res = 0

    if request.method == 'POST':
        px1 = float(request.form.get('px1', 0))
        py1 = float(request.form.get('py1', 0))
        px2 = float(request.form.get('px2', 0))
        py2 = float(request.form.get('py2', 0))

        res = sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)

    return render_template(
        "distancia.html",
        px1=px1,
        py1=py1,
        px2=px2,
        py2=py2,
        res=res
    )

@app.route('/hola')
def hola():
    return "<h1>Hola PWA - IEVN1003</h1>"

@app.route('/user/<string:nom>')
def user(nom):
    return "<h1>Hola User: {}</h1>".format(nom)

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route('/suma/<float:n1>/<float:n2>')
def func(n1, n2):
    return "La suma es: {}".format(n1 + n2)

if __name__ == "__main__":
    app.run(debug=True)
