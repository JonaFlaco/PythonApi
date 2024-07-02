from flask import Flask
from config import config

# Rutas
from routes import Person
from routes import Product
from routes import Request

app = Flask(__name__)

def page_not_found(error): 
    return "<h1>Pagina no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # BluePrints
    app.register_blueprint(Person.main, url_prefix='/api/persons')
    app.register_blueprint(Product.main, url_prefix='/api/products')
    app.register_blueprint(Request.main, url_prefix='/api/requests')

    #Error Handler
    app.register_error_handler(404, page_not_found)
    app.run()
