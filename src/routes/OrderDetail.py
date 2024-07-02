from flask import Blueprint, jsonify, request
import uuid

# MODELOS
from models.OrderDetailModel import OrderDetailModel

# ENTIDADES
from models.entities.OrderDetail import OrderDetail

main = Blueprint('orderDetail_blueprint',__name__)

# BUSCAR TODOS LOS USUARIOS
@main.route('/')
def get_orderDetails():
    try:
        orderDetails = OrderDetailModel.get_orderDetails()
        return jsonify(orderDetails)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# BUSCAR UN USUARIO
@main.route('/<id>')
def get_orderDetail(id):
    try:
        orderDetail = OrderDetailModel.get_orderDetail(id)
        if orderDetail != None:
            return jsonify(orderDetail)
        else:
            return jsonify({'message':'El usuario no fue encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# AGREGAR UN USUARIO
@main.route('/post', methods = ['POST'])
def add_orderDetail():
    try:
        id = uuid.uuid4()
        amount = request.json['amount']
        unitPrice = request.json['unitPrice']
        orderDetail = OrderDetail(str(id), amount, unitPrice)

        affected_rows = OrderDetailModel.add_orderDetail(orderDetail)

        if affected_rows == 1:
            return jsonify (orderDetail.id)
        else:
            return jsonify({'message': 'Error al agregar el detalle de la orden'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# ELIMINAR UN USUARIO
@main.route('/delete/<id>', methods=['DELETE'])
def delete_orderDetail(id):
    try:
        orderDetail = OrderDetail(id)
        affected_rows = OrderDetailModel.delete_orderDetail(orderDetail)

        if affected_rows == 1:
            return jsonify(orderDetail.id)
        else:
            return jsonify({'message': "No se puedo eliminar a el detalle de la orden"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# EDITAR UN USUARIO
@main.route('/put/<id>', methods = ['PUT'])
def update_orderDetail(id):
    try:
        amount = request.json['amount']
        unitPrice = request.json['unitPrice']
        orderDetail = OrderDetail(id, amount, unitPrice)

        affected_rows = OrderDetailModel.update_orderDetail(orderDetail)

        if affected_rows == 1:
            return jsonify (orderDetail.id)
        else:
            return jsonify({'message': 'Error al actualizar el Detalle de la orden'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500