# RSE API CLIENT

Este es un módulo para interactuar con la API RSE. Es una implementación básica para simplemente agregar el módulo, instalar las dependencias, agregar los valores correspondienetes en el archivo .env para luego hacer uso de la funcionalidad.

## Instalación

### 1. Crear y Activar un Entorno Virtual

Primero, crea y activa un entorno virtual:

```bash
# Crear un entorno virtual
python -m venv venv
```

```bash
# Activar el entorno virtual (Windows)
venv\Scripts\activate
```

```bash
# Activar el entorno virtual (MacOS/Linux)
source venv/bin/activate
```

```bash
# Desactivar el entorno virtual (Windows)
deactivate
```

### 2. Instala las dependencias

Las dependencias que se instalarán son:
* requests
* python-dotenv

Para ello ejecuta el siguiente comando:
```bash
pip install .
```

## Configuración

Ejecuta el siguiente comando o copia tu editor el archivo .env.example y renombralo .env

Dentro estan los valores que se necesitan para realizar las peticiones RSE API.

### Comando
```bash
cp .env.example .env
```

### Valores dentro de .env.example 
En tu nuevo archivo .env, cambia por los que correspondan. Esto es lo básico la idea sería ir agregando los endpoints que necesites para luego pasarle a la función para realizar la petición.

```bash
URL=https://api.rse.example.com
USERNAME=tu_usuario
PASSWORD=tu_clave
ENDPOINT_JOBS=jobs
```

## Uso del Módulo
Para hacer uso del módulo en cualquier script de Python y especificar el endpoint que deseen:

from rse_api_client import RSEAPIClient

```python
client = RSEAPIClient()
response = client.make_request('get', 'jobs')
print("Response:", data)
```

## Ejecutar Test
```bash
python -m unittest discover -s tests
```