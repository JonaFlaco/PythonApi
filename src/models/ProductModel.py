from database.db import get_connection
from .entities.Product import Product

class ProductModel():

# OBTENER TODOS LOS USUARIOS
    @classmethod
    def get_products(self):
        try:
            connection = get_connection()
            products = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, price, description FROM product ORDER BY name ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    product = Product(row[0], row[1], row[2], row[3])
                    products.append(product.to_JSON())

            connection.close()
            return products
        except Exception as ex:
            raise Exception(ex)
        
# OBTENER UN PRODUCTO
    @classmethod
    def get_product(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, price, description FROM product WHERE id = %s", (id,))
                row = cursor.fetchone()

                product = None
                if row != None:
                    product = Product(row[0], row[1], row[2], row[3])
                    product = product.to_JSON()

            connection.close()
            return product
        except Exception as ex:
            raise Exception(ex)

# REGISTRAR UN PRODUCTO
    @classmethod
    def add_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO product (id, name, price, description) 
                               VALUES(%s, %s, %s, %s)""",(product.id, product.name, product.price, product.description))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

# ELIMINAR UN PRODUCTO
    @classmethod
    def delete_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM product WHERE id = %s", (product.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
# ACTUALIZAR UN PRODUCTO
    @classmethod
    def update_product(self, product):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE product SET name = %s, price = %s, description = %s
                               WHERE id = %s""",(product.name, product.price, product.description, product.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)