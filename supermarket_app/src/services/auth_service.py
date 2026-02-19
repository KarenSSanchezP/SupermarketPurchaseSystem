from supermarket_app.src.repositories.usuario_repo import UsuarioRepository
from supermarket_app.src.models.usuarios.cliente import Cliente

class AuthService:
    def __init__(self):
        self.repo = UsuarioRepository()
    
    def login(self, username, password):
        """
        Verifica las credenciales del usuario
        """
        try:
            usuario = self.repo.buscar_usuario_por_username(username)
            if usuario is None:
                raise ValueError("Usuario no encontrado")
            else:
                if usuario.password == password:
                    return usuario
                else:
                    raise ValueError("Contraseña incorrecta")
        except Exception as e:
            raise e
    
    def registrar_cliente(self, nombres, apellidos, password):
        """
        Registra un nuevo cliente en la base de datos
        """
        try:
            nuevo_id = self.repo.obtener_siguiente_id()
            
            nuevo_cliente = Cliente(nuevo_id, nombres, apellidos, password, True)
            self.repo.guardar_usuario(nuevo_cliente)
            
            return nuevo_cliente
        except Exception as e:
            raise e