from base_datos import db
from base_datos.models import Consulta


def guardar_consulta(consulta):
    """
    Repository: interactua directamente con la base de datos.
    Guarda una consulta en la DB.
    Retorna: (consulta, None) si exito, (None, error) si falla.
    """
    try:
        db.session.add(consulta)      # Prepara el objeto para insertar
        db.session.commit()            # Confirma la transaccion en la DB
        return consulta, None          # Retorna la consulta guardada
    except Exception as e:
        db.session.rollback()         # Deshace cualquier cambio si falla
        return None, str(e)           # Retorna el error para manejarlo


def obtener_consulta_por_id(id):
    """
    Repository: busca una consulta por su ID en la DB.
    Se usa para validar FK en otras entidades (ej: ConsultaServicio).
    Retorna: Consulta si existe, None si no.
    """
    return Consulta.query.get(id)