from flask import Blueprint, render_template, request, redirect, url_for
from .models import LIBROS  # Si usas un archivo models.py para almacenar la lista de libros

# Crear el Blueprint
biblioteca_bp = Blueprint('biblioteca', __name__)

# Ruta para la página de inicio (index)
@biblioteca_bp.route('/')
def index():
    return render_template('index.html')

# Ruta para ver los libros
@biblioteca_bp.route('/ver_libros')
def obtener_libros():
    return render_template('ver_libros.html', libros=LIBROS)

# Ruta para agregar un libro
@biblioteca_bp.route('/agregar_libro', methods=['GET', 'POST'])
def agregar_libro():
    if request.method == 'POST':
        # Obtener los datos del formulario
        titulo = request.form['titulo']
        autor = request.form['autor']
        
        # Crear un nuevo libro (como un diccionario) y agregarlo a la lista
        nuevo_libro = {
            "id": len(LIBROS) + 1,  # El ID será el siguiente número disponible
            "titulo": titulo,
            "autor": autor
        }
        LIBROS.append(nuevo_libro)  # Agregar a la lista de libros
        
        # Redirigir a la página de ver libros
        return redirect(url_for('biblioteca.obtener_libros'))
    
    return render_template('agregar_libro.html')
