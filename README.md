# FERREMAS" 
### 1. Configuración del Entorno
```bash
# Creación del entorno virtual y activación
pip install virtualenv

#ir a la carpeta que estara alojado el proyecto carpeta base donde se dejara la carpeta ferremas 
# Ejemplo: FERREMAS\

#crear el entorno virtual con el comando
virtualenv venv

# El siguiente comando es solo para windows
call venv\Scripts\activate.bat

#entrar en la carpeta interna del proyecto
cd ferremas
#Ej: FERREMAS\ferremas

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