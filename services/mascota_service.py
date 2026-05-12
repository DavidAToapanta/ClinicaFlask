from base_datos.models import Mascota
from repositories.mascota_repository import guardar_mascota
from repositories.cliente_repository import obtener_cliente_por_id
import re


def crear_mascota(data):
    """
    Service: orquestador con validaciones de negocio.
    Valida los datos de la mascota y llama al repository para guardarla.
    Retorna: (body, status_code)
    """
    # Verifica que se hayan enviado datos
    if not data:
        return {"error": "No se recibió datos"}, 400

    # Extrae los campos del JSON recibido
    nombre = data.get("nombre")
    especie = data.get("especie")
    raza = data.get("raza")
    edad = data.get("edad")
    sexo = data.get("sexo")
    cliente_id = data.get("cliente_id")

    # VALIDACIONES

    # 1. Nombre: obligatorio y no puede estar vacio
    if not nombre or not nombre.strip():
        return {"error": "El nombre es requerido"}, 400

    # 2. Nombre: maximo 100 caracteres
    if len(nombre) > 100:
        return {"error": "El nombre no puede exceder 100 caracteres"}, 400

    # 3. Especie: obligatoria, maximo 50 caracteres
    if not especie or not especie.strip():
        return {"error": "La especie es requerida"}, 400

    if len(especie) > 50:
        return {"error": "La especie no puede exceder 50 caracteres"}, 400

    # 4. Raza (opcional): maximo 100 caracteres
    if raza and len(raza) > 100:
        return {"error": "La raza no puede exceder 100 caracteres"}, 400

    # 5. Edad (opcional): debe ser un entero mayor o igual a 0
    if edad is not None:
        try:
            edad_int = int(edad)
            if edad_int < 0:
                return {"error": "La edad debe ser un número positivo"}, 400
        except (ValueError, TypeError):
            return {"error": "La edad debe ser un número entero"}, 400

    # 6. Sexo (opcional): debe ser uno de los valores permitidos
    if sexo:
        sexo_valido = re.match(r'^(macho|hembra|M|H|Masculino|Femenino)$', sexo, re.IGNORECASE)
        if not sexo_valido:
            return {"error": "Sexo inválido. Use: macho, hembra, M, H, Masculino o Femenino"}, 400

    # 7. Cliente ID: obligatorio, debe existir en la DB
    if not cliente_id:
        return {"error": "El cliente_id es requerido"}, 400

    # Verificar que el cliente existe en la DB
    cliente_existe = obtener_cliente_por_id(cliente_id)
    if not cliente_existe:
        return {"error": f"No existe un cliente con ID {cliente_id}"}, 404

    # CREAR el objeto Mascota con los datos validados
    nueva_mascota = Mascota(
        nombre=nombre.strip(),        # strip() elimina espacios al inicio/final
        especie=especie.strip(),
        raza=raza,
        edad=edad,
        sexo=sexo,
        cliente_id=cliente_id
    )

    # LLAMAR al repository para guardar en la DB
    mascota, error = guardar_mascota(nueva_mascota)

    # Manejar error de la DB
    if error:
        return {"error": f"Error al guardar mascota: {error}"}, 500

    # Exito: retorna la mascota serializada y status 201 (Created)
    return mascota.to_dict(), 201