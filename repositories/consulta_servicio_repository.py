from base_datos import db
from base_datos.models import ConsultaServicio


def guardar_consulta_servicio(consulta_servicio):
    """
    Repository: interactua directamente con la base de datos.
    Guarda una relacion consulta-servicio en la DB.
    Retorna: (consulta_servicio, None) si exito, (None, error) si falla.
    """
    try:
        db.session.add(consulta_servicio)  # Prepara el objeto para insertar
        db.session.commit()                  # Confirma la transaccion en la DB
        return consulta_servicio, None       # Retorna la relacion guardada
    except Exception as e:
        db.session.rollback()               # Deshace cualquier cambio si falla
        return None, str(e)                 # Retorna el error para manejarlo