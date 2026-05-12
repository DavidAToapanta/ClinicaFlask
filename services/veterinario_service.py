from base_datos.models import Veterinario
from repositories.veterinario_repository import guardar_veterinario
import re


def crear_veterinario(data):
    """
    Service: orquestador con validaciones de negocio.
    Valida los datos del veterinario y llama al repository para guardarlo.
    Retorna: (body, status_code)
    """
    # Verifica que se hayan enviado datos
    if not data:
        return {"error": "No se recibió datos"}, 400

    # Extrae los campos del JSON recibido
    nombre = data.get("nombre")
    especialidad = data.get("especialidad")
    telefono = data.get("telefono")

    # VALIDACIONES

    # 1. Nombre: obligatorio y no puede estar vacio
    if not nombre or not nombre.strip():
        return {"error": "El nombre es requerido"}, 400

    # 2. Nombre: maximo 100 caracteres
    if len(nombre) > 100:
        return {"error": "El nombre no puede exceder 100 caracteres"}, 400

    # 3. Especialidad (opcional): maximo 100 caracteres
    if especialidad and len(especialidad) > 100:
        return {"error": "La especialidad no puede exceder 100 caracteres"}, 400

    # 4. Telefono (opcional): regex valida que tenga 7-15 digitos, puede empezar con +
    if telefono:
        telefono_valido = re.match(r'^\+?[0-9]{7,15}$', telefono)
        if not telefono_valido:
            return {"error": "Teléfono inválido"}, 400

    # CREAR el objeto Veterinario con los datos validados
    nuevo_veterinario = Veterinario(
        nombre=nombre.strip(),       # strip() elimina espacios al inicio/final
        especialidad=especialidad,
        telefono=telefono
    )

    # LLAMAR al repository para guardar en la DB
    veterinario, error = guardar_veterinario(nuevo_veterinario)

    # Manejar error de la DB
    if error:
        return {"error": f"Error al guardar veterinario: {error}"}, 500

    # Exito: retorna el veterinario serializado y status 201 (Created)
    return veterinario.to_dict(), 201