from base_datos.models import ConsultaServicio
from repositories.consulta_servicio_repository import guardar_consulta_servicio
from repositories.consulta_repository import obtener_consulta_por_id
from repositories.servicio_repository import obtener_servicio_por_id


def crear_consulta_servicio(data):
    """
    Service: orquestador con validaciones de negocio.
    Valida los datos de la relacion consulta-servicio y llama al repository.
    Retorna: (body, status_code)
    """
    # Verifica que se hayan enviado datos
    if not data:
        return {"error": "No se recibió datos"}, 400

    # Extrae los campos del JSON recibido
    consulta_id = data.get("consulta_id")
    servicio_id = data.get("servicio_id")

    # VALIDACIONES

    # 1. Consulta ID: obligatorio, debe existir en la DB
    if not consulta_id:
        return {"error": "El consulta_id es requerido"}, 400

    # Verificar que la consulta existe en la DB
    consulta_existe = obtener_consulta_por_id(consulta_id)
    if not consulta_existe:
        return {"error": f"No existe una consulta con ID {consulta_id}"}, 404

    # 2. Servicio ID: obligatorio, debe existir en la DB
    if not servicio_id:
        return {"error": "El servicio_id es requerido"}, 400

    # Verificar que el servicio existe en la DB
    servicio_existe = obtener_servicio_por_id(servicio_id)
    if not servicio_existe:
        return {"error": f"No existe un servicio con ID {servicio_id}"}, 404

    # CREAR el objeto ConsultaServicio con los datos validados
    nueva_relacion = ConsultaServicio(
        consulta_id=consulta_id,
        servicio_id=servicio_id
    )

    # LLAMAR al repository para guardar en la DB
    consulta_servicio, error = guardar_consulta_servicio(nueva_relacion)

    # Manejar error de la DB
    if error:
        return {"error": f"Error al guardar relación: {error}"}, 500

    # Exito: retorna la relacion serializada y status 201 (Created)
    return consulta_servicio.to_dict(), 201