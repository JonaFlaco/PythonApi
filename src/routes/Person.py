from flask import Blueprint, jsonify, request
import uuid

# MODELOS
from models.PersonModel import PersonModel

# ENTIDADES
from models.entities.Person import Person

main = Blueprint('person_blueprint',__name__)

# BUSCAR TODOS LOS USUARIOS
@main.route('/')
def get_persons():
    try:
        persons = PersonModel.get_persons()
        return jsonify(persons)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# BUSCAR UN USUARIO
@main.route('/<id>')
def get_person(id):
    try:
        person = PersonModel.get_person(id)
        if person != None:
            return jsonify(person)
        else:
            return jsonify({'message':'El usuario no fue encontrado'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# AGREGAR UN USUARIO
@main.route('/post', methods = ['POST'])
def add_person():
    try:
        id = uuid.uuid4()
        name = request.json['name']
        userName = request.json['userName']
        birthday = request.json['birthday']
        person = Person(str(id), name, userName, birthday)

        affected_rows = PersonModel.add_person(person)

        if affected_rows == 1:
            return jsonify (person.id)
        else:
            return jsonify({'message': 'Error al agregar la persona'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# ELIMINAR UN USUARIO
@main.route('/delete/<id>', methods=['DELETE'])
def delete_person(id):
    try:
        person = Person(id)
        affected_rows = PersonModel.delete_person(person)

        if affected_rows == 1:
            return jsonify(person.id)
        else:
            return jsonify({'message': "No se puedo eliminar a la persona"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
# EDITAR UN USUARIO
@main.route('/put/<id>', methods = ['PUT'])
def update_person(id):
    try:
        name = request.json['name']
        userName = request.json['userName']
        birthday = request.json['birthday']
        person = Person(id, name, userName, birthday)

        affected_rows = PersonModel.update_person(person)

        if affected_rows == 1:
            return jsonify (person.id)
        else:
            return jsonify({'message': 'Error al actualizar la persona'}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500