from base_datos import db
from base_datos.models import Cliente


def guardar_cliente(cliente):
    """
    Repository: interactua directamente con la base de datos.
    Guarda un cliente en la DB.
    Retorna: (cliente, None) si exito, (None, error) si falla.
    """
    try:
        db.session.add(cliente)      # Prepara el objeto para insertar
        db.session.commit()          # Confirma la transaccion en la DB
        return cliente, None         # Retorna el cliente guardado
    except Exception as e:
        db.session.rollback()       # Deshace cualquier cambio si falla
        return None, str(e)         # Retorna el error para manejarlo


def obtener_cliente_por_id(id):
    """
    Repository: busca un cliente por su ID en la DB.
    Se usa para validar FK en otras entidades (ej: Mascota, Consulta).
    Retorna: Cliente si existe, None si no.
    """
    return Cliente.query.get(id)