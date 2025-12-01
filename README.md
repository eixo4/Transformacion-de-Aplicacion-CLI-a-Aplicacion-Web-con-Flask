# ⚡ Turbo-Librarian Web

**Turbo-Librarian Web** es una aplicación moderna y ultrarrápida para gestionar tu biblioteca personal. Transforma la gestión de libros en una experiencia ágil gracias a su interfaz web limpia y su motor de base de datos en memoria.

<img width="1679" height="1019" alt="image" src="https://github.com/user-attachments/assets/a547b122-f9ca-4dfc-8767-675aff568f5b" />


## 🚀 Características Principales

* **Velocidad Extrema:** Utiliza **KeyDB** (compatible con Redis) para almacenamiento en memoria de alto rendimiento.
* **Interfaz Moderna:** Diseño responsivo y atractivo construido con **Bootstrap 5**.
* **Gestión Completa (CRUD):**
    * **Agregar:** Registra nuevos libros con título, autor, género y estado.
    * **Listar:** Visualiza tu colección en una tabla organizada.
    * **Buscar:** Filtra instantáneamente por título, autor o género.
    * **Editar:** Modifica detalles y actualiza el estado de lectura.
    * **Eliminar:** Borra libros de tu colección de forma segura.
* **Feedback Visual:** Sistema de alertas para confirmar acciones (guardado, eliminado, errores).

## 🛠️ Tecnologías Utilizadas

* **Backend:** [Python](https://www.python.org/) + [Flask](https://flask.palletsprojects.com/)
* **Base de Datos:** [KeyDB](https://docs.keydb.dev/) (o [Redis](https://redis.io/))
* **Frontend:** HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/)
* **Driver:** `redis-py`

## 📋 Requisitos Previos

1.  **Python 3.8** o superior.
2.  **Servidor KeyDB o Redis** en ejecución.
    * *Opción recomendada (Docker):* `docker run -d -p 6379:6379 --name mi-keydb eqalpha/keydb`
    * *Opción Windows:* Redis para Windows (MSI o Zip).

## ⚙️ Instalación y Configuración

Sigue estos pasos para desplegar el proyecto en tu máquina local:

### 1. Clonar el repositorio
Descarga el código fuente en tu computadora.

### 2. Crear entorno virtual (Opcional pero recomendado)
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
````

### 3\. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4\. Configurar variables de entorno

Crea un archivo llamado `.env` en la raíz del proyecto y configura tus credenciales:

```ini
KEYDB_HOST=localhost
KEYDB_PORT=6379
KEYDB_PASSWORD=
SECRET_KEY=clave_secreta_para_flask_cambiar_esto
FLASK_APP=app.py
FLASK_ENV=development
```

> **Nota:** Si tu Redis/KeyDB no tiene contraseña, deja `KEYDB_PASSWORD` vacío.

## ▶️ Ejecución

Asegúrate de que tu servidor de base de datos esté corriendo y luego inicia la aplicación:

```bash
python app.py
```

Abre tu navegador y visita: **[http://127.0.0.1:5000](https://www.google.com/search?q=http://127.0.0.1:5000)**

## 📂 Estructura del Proyecto

```text
turbo-librarian-web/
│
├── app.py              # Controlador principal (Rutas Flask)
├── .env                # Variables de entorno
├── requirements.txt    # Lista de librerías
│
├── static/             # Archivos estáticos
│   └── style.css       # Estilos personalizados
│
└── templates/          # Vistas HTML (Jinja2)
    ├── base.html       # Plantilla maestra (Navbar y Footer)
    ├── index.html      # Página de inicio y listado
    ├── add.html        # Formulario de creación
    └── edit.html       # Formulario de edición
```

## 🐛 Solución de Problemas Comunes

  * **Error 10061 (ConnectionRefused):**
      * Significa que Python no encuentra el servidor de base de datos.
      * *Solución:* Asegúrate de abrir Docker o ejecutar `redis-server.exe` antes de iniciar la app.
  * **Botón "+ Nuevo Libro" invisible:**
      * Si el botón es blanco sobre fondo azul, asegúrate de haber actualizado `base.html` eliminando la clase `nav-link` del botón.

-----

Hecho con ❤️ y Python.
