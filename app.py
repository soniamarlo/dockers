from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables del archivo .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255))
    CP = db.Column(db.String(10))
    localidad = db.Column(db.String(100))

class Perro(db.Model):
    __tablename__ = 'perros'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    raza = db.Column(db.String(50), nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), default=0)

class HistorialAdopciones(db.Model):
    __tablename__ = 'historialAdopciones'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    idPerro = db.Column(db.Integer, db.ForeignKey('perros.id'))

@app.route('/')
def index(): #Añadir página de inicio
    return """
    <h1>Bienvenido a la Aplicación de Gestión de Adopciones</h1>
    <p>Utiliza los siguientes endpoints para interactuar con la API:</p>
    <ul>
        <li><strong>GET /usuarios</strong>: Lista de todos los usuarios</li>
        <li><strong>POST /usuarios</strong>: Añadir un nuevo usuario</li>
        <li><strong>GET /perros</strong>: Lista de todos los perros</li>
        <li><strong>POST /perros</strong>: Añadir un nuevo perro</li>
        <li><strong>GET /historialAdopciones</strong>: Ver historial de adopciones</li>
        <li><strong>POST /historialAdopciones</strong>: Añadir un historial de adopción</li>
    </ul>
    <p>Para más información, consulta la documentación o el archivo README.md.</p>
    """
    
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id': u.id, 'nombre': u.nombre, 'email': u.email, 'direccion': u.direccion, 'CP': u.CP, 'localidad': u.localidad} for u in usuarios])

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    nuevo_usuario = Usuario(nombre=data['nombre'], email=data['email'], direccion=data.get('direccion'), CP=data.get('CP'), localidad=data.get('localidad'))

    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'id': nuevo_usuario.id, 'nombre': nuevo_usuario.nombre, 'email': nuevo_usuario.email}), 201

@app.route('/perros', methods=['GET'])
def get_perros():
    perros = Perro.query.all()
    return jsonify([{'id': p.id, 'nombre': p.nombre, 'raza': p.raza, 'idUsuario': p.idUsuario} for p in perros])

@app.route('/perros', methods=['POST'])
def create_perro():
    data = request.json
    nuevo_perro = Perro(nombre=data['nombre'], raza=data['raza'], idUsuario=data.get('idUsuario', 0))
    db.session.add(nuevo_perro)
    db.session.commit()
    return jsonify({'id': nuevo_perro.id, 'nombre': nuevo_perro.nombre, 'raza': nuevo_perro.raza, 'idUsuario': nuevo_perro.idUsuario}), 201

@app.route('/historialAdopciones', methods=['POST'])
def create_historial_adopciones():
    data = request.json
    nuevo_historial = HistorialAdopciones(fecha=data['fecha'], idUsuario=data['idUsuario'], idPerro=data['idPerro'])
    db.session.add(nuevo_historial)
    db.session.commit()
    return jsonify({'id': nuevo_historial.id, 'fecha': nuevo_historial.fecha.isoformat(), 'idUsuario': nuevo_historial.idUsuario, 'idPerro': nuevo_historial.idPerro}), 201@app.route('/historialAdopciones', methods=['GET'])
def get_historial_adopciones():
    historiales = HistorialAdopciones.query.all()
    return jsonify([{'id': h.id, 'fecha': h.fecha.isoformat(), 'idUsuario': h.idUsuario, 'idPerro': h.idPerro} for h in historiales])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
    app.run(host='0.0.0.0', port=8080)
