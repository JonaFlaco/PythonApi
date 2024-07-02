from database.db import get_connection
from .entities.Request import Request

class RequestModel():

# OBTENER TODOS LOS USUARIOS
    @classmethod
    def get_requests(self):
        try:
            connection = get_connection()
            requests = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, state, date FROM request ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    request = Request(row[0], row[1], row[2])
                    requests.append(request.to_JSON())

            connection.close()
            return requests
        except Exception as ex:
            raise Exception(ex)
        
# OBTENER UN USUARIO
    @classmethod
    def get_request(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, state, date FROM request WHERE id = %s", (id,))
                row = cursor.fetchone()

                request = None
                if row != None:
                    request = Request(row[0], row[1], row[2])
                    request = request.to_JSON()

            connection.close()
            return request
        except Exception as ex:
            raise Exception(ex)

# REGISTRAR UN USUARIO
    @classmethod
    def add_request(self, request):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO request (id, state, date) 
                               VALUES(%s, %s, %s)""",(request.id, request.state, request.date))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

# ELIMINAR UN USUARIO
    @classmethod
    def delete_request(self, request):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM request WHERE id = %s", (request.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
# ACTUALIZAR UN USUARIO
    @classmethod
    def update_request(self, request):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE request SET state = %s, date = %s
                               WHERE id = %s""",(request.state, request.date, request.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)