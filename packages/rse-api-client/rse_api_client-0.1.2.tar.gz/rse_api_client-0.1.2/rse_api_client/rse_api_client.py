import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Desactivar el aviso de solicitud insegura
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RSEAPIClient:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv('URL')
        self.username = os.getenv('USER')
        self.password = os.getenv('PASSWORD')

    def make_request(self, method, endpoint, params=None, data=None):
        # Armado de URL
        url = f"{self.base_url}/{endpoint}"

        # Datos y autenticación
        auth = HTTPBasicAuth(self.username, self.password)

        # Diccionario para almacenar los argumentos
        kwargs = {
            'auth': auth,
            'verify': False
        }

        # Agregar 'data' y 'params' si están presentes
        if data:
            kwargs['json'] = data
        if params:
            kwargs['params'] = params

        # Obtener el método dinámicamente
        try:
            response = getattr(requests, method)(url, **kwargs)
            print(f"Response: {response}")  # Imprimir la respuesta
            return response
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None
