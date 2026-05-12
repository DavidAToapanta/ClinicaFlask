from base_datos.models import Servicio
from repositories.servicio_repository import guardar_servicio


def crear_servicio(data):
    """
    Service: orquestador con validaciones de negocio.
    Valida los datos del servicio y llama al repository para guardarlo.
    Retorna: (body, status_code)
    """
    # Verifica que se hayan enviado datos
    if not data:
        return {"error": "No se recibió datos"}, 400

    # Extrae los campos del JSON recibido
    nombre = data.get("nombre")
    precio = data.get("precio")

    # VALIDACIONES

    # 1. Nombre: obligatorio y no puede estar vacio
    if not nombre or not nombre.strip():
        return {"error": "El nombre es requerido"}, 400

    # 2. Nombre: maximo 100 caracteres
    if len(nombre) > 100:
        return {"error": "El nombre no puede exceder 100 caracteres"}, 400

    # 3. Precio: obligatorio
    if precio is None:
        return {"error": "El precio es requerido"}, 400

    # 4. Precio: debe ser un numero positivo
    try:
        precio_float = float(precio)
        if precio_float <= 0:
            return {"error": "El precio debe ser un número positivo"}, 400
    except (ValueError, TypeError):
        return {"error": "El precio debe ser un número"}, 400

    # CREAR el objeto Servicio con los datos validados
    nuevo_servicio = Servicio(
        nombre=nombre.strip(),       # strip() elimina espacios al inicio/final
        precio=precio_float
    )

    # LLAMAR al repository para guardar en la DB
    servicio, error = guardar_servicio(nuevo_servicio)

    # Manejar error de la DB
    if error:
        return {"error": f"Error al guardar servicio: {error}"}, 500

    # Exito: retorna el servicio serializado y status 201 (Created)
    return servicio.to_dict(), 201