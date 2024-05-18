# FERREMAS" 
### 1. Configuración del Entorno
```bash
# Creación del entorno virtual y activación
pip3 install virtualenv
virtualenv venv
# El siguiente comando es solo para windows
call venv\Scripts\activate.bat

cd ferremas

# Instalación de dependencias iniciales
pip install Django
# Manualmente deben crear un archivo llamado en el root del proyecto requirements.txt

# Instalación de Django REST Framework
pip install djangorestframework

# Aplicar migraciones para crear la tabla en la base de datos
python manage.py makemigrations
python manage.py migrate

# Ejecutar el servidor
python manage.py runserver
```