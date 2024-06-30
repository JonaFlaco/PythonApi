from flask import Blueprint, jsonify, request
import uuid

# MODELOS
from models.ProductModel import ProductModel

# ENTIDADES
from models.entities.Product import Product

main = Blueprint('product_blueprint',__name__)

# BUSCAR TODOS LOS PRODUCTOS
@main.route('/')
def get_products():
    try:
        products = ProductModel.get_products()
        return jsonify(products)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# BUSCAR UN PRODUCTO
@main.route('/<id>')
def get_product(id):
    try:
        product = ProductModel.get_product(id)
        if product != None:
            return jsonify(product)
        else:
            return jsonify({'message':'El producto no fue encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# AGREGAR UN PRODUCTO
@main.route('/post', methods = ['POST'])
def add_product():
    try:
        id = uuid.uuid4()
        name = request.json['name']
        price = request.json['price']
        description = request.json['description']
        product = Product(str(id), name, price, description)

        affected_rows = ProductModel.add_product(product)

        if affected_rows == 1:
            return jsonify (product.id)
        else:
            return jsonify({'message': 'Error al agregar la producto'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# ELIMINAR UN PRODUCTO
@main.route('/delete/<id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product(id)
        affected_rows = ProductModel.delete_product(product)

        if affected_rows == 1:
            return jsonify(product.id)
        else:
            return jsonify({'message': "No se puedo eliminar el producto"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# EDITAR UN PRODUCTO
@main.route('/put/<id>', methods = ['PUT'])
def update_product(id):
    try:
        name = request.json['name']
        price = request.json['price']
        description = request.json['description']
        product = Product(id, name, price, description)

        affected_rows = ProductModel.update_product(product)

        if affected_rows == 1:
            return jsonify (product.id)
        else:
            return jsonify({'message': 'Error al actualizar el producto'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500