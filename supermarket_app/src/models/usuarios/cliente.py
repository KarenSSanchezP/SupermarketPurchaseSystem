from .usuario import Usuario

class Cliente(Usuario):
    def __init__(self, user_id, nombres, apellidos, password, es_primer_ingreso, username=None):
        super().__init__(user_id, nombres, apellidos, password, 'cliente', es_primer_ingreso, username)
    
    def __str__(self):
        return f"[Cliente] {self._nombres} {self._apellidos} (User: {self._username})"