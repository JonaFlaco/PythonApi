from flask import Blueprint, jsonify, request
import uuid

# MODELOS
from models.RequestModel import RequestModel

# ENTIDADES
from models.entities.Request import Request

main = Blueprint('request_blueprint', __name__)

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

def is_valid_request_data(data):
    required_fields = ['state', 'date']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Falta el campo {field} o está vacío."
    return True, ""

# BUSCAR TODOS LOS USUARIOS
@main.route('/')
def get_requests():
    try:
        requests = RequestModel.get_requests()
        return jsonify(requests)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# BUSCAR UN USUARIO
@main.route('/<id>')
def get_request(id):
    if not is_valid_uuid(id):
        return jsonify({'message': 'ID inválido'}), 400
    try:
        request_data = RequestModel.get_request(id)
        if request_data is not None:
            return jsonify(request_data)
        else:
            return jsonify({'message': 'La orden no fue encontrada'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# AGREGAR UN USUARIO
@main.route('/post', methods=['POST'])
def add_request():
    data = request.json
    is_valid, message = is_valid_request_data(data)
    if not is_valid:
        return jsonify({'message': message}), 400
    try:
        id = uuid.uuid4()
        state = data['state']
        date = data['date']
        new_request = Request(str(id), state, date)

        affected_rows = RequestModel.add_request(new_request)

        if affected_rows == 1:
            return jsonify(new_request.id)
        else:
            return jsonify({'message': 'Error al agregar la solicitud'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# ELIMINAR UN USUARIO
@main.route('/delete/<id>', methods=['DELETE'])
def delete_request(id):
    if not is_valid_uuid(id):
        return jsonify({'message': 'ID inválido'}), 400
    try:
        request = Request(id)
        affected_rows = RequestModel.delete_request(request)

        if affected_rows == 1:
            return jsonify(request.id)
        else:
            return jsonify({'message': "No se pudo eliminar la solicitud"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# EDITAR UN USUARIO
@main.route('/put/<id>', methods=['PUT'])
def update_request(id):
    if not is_valid_uuid(id):
        return jsonify({'message': 'ID inválido'}), 400
    data = request.json
    is_valid, message = is_valid_request_data(data)
    if not is_valid:
        return jsonify({'message': message}), 400
    try:
        state = data['state']
        date = data['date']
        updated_request = Request(id, state, date)

        affected_rows = RequestModel.update_request(updated_request)

        if affected_rows == 1:
            return jsonify(updated_request.id)
        else:
            return jsonify({'message': 'Error al actualizar la solicitud'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
