# app/repositories.py
from .models import Libro

class RepositorioLibros:
    def __init__(self):
        self.libros = []  # Almacenamos los libros en memoria

    def obtener_todos(self):
        return self.libros

    def agregar(self, libro):
        self.libros.append(libro)
