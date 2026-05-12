# pyrefly: ignore [missing-import]
from flask import Blueprint, request, jsonify
from services.consulta_servicio_service import crear_consulta_servicio


# Blueprint: define un grupo de rutas relacionadas
# Se registrara en app.py con el prefijo '/consulta-servicios'
consulta_servicios_bp = Blueprint('consulta_servicios', __name__)


@consulta_servicios_bp.route('/', methods=['POST'])
def crear():
    """
    Route: recibe las peticiones HTTP y responde.
    Endpoint: POST /consulta-servicios/
    """
    data = request.get_json()                       # Obtiene el JSON del body
    body, status = crear_consulta_servicio(data)    # Llama al service para procesar
    return jsonify(body), status                    # Convierte el dict a JSON y retorna