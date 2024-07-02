from flask import Blueprint, jsonify, request
import uuid

# MODELOS
from models.OrderDetailModel import OrderDetailModel

# ENTIDADES
from models.entities.OrderDetail import OrderDetail

main = Blueprint('orderDetail_blueprint', __name__)

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

def is_valid_request_data(data):
    required_fields = ['amount', 'unitPrice', 'personId', 'productId']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Falta el campo {field} o está vacío."
    return True, ""

# BUSCAR TODOS LOS DETALLES DE ORDEN
@main.route('/')
def get_orderDetails():
    try:
        orderDetails = OrderDetailModel.get_orderDetails()
        return jsonify(orderDetails)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# BUSCAR UN DETALLE DE ORDEN
@main.route('/<id>')
def get_orderDetail(id):
    if not is_valid_uuid(id):
        return jsonify({'message': 'ID inválido'}), 400
    try:
        orderDetail = OrderDetailModel.get_orderDetail(id)
        if orderDetail is not None:
            return jsonify(orderDetail)
        else:
            return jsonify({'message': 'El detalle de la orden no fue encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# AGREGAR UNA ORDEN DE DETALLE
@main.route('/post', methods=['POST'])
def add_orderDetail():
    data = request.json
    is_valid, message = is_valid_request_data(data)
    if not is_valid:
        return jsonify({'message': message}), 400
    try:
        id = uuid.uuid4()
        amount = data['amount']
        unitPrice = data['unitPrice']
        personId = data['personId']
        productId = data['productId']
        orderDetail = OrderDetail(str(id), amount, unitPrice, personId, productId)

        affected_rows = OrderDetailModel.add_orderDetail(orderDetail)

        if affected_rows == 1:
            return jsonify(orderDetail.id)
        else:
            return jsonify({'message': 'Error al agregar el detalle de la orden'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# ELIMINAR UN DETALLE DE ORDEN
@main.route('/delete/<id>', methods=['DELETE'])
def delete_orderDetail(id):
    if not is_valid_uuid(id):
        return jsonify({'message': 'ID inválido'}), 400
    try:
        orderDetail = OrderDetail(id)
        affected_rows = OrderDetailModel.delete_orderDetail(orderDetail)

        if affected_rows == 1:
            return jsonify(orderDetail.id)
        else:
            return jsonify({'message': "No se pudo eliminar el detalle de la orden"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# EDITAR UN DETALLE DE ORDEN
@main.route('/put/<id>', methods=['PUT'])
def update_orderDetail(id):
    if not is_valid_uuid(id):
        return jsonify({'message': 'ID inválido'}), 400
    data = request.json
    is_valid, message = is_valid_request_data(data)
    if not is_valid:
        return jsonify({'message': message}), 400
    try:
        amount = data['amount']
        unitPrice = data['unitPrice']
        personId = data['personId']
        productId = data['productId']
        orderDetail = OrderDetail(id, amount, unitPrice, personId, productId)

        affected_rows = OrderDetailModel.update_orderDetail(orderDetail)

        if affected_rows == 1:
            return jsonify(orderDetail.id)
        else:
            return jsonify({'message': 'Error al actualizar el detalle de la orden'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
