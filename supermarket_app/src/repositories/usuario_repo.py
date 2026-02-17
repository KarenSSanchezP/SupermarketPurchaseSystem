import csv
import os
from src.models.usuarios.cliente import Cliente
from src.models.usuarios.admin import Admin

class UsuarioRepository:
    def __init__(self):
        self.archivo = 'supermarket_app/data/usuarios.csv'
        
    def obtener_siguiente_id(self):
        """
        Lee el archivo CSV, encuentra el ID más alto y lo retorna + 1
        """
        if not os.path.exists(self.archivo):
            raise FileNotFoundError(f"Archivo {self.archivo} no encontrado")
        
        id_max = 0
        try:
            with open(self.archivo, 'r') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    id_actual = int(linea['user_id'])
                    if id_actual > id_max:
                        id_max = id_actual
        except (ValueError, IndexError):
            raise ValueError("Error al leer el archivo CSV")
        
        return id_max + 1
    
    def guardar_usuario(self, usuario):
        """
        Guarda un nuevo usuario en el archivo CSV
        """
        pass