from flask import Flask
from config import config

# Rutas
from routes import Person

app = Flask(__name__)

def page_not_found(error): 
    return "<h1>Pagina no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # BluePrints
    app.register_blueprint(Person.main, url_prefix='/api/persons')

    #Error Handler
    app.register_error_handler(404, page_not_found)
    app.run()
