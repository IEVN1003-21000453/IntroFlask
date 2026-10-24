from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import config
from blueprints.alumnos.routes import alumnos_bp
from blueprints.maestros.routes import maestros_bp

app = Flask(__name__)

app.config.from_object(config['development'])

CORS(app)

con = MySQL(app)

app.register_blueprint(alumnos_bp)
app.register_blueprint(maestros_bp)

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>"

if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000)