from flask import Flask
from config import config
from flasgger import Swagger

# Rutas
from routes import Person
from routes import Product
from routes import Request
from routes import OrderDetail

app = Flask(__name__)
swagger = Swagger(app)  # Inicializa Swagger

def page_not_found(error): 
    return "<h1>Pagina no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # BluePrints
    app.register_blueprint(Person.main, url_prefix='/api/persons')
    app.register_blueprint(Product.main, url_prefix='/api/products')
    app.register_blueprint(Request.main, url_prefix='/api/requests')
    app.register_blueprint(OrderDetail.main, url_prefix='/api/orderDetails')

    # Error Handler
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0', port=8000, debug=True)  # Asegúrate de que se exponga en todas las interfaces
