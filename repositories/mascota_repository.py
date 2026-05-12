from base_datos import db
from base_datos.models import Mascota


def guardar_mascota(mascota):
    """
    Repository: interactua directamente con la base de datos.
    Guarda una mascota en la DB.
    Retorna: (mascota, None) si exito, (None, error) si falla.
    """
    try:
        db.session.add(mascota)      # Prepara el objeto para insertar
        db.session.commit()          # Confirma la transaccion en la DB
        return mascota, None         # Retorna la mascota guardada
    except Exception as e:
        db.session.rollback()       # Deshace cualquier cambio si falla
        return None, str(e)         # Retorna el error para manejarlo


def obtener_mascota_por_id(id):
    """
    Repository: busca una mascota por su ID en la DB.
    Se usa para validar FK en otras entidades (ej: Consulta).
    Retorna: Mascota si existe, None si no.
    """
    return Mascota.query.get(id)