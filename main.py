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
        
if __name__ == "__main__":
    # menu = Menu()
    # menu.mostrar_menu_principal()
    
    prueba_rapida()