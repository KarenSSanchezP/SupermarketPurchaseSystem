from supermarket_app.src.services.auth_service import AuthService
from supermarket_app.src.ui.menu import Menu

def prueba_rapida():
    print("--- INICIANDO PRUEBA DE REGISTRO ---")
    
    servicio_auth = AuthService()
    
    try:
        print("Registrando cliente...")
        cliente = servicio_auth.registrar_cliente("Juan", "Perez", "123456")
        
        print(f"EXITO: Se creo el objeto cliente: {cliente}")
        print("Revisar el archivo CSV en /data/usuarios.csv")
        
    except Exception as e:
        print(f"ERROR: {e}")
        
    
def prueba_login():
    servicio_auth = AuthService()
    print("--- BIENVENIDO AL SUPERMERCADO ---")
    
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    try:
        usuario_logueado = servicio_auth.login(usuario, contraseña)
        
        print("\nLOGIN EXITOSO")
        print(f"Has entrado como {usuario_logueado.username}")
    
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    # menu = Menu()
    # menu.mostrar_menu_principal()
    
    # prueba_rapida()
    
    prueba_login()