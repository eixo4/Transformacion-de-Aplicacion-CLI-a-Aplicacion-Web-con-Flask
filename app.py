import os
import json
import uuid
import redis
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

# Cargar configuración
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev_key')

# --- CONEXIÓN A KEYDB / REDIS ---
try:
    db = redis.Redis(
        host=os.getenv('KEYDB_HOST', 'localhost'),
        port=int(os.getenv('KEYDB_PORT', 6379)),
        password=os.getenv('KEYDB_PASSWORD', None),
        decode_responses=True  # Importante para recibir Strings, no Bytes
    )
    db.ping()  # Check de conexión
except redis.ConnectionError:
    print("❌ Error: No se pudo conectar a KeyDB. Asegúrate que esté corriendo.")


# --- RUTAS ---

@app.route('/')
def index():
    """Página principal: Listado y Búsqueda"""
    query = request.args.get('q', '').lower()
    libros = []

    # Recorremos todas las claves que empiecen con 'libro:'
    for key in db.scan_iter("libro:*"):
        data_json = db.get(key)
        if data_json:
            libro = json.loads(data_json)

            # Filtro de búsqueda (si hay query)
            if query:
                if (query in libro['titulo'].lower() or
                        query in libro['autor'].lower() or
                        query in libro['genero'].lower()):
                    libros.append(libro)
            else:
                libros.append(libro)

    return render_template('index.html', libros=libros, query=query)


@app.route('/add', methods=['GET', 'POST'])
def add_libro():
    """Agregar nuevo libro"""
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        genero = request.form['genero']
        estado = request.form['estado']

        # Validar campos vacíos
        if not titulo or not autor:
            flash('Título y Autor son obligatorios', 'danger')
            return redirect(url_for('add_libro'))

        # Generar ID y guardar
        book_id = str(uuid.uuid4())
        key = f"libro:{book_id}"

        libro_dict = {
            "id": book_id,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "estado": estado
        }

        try:
            db.set(key, json.dumps(libro_dict))
            flash('¡Libro agregado exitosamente!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error al guardar: {e}', 'danger')

    return render_template('add.html')


@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit_libro(book_id):
    """Editar libro existente"""
    key = f"libro:{book_id}"

    if not db.exists(key):
        flash('El libro no existe', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        # Obtener datos del form
        libro_dict = {
            "id": book_id,  # Mantenemos el ID original
            "titulo": request.form['titulo'],
            "autor": request.form['autor'],
            "genero": request.form['genero'],
            "estado": request.form['estado']
        }

        db.set(key, json.dumps(libro_dict))  # Sobreescribir
        flash('Libro actualizado correctamente', 'success')
        return redirect(url_for('index'))

    # GET: Cargar datos actuales para mostrarlos en el form
    data_json = db.get(key)
    libro = json.loads(data_json)
    return render_template('edit.html', libro=libro)


@app.route('/delete/<book_id>', methods=['POST'])
def delete_libro(book_id):
    """Eliminar libro"""
    key = f"libro:{book_id}"
    db.delete(key)
    flash('Libro eliminado del sistema', 'warning')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)