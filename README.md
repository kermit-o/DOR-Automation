# DOR Automation Project

# Descripción del Proyecto

Este proyecto es una aplicación basada en Flask diseñada para automatizar la gestión de reportes DOR (Daily Operations Report) en un entorno hotelero. La aplicación permite a los usuarios realizar varias tareas relacionadas con el manejo de archivos, generación de reportes y gestión de usuarios.

## Funcionalidades Principales

1. **Subida de Archivos**:
   - Los usuarios pueden cargar archivos DOR (en formatos como `.xlsm`, `.xlsx`) a través de un formulario web.
   - Los archivos subidos se procesan, y los datos relevantes se almacenan en una base de datos SQLite.

2. **Gestión de Reportes**:
   - Lista y muestra los reportes procesados en una interfaz web.
   - Permite exportar reportes específicos en formato PDF.
   - Incluye opciones para filtrar y buscar reportes por nombre de archivo.

3. **Descarga de Archivos**:
   - Los usuarios pueden descargar archivos procesados y exportados directamente desde la aplicación.

4. **Eliminación de Archivos**:
   - Proporciona la funcionalidad para eliminar archivos cargados desde la interfaz.

5. **Dashboard y Login**:
   - Los usuarios autenticados pueden acceder a un dashboard con opciones para gestionar reportes, configuraciones y más.
   - Implementa Flask-Login para la autenticación y gestión de sesiones.

6. **Generación de PDFs**:
   - Los reportes DOR procesados pueden ser exportados a PDF con un diseño predefinido.

## Arquitectura del Proyecto

- **`app/__init__.py`**:
  - Inicializa la aplicación Flask.
  - Configura las extensiones como SQLAlchemy, Flask-Migrate y Flask-Login.
  - Registra los blueprints para manejar las rutas de la aplicación.

- **`app/config.py`**:
  - Define las configuraciones principales, incluida la URI de la base de datos SQLite.

- **`app/extensions.py`**:
  - Contiene la inicialización de extensiones como SQLAlchemy (`db`) y Flask-Login (`login`).

- **`app/routes/`**:
  - Contiene blueprints para manejar rutas relacionadas con la gestión de archivos, reportes y el dashboard.

- **`app/models/`**:
  - Define los modelos de la base de datos, como `DORReport`, para almacenar la información procesada de los reportes.

- **`app/utils/`**:
  - Incluye utilidades para manejar archivos, procesar PDFs y gestionar la base de datos.

## Flujo de Trabajo

1. **Subida de Archivos**:
   - Los usuarios cargan un archivo a través del formulario web.
   - El archivo se procesa, y los datos se almacenan en la base de datos.

2. **Visualización de Reportes**:
   - Los usuarios pueden ver una lista de reportes procesados.
   - Opcionalmente, pueden filtrar los reportes por nombre.

3. **Exportación y Descarga**:
   - Los reportes seleccionados pueden exportarse a PDF.
   - Los usuarios pueden descargar los PDFs o archivos originales desde la aplicación.

4. **Autenticación y Dashboard**:
   - Los usuarios inician sesión para acceder al dashboard, donde pueden gestionar los reportes y acceder a funcionalidades adicionales.

## Tecnologías Usadas

- **Backend**:
  - Flask (Framework principal).
  - SQLAlchemy (ORM para la base de datos).
  - Flask-Migrate (Gestión de migraciones).
  - Flask-Login (Autenticación).

- **Frontend**:
  - Jinja2 (Motor de plantillas para renderizar HTML).
  - Bootstrap (Diseño responsivo).

- **Base de Datos**:
  - SQLite (Base de datos ligera y fácil de usar).

## Potenciales Mejoras

1. **Mejorar la Seguridad**:
   - Implementar una mejor gestión de contraseñas (bcrypt o similar).
   - Usar HTTPS en producción.

2. **Interfaz de Usuario**:
   - Mejorar el diseño del dashboard y las páginas con más personalización.

3. **Despliegue**:
   - Migrar a un servidor WSGI para producción, como Gunicorn o uWSGI.
   - Configurar el despliegue en una plataforma como AWS, Heroku o similar.

4. **Soporte para Otros Formatos**:
   - Ampliar el soporte para más formatos de archivos y exportación.
