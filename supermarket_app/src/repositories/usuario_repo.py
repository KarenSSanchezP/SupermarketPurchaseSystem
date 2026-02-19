import csv
import os
from supermarket_app.src.models.usuarios.cliente import Cliente
from supermarket_app.src.models.usuarios.admin import Admin
from supermarket_app.src.utils.validaciones import Validaciones

class UsuarioRepository():
    def __init__(self):
        self.archivo = 'supermarket_app/data/usuarios.csv'
        os.makedirs(os.path.dirname(self.archivo), exist_ok=True)
        
    def obtener_siguiente_id(self):
        """
        Lee el archivo CSV, encuentra el ID más alto y lo retorna 
        incrementado en 1 para asignar al nuevo usuario
        """
        if not os.path.exists(self.archivo):
            return 1  # Si el archivo no existe, el primer ID será 1
                
        id_max = 0
        try:
            with open(self.archivo, 'r') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    id_actual = int(linea['user_id'])
                    if id_actual > id_max:
                        id_max = id_actual
        except Exception:
            # Si hay un error al leer el archivo, no hay usuarios, 
            # el primer ID será 1
            return 1  
        
        return id_max + 1
    
    def guardar_usuario(self, usuario):
        """
        Guarda un nuevo usuario en el archivo CSV 
        """
        columnas = ['user_id', 'nombres', 'apellidos', 'password', 
                    'rol', 'es_primer_ingreso', 'username']
        archivo_existe = os.path.exists(self.archivo)
        
        with open(self.archivo, mode='a', newline='') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=columnas)
            if not archivo_existe:
                writer.writeheader()
                
            linea = {
                'user_id': usuario.user_id,
                'nombres': usuario.nombres,
                'apellidos': usuario.apellidos,
                'password': usuario.password,
                'rol': usuario.rol,
                'es_primer_ingreso': usuario.es_primer_ingreso,
                'username': usuario.username
                }
            writer.writerow(linea)
    
    def buscar_usuario(self, username):
        """
        Busca un usuario en el archivo CSV por su username
        """
        Validaciones('usuarios').validar_archivo_existente()
        
        try:
            with open(self.archivo, 'r') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    if linea['username'] == username:
                        if linea['rol'] == 'admin':
                            return Admin(linea['user_id'], linea['username'], linea['password'])
                        else:
                            return Cliente(linea['user_id'], linea['username'], linea['password'])
        except (ValueError, IndexError):
            raise ValueError("Error al leer el archivo CSV")
        
        raise ValueError(f"Usuario {username} no encontrado")
    
    def buscar_usuario_por_username(self, username_buscado):
        """
        Busca un usuario en el archivo CSV por su username
        Retorna la linea del archivo CSV o None si no existe
        """
        if not os.path.exists(self.archivo):
            return None # Si el archivo no existe, no hay usuarios
        
        try:
            with open(self.archivo, 'r') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    if linea['username'] == username_buscado:
                        return linea
            return None
        except (ValueError, IndexError):
            raise ValueError("Error al leer el archivo CSV")