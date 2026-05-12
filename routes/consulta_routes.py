# pyrefly: ignore [missing-import]
from flask import Blueprint, request, jsonify
from services.consulta_service import crear_consulta


# Blueprint: define un grupo de rutas relacionadas
# Se registrara en app.py con el prefijo '/consultas'
consultas_bp = Blueprint('consultas', __name__)


@consultas_bp.route('/', methods=['POST'])
def crear():
    """
    Route: recibe las peticiones HTTP y responde.
    Endpoint: POST /consultas/
    """
    data = request.get_json()          # Obtiene el JSON del body de la peticion
    body, status = crear_consulta(data)  # Llama al service para procesar
    return jsonify(body), status      # Convierte el dict a JSON y retorna