# FERREMAS" 

- Descomprimir el proyecto en una carperta Ej.Carpeta/ferremas
- Abrir simbolo del sistema apuntando a la Carpeta Principal


### 1. Configuración del Entorno (Recomendacion usar CMD)
```bash
# Creación del entorno virtual y activación
pip install virtualenv

#Crear el entorno virtual con el comando
virtualenv venv

# El siguiente comando activa el entorno virtual 
call venv\Scripts\activate.bat

# Instalación de dependencias iniciales
pip install -r requirements.txt -v

#Entrar en la carpeta del proyecto
cd ferremas
#Ej: Carpeta\ferremas
```

### Organización General
```
Carpeta/
├── ferremas/
├── ├── auth/
├── ├── branches/
├── ├── carts/
├── ├── ferremas/
├── ├── orders/
├── ├── products/
├── ├── stock/
├── ├── users/
├── venv/
├── requirements.txt
├── README.md
```

# Ejecutar el servidor
```bash
python manage.py runserver
```

### Otros

# Aplicar migraciones para crear la tabla en la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```
### Comando para cargar el backup de la base de datos
```bash

python manage.py loaddata backup.json
```

### Documentacion postman con lo solicitado
https://documenter.getpostman.com/view/18246564/2sA3QqhZEa


### Una API que me permita obtener todos los productos activos existentes
api/products/

### Una API que me permita ingresar 1 o más productos a un carro de compras
api/cart/add/

### Una API que me permita pagar el carro de compras y finalizar mi pedido
api/orders/finalize/


### Documentacion postman adicional
https://documenter.getpostman.com/view/18246564/2sA3QqfYLy