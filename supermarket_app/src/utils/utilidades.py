import os

class Utilidades:
    def __init__(self, nombre_archivo=None):
        if nombre_archivo:
            self.archivo = f'supermarket_app/data/{nombre_archivo}.csv'
        else:
            self.archivo = None
        
    def validar_archivo_existente(self):
        if not os.path.exists(self.archivo):
            raise FileNotFoundError(f"Archivo {self.archivo} no encontrado")
    
    def validar_nombre(self, nombre):
        if not nombre:
            raise ValueError("Nombre no puede estar vacío")
        
        if len(nombre) > 50:
            raise ValueError("El nombre debe tener 50 caracteres como máximo")
    
    def validar_apellidos(self, apellidos):
        if not apellidos:
            raise ValueError("Apellidos no pueden estar vacíos")
        
        if len(apellidos) > 50:
            raise ValueError("Los apellidos deben tener 50 caracteres como máximo")
    
    def validar_password(self, password):
        if not password:
            raise ValueError("La contraseña no puede estar vacía")
        
        if len(password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        
        if len(password) > 50:
            raise ValueError("La contraseña debe tener 50 caracteres como máximo")
    
    def limpiar_consola(self):
        os.system('cls' if os.name == 'nt' else 'clear')    