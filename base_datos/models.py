from . import db
from datetime import datetime

class Cliente(db.Model):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(150))
    direccion = db.Column(db.String(255))

    mascotas = db.relationship('Mascota', backref='cliente', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'email': self.email,
            'direccion': self.direccion
        }
        
class Mascota(db.Model):
    __tablename__ = 'mascota'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    raza = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    sexo = db.Column(db.String(20))

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    consultas = db.relationship('Consulta', backref='mascota', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'especie': self.especie,
            'raza': self.raza,
            'edad': self.edad,
            'sexo': self.sexo,
            'cliente_id': self.cliente_id
        }


class Veterinario(db.Model):
    __tablename__ = 'veterinario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

    consultas = db.relationship('Consulta', backref='veterinario', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'especialidad': self.especialidad,
            'telefono': self.telefono
        }


class Consulta(db.Model):
    __tablename__ = 'consulta'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    motivo = db.Column(db.String(255), nullable=False)
    diagnostico = db.Column(db.Text)
    tratamiento = db.Column(db.Text)

    mascota_id = db.Column(db.Integer, db.ForeignKey('mascota.id'), nullable=False)
    veterinario_id = db.Column(db.Integer, db.ForeignKey('veterinario.id'), nullable=False)

    servicios = db.relationship(
        'ConsultaServicio',
        backref='consulta',
        lazy=True,
        cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'fecha': self.fecha,
            'motivo': self.motivo,
            'diagnostico': self.diagnostico,
            'tratamiento': self.tratamiento,
            'mascota_id': self.mascota_id,
            'veterinario_id': self.veterinario_id
        }


class Servicio(db.Model):
    __tablename__ = 'servicio'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)

    consultas = db.relationship('ConsultaServicio', backref='servicio', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio
        }

class ConsultaServicio(db.Model):
    __tablename__ = 'consulta_servicio'

    id = db.Column(db.Integer, primary_key=True)

    consulta_id = db.Column(db.Integer, db.ForeignKey('consulta.id'), nullable=False)
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicio.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'consulta_id': self.consulta_id,
            'servicio_id': self.servicio_id
        }
