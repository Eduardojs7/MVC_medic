from flask import Flask
from .routes import biblioteca_bp  # Asegúrate de que el Blueprint se importe correctamente

def create_app():
    app = Flask(__name__)

    # Registrar el Blueprint
    app.register_blueprint(biblioteca_bp, url_prefix='/biblioteca')  # Aquí se registra el Blueprint

    return app
