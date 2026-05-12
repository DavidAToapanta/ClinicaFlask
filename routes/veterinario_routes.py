# pyrefly: ignore [missing-import]
from flask import Blueprint, request, jsonify
from services.veterinario_service import crear_veterinario


# Blueprint: define un grupo de rutas relacionadas
# Se registrara en app.py con el prefijo '/veterinarios'
veterinarios_bp = Blueprint('veterinarios', __name__)


@veterinarios_bp.route('/', methods=['POST'])
def crear():
    """
    Route: recibe las peticiones HTTP y responde.
    Endpoint: POST /veterinarios/
    """
    data = request.get_json()           # Obtiene el JSON del body de la peticion
    body, status = crear_veterinario(data)  # Llama al service para procesar
    return jsonify(body), status       # Convierte el dict a JSON y retorna