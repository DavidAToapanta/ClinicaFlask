# pyrefly: ignore [missing-import]
from flask import Blueprint, request, jsonify
from services.servicio_service import crear_servicio


# Blueprint: define un grupo de rutas relacionadas
# Se registrara en app.py con el prefijo '/servicios'
servicios_bp = Blueprint('servicios', __name__)


@servicios_bp.route('/', methods=['POST'])
def crear():
    """
    Route: recibe las peticiones HTTP y responde.
    Endpoint: POST /servicios/
    """
    data = request.get_json()          # Obtiene el JSON del body de la peticion
    body, status = crear_servicio(data)  # Llama al service para procesar
    return jsonify(body), status      # Convierte el dict a JSON y retorna