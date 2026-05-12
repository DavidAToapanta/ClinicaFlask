from base_datos import db
from base_datos.models import Veterinario


def guardar_veterinario(veterinario):
    """
    Repository: interactua directamente con la base de datos.
    Guarda un veterinario en la DB.
    Retorna: (veterinario, None) si exito, (None, error) si falla.
    """
    try:
        db.session.add(veterinario)      # Prepara el objeto para insertar
        db.session.commit()              # Confirma la transaccion en la DB
        return veterinario, None         # Retorna el veterinario guardado
    except Exception as e:
        db.session.rollback()           # Deshace cualquier cambio si falla
        return None, str(e)             # Retorna el error para manejarlo


def obtener_veterinario_por_id(id):
    """
    Repository: busca un veterinario por su ID en la DB.
    Se usa para validar FK en otras entidades (ej: Consulta).
    Retorna: Veterinario si existe, None si no.
    """
    return Veterinario.query.get(id)