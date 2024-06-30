from database.db import get_connection
from .entities.Person import Person

class PersonModel():

# OBTENER TODOS LOS USUARIOS
    @classmethod
    def get_persons(self):
        try:
            connection = get_connection()
            persons = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, user_name, birthday FROM person ORDER BY name ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    person = Person(row[0], row[1], row[2], row[3])
                    persons.append(person.to_JSON())

            connection.close()
            return persons
        except Exception as ex:
            raise Exception(ex)
        
# OBTENER UN USUARIO
    @classmethod
    def get_person(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, user_name, birthday FROM person WHERE id = %s", (id,))
                row = cursor.fetchone()

                person = None
                if row != None:
                    person = Person(row[0], row[1], row[2], row[3])
                    person = person.to_JSON()

            connection.close()
            return person
        except Exception as ex:
            raise Exception(ex)

# REGISTRAR UN USUARIO
    @classmethod
    def add_person(self, person):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO person (id, name, user_name, birthday) 
                               VALUES(%s, %s, %s, %s)""",(person.id, person.name, person.userName, person.birthday))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

# ELIMINAR UN USUARIO
    @classmethod
    def delete_person(self, person):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM person WHERE id = %s", (person.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
# ACTUALIZAR UN USUARIO
    @classmethod
    def update_person(self, person):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE person SET name = %s, user_name = %s, birthday = %s
                               WHERE id = %s""",(person.name, person.userName, person.birthday, person.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)