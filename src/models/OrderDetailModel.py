from database.db import get_connection
from .entities.OrderDetail import OrderDetail

class OrderDetailModel():

#OBTENER TODOS LOS DETALLES DE ORDEN
    @classmethod
    def get_orderDetails(self):
        try:
            connection = get_connection()
            orderDetails = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, amount, unit_price, person_id, product_id FROM order_detail ORDER BY amount ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    orderDetail = OrderDetail(row[0], row[1], row[2], row[3], row[4])
                    orderDetails.append(orderDetail.to_JSON())

            connection.close()
            return orderDetails
        except Exception as ex:
            raise Exception(ex)

#OBTENER UN DETALLE DE ORDEN
    @classmethod
    def get_orderDetail(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, amount, unit_price, person_id, product_id FROM order_detail WHERE id = %s", (id,))
                row = cursor.fetchone()

                orderDetail = None
                if row != None:
                    orderDetail = OrderDetail(row[0], row[1], row[2], row[3], row[4])
                    orderDetail = orderDetail.to_JSON()

            connection.close()
            return orderDetail
        except Exception as ex:
            raise Exception(ex)

#REGISTRAR UN DETALLE DE ORDEN
    @classmethod
    def add_orderDetail(self, orderDetail):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO order_detail (id, amount, unit_price, person_id, product_id) 
                               VALUES(%s, %s, %s, %s, %s)""",(orderDetail.id, orderDetail.amount, orderDetail.unitPrice, orderDetail.personId, orderDetail.productId))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

#ELIMINAR UN DETALLE DE ORDEN
    @classmethod
    def delete_orderDetail(self, orderDetail):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM order_detail WHERE id = %s", (orderDetail.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

#ACTUALIZAR UN DETALLE DE ORDEN
    @classmethod
    def update_orderDetail(self, orderDetail):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE order_detail SET amount = %s, unit_price = %s, person_id = %s, product_id = %s
                               WHERE id = %s""",(orderDetail.amount, orderDetail.unitPrice, orderDetail.personId, orderDetail.productId, orderDetail.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
