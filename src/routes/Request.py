from flask import Blueprint, jsonify, request
import uuid

# MODELOS
from models.RequestModel import RequestModel

# ENTIDADES
from models.entities.Request import Request

main = Blueprint('request_blueprint',__name__)

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
    try:
        request = RequestModel.get_request(id)
        if request != None:
            return jsonify(request)
        else:
            return jsonify({'message':'La orden no fue encontrada'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# AGREGAR UN USUARIO
@main.route('/post', methods=['POST'])
def add_request():
    try:
        id = uuid.uuid4()
        state = request.json['state']
        date = request.json['date']
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
    try:
        request = Request(id)
        affected_rows = RequestModel.delete_request(request)

        if affected_rows == 1:
            return jsonify(request.id)
        else:
            return jsonify({'message': "No se puedo eliminar a la request"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# EDITAR UN USUARIO
@main.route('/put/<id>', methods=['PUT'])
def update_request(id):
    try:
        state = request.json['state']
        date = request.json['date']
        updated_request = Request(id, state, date)  # Cambié el nombre a 'updated_request'

        affected_rows = RequestModel.update_request(updated_request)

        if affected_rows == 1:
            return jsonify(updated_request.id)
        else:
            return jsonify({'message': 'Error al actualizar la solicitud'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500