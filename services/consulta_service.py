from datetime import datetime
from base_datos.models import Consulta
from repositories.consulta_repository import guardar_consulta
from repositories.mascota_repository import obtener_mascota_por_id
from repositories.veterinario_repository import obtener_veterinario_por_id


def crear_consulta(data):
    """
    Service: orquestador con validaciones de negocio.
    Valida los datos de la consulta y llama al repository para guardarla.
    Retorna: (body, status_code)
    """
    # Verifica que se hayan enviado datos
    if not data:
        return {"error": "No se recibió datos"}, 400

    # Extrae los campos del JSON recibido
    fecha = data.get("fecha")
    motivo = data.get("motivo")
    diagnostico = data.get("diagnostico")
    tratamiento = data.get("tratamiento")
    mascota_id = data.get("mascota_id")
    veterinario_id = data.get("veterinario_id")

    # VALIDACIONES

    # 1. Fecha (opcional): si se proporciona, debe ser formato valido
    fecha_parsed = None
    if fecha:
        try:
            # Acepta formatos como "2024-01-15" o "2024-01-15T10:30:00"
            fecha_parsed = datetime.fromisoformat(fecha.replace('Z', '+00:00'))
        except (ValueError, AttributeError):
            return {"error": "Fecha inválida. Use formato ISO (YYYY-MM-DD o YYYY-MM-DDTHH:MM:SS)"}, 400

    # 2. Motivo: obligatorio
    if not motivo or not motivo.strip():
        return {"error": "El motivo es requerido"}, 400

    # 3. Motivo: maximo 255 caracteres
    if len(motivo) > 255:
        return {"error": "El motivo no puede exceder 255 caracteres"}, 400

    # 4. Diagnostico (opcional): texto libre, sin limite
    # No requiere validacion especial

    # 5. Tratamiento (opcional): texto libre, sin limite
    # No requiere validacion especial

    # 6. Mascota ID: obligatorio, debe existir en la DB
    if not mascota_id:
        return {"error": "El mascota_id es requerido"}, 400

    # Verificar que la mascota existe en la DB
    mascota_existe = obtener_mascota_por_id(mascota_id)
    if not mascota_existe:
        return {"error": f"No existe una mascota con ID {mascota_id}"}, 404

    # 7. Veterinario ID: obligatorio, debe existir en la DB
    if not veterinario_id:
        return {"error": "El veterinario_id es requerido"}, 400

    # Verificar que el veterinario existe en la DB
    veterinario_existe = obtener_veterinario_por_id(veterinario_id)
    if not veterinario_existe:
        return {"error": f"No existe un veterinario con ID {veterinario_id}"}, 404

    # CREAR el objeto Consulta con los datos validados
    nueva_consulta = Consulta(
        fecha=fecha_parsed,            # None usa default del modelo (datetime.utcnow)
        motivo=motivo.strip(),
        diagnostico=diagnostico,
        tratamiento=tratamiento,
        mascota_id=mascota_id,
        veterinario_id=veterinario_id
    )

    # LLAMAR al repository para guardar en la DB
    consulta, error = guardar_consulta(nueva_consulta)

    # Manejar error de la DB
    if error:
        return {"error": f"Error al guardar consulta: {error}"}, 500

    # Exito: retorna la consulta serializada y status 201 (Created)
    return consulta.to_dict(), 201