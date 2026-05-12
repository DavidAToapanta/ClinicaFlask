# pyrefly: ignore [missing-import]
from flask import Blueprint, request, jsonify
from services.cliente_service import crear_cliente


# Blueprint: define un grupo de rutas relacionadas
# Se registrara en app.py con el prefijo '/clientes'
clientes_bp = Blueprint('clientes', __name__)


@clientes_bp.route('/', methods=['POST'])
def crear():
    """
    Route: recibe las peticiones HTTP y responde.
    Endpoint: POST /clientes/ (la / se agrega por el url_prefix)
    """
    data = request.get_json()       # Obtiene el JSON del body de la peticion
    body, status = crear_cliente(data)  # Llama al service para procesar
    return jsonify(body), status   # Convierte el dict a JSON y retorna