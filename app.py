import os 
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from flask import Flask
from base_datos import _init_db
import base_datos.models

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'clave-secreet')
_init_db(app)

# Registrar blueprints de todos los modelos
from routes.cliente_routes import clientes_bp
from routes.mascota_routes import mascotas_bp
from routes.veterinario_routes import veterinarios_bp
from routes.consulta_routes import consultas_bp
from routes.servicio_routes import servicios_bp
from routes.consulta_servicio_routes import consulta_servicios_bp

app.register_blueprint(clientes_bp, url_prefix='/clientes')
app.register_blueprint(mascotas_bp, url_prefix='/mascotas')
app.register_blueprint(veterinarios_bp, url_prefix='/veterinarios')
app.register_blueprint(consultas_bp, url_prefix='/consultas')
app.register_blueprint(servicios_bp, url_prefix='/servicios')
app.register_blueprint(consulta_servicios_bp, url_prefix='/consulta-servicios')


@app.route("/")
def hello_world():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True)
