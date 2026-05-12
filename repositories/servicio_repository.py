from base_datos import db
from base_datos.models import Servicio


def guardar_servicio(servicio):
    """
    Repository: interactua directamente con la base de datos.
    Guarda un servicio en la DB.
    Retorna: (servicio, None) si exito, (None, error) si falla.
    """
    try:
        db.session.add(servicio)      # Prepara el objeto para insertar
        db.session.commit()            # Confirma la transaccion en la DB
        return servicio, None          # Retorna el servicio guardado
    except Exception as e:
        db.session.rollback()         # Deshace cualquier cambio si falla
        return None, str(e)           # Retorna el error para manejarlo


def obtener_servicio_por_id(id):
    """
    Repository: busca un servicio por su ID en la DB.
    Se usa para validar FK en otras entidades (ej: ConsultaServicio).
    Retorna: Servicio si existe, None si no.
    """
    return Servicio.query.get(id)