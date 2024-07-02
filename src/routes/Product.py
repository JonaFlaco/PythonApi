from flask import Blueprint, jsonify, request
import uuid
from models.ProductModel import ProductModel
from models.entities.Product import Product

main = Blueprint('product_blueprint', __name__)

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
        if product:
            return jsonify(product)
        else:
            return jsonify({'message': 'El producto no fue encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# AGREGAR UN PRODUCTO
@main.route('/post', methods=['POST'])
def add_product():
    try:
        # Validar campos obligatorios
        if 'name' not in request.json or 'price' not in request.json or 'description' not in request.json:
            return jsonify({'message': 'Datos incompletos para agregar un producto'}), 400

        name = request.json['name']
        price = request.json['price']
        description = request.json['description']

        # Validar que el precio sea un número positivo
        try:
            price = float(price)
            if price <= 0:
                return jsonify({'message': 'El precio debe ser mayor que cero'}), 400
        except ValueError:
            return jsonify({'message': 'El precio debe ser un número válido'}), 400

        # Validar longitud de campos
        if len(name) > 100 or len(description) > 500:
            return jsonify({'message': 'Longitud máxima de nombre: 100 caracteres, descripción: 500 caracteres'}), 400

        id = str(uuid.uuid4())
        product = Product(id, name, price, description)

        affected_rows = ProductModel.add_product(product)

        if affected_rows == 1:
            return jsonify(product.id)
        else:
            return jsonify({'message': 'Error al agregar el producto'}), 500
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
            return jsonify({'message': "No se pudo eliminar el producto"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# EDITAR UN PRODUCTO
@main.route('/put/<id>', methods=['PUT'])
def update_product(id):
    try:
        # Validar campos obligatorios
        if 'name' not in request.json or 'price' not in request.json or 'description' not in request.json:
            return jsonify({'message': 'Datos incompletos para actualizar un producto'}), 400

        name = request.json['name']
        price = request.json['price']
        description = request.json['description']

        # Validar que el precio sea un número positivo
        try:
            price = float(price)
            if price <= 0:
                return jsonify({'message': 'El precio debe ser mayor que cero'}), 400
        except ValueError:
            return jsonify({'message': 'El precio debe ser un número válido'}), 400

        # Validar longitud de campos
        if len(name) > 100 or len(description) > 500:
            return jsonify({'message': 'Longitud máxima de nombre: 100 caracteres, descripción: 500 caracteres'}), 400

        product = Product(id, name, price, description)

        affected_rows = ProductModel.update_product(product)

        if affected_rows == 1:
            return jsonify(product.id)
        else:
            return jsonify({'message': 'Error al actualizar el producto'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
