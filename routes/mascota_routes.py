# pyrefly: ignore [missing-import]
from flask import Blueprint, request, jsonify
from services.mascota_service import crear_mascota


# Blueprint: define un grupo de rutas relacionadas
# Se registrara en app.py con el prefijo '/mascotas'
mascotas_bp = Blueprint('mascotas', __name__)


@mascotas_bp.route('/', methods=['POST'])
def crear():
    """
    Route: recibe las peticiones HTTP y responde.
    Endpoint: POST /mascotas/ (la / se agrega por el url_prefix)
    """
    data = request.get_json()       # Obtiene el JSON del body de la peticion
    body, status = crear_mascota(data)  # Llama al service para procesar
    return jsonify(body), status   # Convierte el dict a JSON y retorna