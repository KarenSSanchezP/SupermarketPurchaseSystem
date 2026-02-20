from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, user_id, nombres, apellidos, password, rol, es_primer_ingreso, username=None):
        self._user_id = user_id
        self._nombres = nombres
        self._apellidos = apellidos
        self._password = password
        self._rol = rol
        self._es_primer_ingreso = es_primer_ingreso
        
        if username:
            self._username = username
        else:
            self._username = self.generar_username()
    
    # Getters y setters de propiedades privadas 
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def nombres(self):
        return self._nombres
    
    @property
    def apellidos(self):
        return self._apellidos
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, nueva_clave):
        if len(nueva_clave) < 6:
            raise ValueError("La clave debe tener al menos 6 caracteres.")
        self._password = nueva_clave
    
    @property
    def es_primer_ingreso(self):
        return self._es_primer_ingreso
    
    @es_primer_ingreso.setter
    def es_primer_ingreso(self, valor):
        self._es_primer_ingreso = bool(valor)
    
    @property
    def rol(self):
        return self._rol
    
    @rol.setter
    def rol(self, nuevo_rol):
        if nuevo_rol not in ('admin', 'cliente'):
            raise ValueError("El rol debe ser 'admin' o 'cliente'")
        self._rol = nuevo_rol
    
    def generar_username(self):
        """
        Genera un nombre de usuario combinando las iniciales del 
        de los apellidos con el ID del usuario
        Ejemplo: Juan Ernesto Martinez Pérez con ID 5 -> MP5
        """
        apellido1, apellido2 = self._apellidos.split(' ')
        inicial_ape1 = apellido1[0]
        inicial_ape2 = apellido2[0]
        return f"{inicial_ape1}{inicial_ape2}{self._user_id}"
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, nuevo_username):
        if len(nuevo_username) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
        self._username = nuevo_username
    
    def __str__(self):
        return f"[{self._rol}] {self._nombres} {self._apellidos} (User: {self._username})"