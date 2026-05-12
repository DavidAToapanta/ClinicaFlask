from base_datos.models import Cliente
from repositories.cliente_repository import guardar_cliente
import re


def crear_cliente(data):
    """
    Service: orquestador con validaciones de negocio.
    Valida los datos del cliente y llama al repository para guardarlo.
    Retorna: (body, status_code)
    """
    # Verifica que se hayan enviado datos
    if not data:
        return {"error": "No se recibió datos"}, 400

    # Extrae los campos del JSON recibido
    nombre = data.get("nombre")
    telefono = data.get("telefono")
    email = data.get("email")
    direccion = data.get("direccion")

    # VALIDACIONES

    # 1. Nombre: obligatorio y no puede estar vacio
    if not nombre or not nombre.strip():
        return {"error": "El nombre es requerido"}, 400

    # 2. Nombre: maximo 100 caracteres
    if len(nombre) > 100:
        return {"error": "El nombre no puede exceder 100 caracteres"}, 400

    # 3. Telefono (opcional): regex valida que tenga 7-15 digitos, puede empezar con +
    if telefono:
        telefono_valido = re.match(r'^\+?[0-9]{7,15}$', telefono)
        if not telefono_valido:
            return {"error": "Teléfono inválido"}, 400

    # 4. Email (opcional): verifica formato basico de email
    if email:
        email_valido = re.match(r'^[^@]+@[^@]+\.[^@]+$', email)
        if not email_valido:
            return {"error": "Email inválido"}, 400

    # 5. Direccion (opcional): maximo 255 caracteres
    if direccion and len(direccion) > 255:
        return {"error": "La dirección no puede exceder 255 caracteres"}, 400

    # CREAR el objeto Cliente con los datos validados
    nuevo_cliente = Cliente(
        nombre=nombre.strip(),    # strip() elimina espacios al inicio/final
        telefono=telefono,
        email=email,
        direccion=direccion
    )

    # LLAMAR al repository para guardar en la DB
    cliente, error = guardar_cliente(nuevo_cliente)

    # Manejar error de la DB
    if error:
        return {"error": f"Error al guardar cliente: {error}"}, 500

    # Exito: retorna el cliente serializado y status 201 (Created)
    return cliente.to_dict(), 201