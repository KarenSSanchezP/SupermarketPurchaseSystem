import csv
import os
from supermarket_app.src.models.usuarios.cliente import Cliente
from supermarket_app.src.models.usuarios.admin import Admin
from supermarket_app.src.utils.utilidades import Utilidades

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
            with open(self.archivo, 'r', encoding='utf-8') as archivo:
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
        archivo_existe_vacio = os.path.getsize(self.archivo) == 0 if archivo_existe else True
        
        with open(self.archivo, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=columnas)
            if not archivo_existe or archivo_existe_vacio:
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
    
    def actualizar_usuario(self, usuario_actualizado):
        """
        Actualiza un usuario existente en el archivo CSV
        """
        columnas = ['user_id', 'nombres', 'apellidos', 'password', 
                    'rol', 'es_primer_ingreso', 'username']
        usuarios = []
        
        try:
            with open(self.archivo, 'r', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    if linea['username'] == usuario_actualizado.username:
                        linea['user_id'] = usuario_actualizado.user_id
                        linea['nombres'] = usuario_actualizado.nombres
                        linea['apellidos'] = usuario_actualizado.apellidos
                        linea['password'] = usuario_actualizado.password
                        linea['rol'] = usuario_actualizado.rol
                        linea['es_primer_ingreso'] = usuario_actualizado.es_primer_ingreso
                        linea['username'] = usuario_actualizado.username
                    usuarios.append(linea)
            
            with open(self.archivo, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.DictWriter(archivo, fieldnames=columnas)
                writer.writeheader()
                for linea in usuarios:
                    writer.writerow(linea)
        except Exception as e:
            raise e
    
    def buscar_usuario_por_username(self, username_buscado):
        """
        Busca un usuario en el archivo CSV por su username
        Retorna la linea del archivo CSV o None si no existe
        """
        if not os.path.exists(self.archivo):
            return None # Si el archivo no existe, no hay usuarios
        
        try:
            with open(self.archivo, 'r', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    if linea['username'] == username_buscado:
                        es_primer_ingreso = linea['es_primer_ingreso'] == 'True'
                        if linea['rol'] == 'admin':
                            admin = Admin(int(linea['user_id']), linea['nombres'], linea['apellidos'], 
                                        linea['password'], es_primer_ingreso, linea['username'])
                            return admin
                        else:
                            return Cliente(int(linea['user_id']), linea['nombres'], linea['apellidos'], 
                                        linea['password'], es_primer_ingreso, linea['username'])
            return None
        except (ValueError, IndexError):
            raise ValueError("Error al leer el archivo CSV")