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



### Comando para cargar el backup de la base de datos (Opcional)
# la base de datos se encuentra poblada
```bash

python manage.py loaddata backup.json
```


### Otros

# Aplicar migraciones para crear la tabla en la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### Documentacion postman Completa
https://documenter.getpostman.com/view/18246564/2sA3QqfYLy

### Documentacion postman con lo solicitado EV 2
https://documenter.getpostman.com/view/18246564/2sA3QqhZEa


### Una API que me permita obtener todos los productos activos existentes
api/products/

### Una API que me permita ingresar 1 o más productos a un carro de compras
api/cart/add/

### Una API que me permita pagar el carro de compras y finalizar mi pedido
api/orders/finalize/






### Test
### Como ejecutar el test
- Para ejecutar el test se debe abrir un CMD en la ruta del proyecto "FERREMAS\ferremas"
-se debe ejecutar el siguiente comando 

```bash
# Para ejecutar todas las pruebas
pytest

```
### ejemplo de ubicacion de test para cada componente

ferremas/
│
├── apps/
│   ├── Componente/
│   │   ├── tests/
│   │   │   ├── unit/
│   │   │   │   ├── test_unit_componente.py
│   │   │   │   └── ...
│   │   │   ├── integration/
│   │   │   │   ├── test_integration_componente.py
│   │   │   │   └── ...
│   │   │   └── ...
│   │   └── ...
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md


### Integracion de plataformas 005V

### Integrantes:

Alejandro Yañez Almendras

Daniel Stari Zúñiga

Italo Navarrete Rojas
