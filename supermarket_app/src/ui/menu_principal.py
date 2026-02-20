from .menu_base import MenuBase
from .menu_admin import MenuAdmin
from .menu_cliente import MenuCliente
from supermarket_app.src.services.auth_service import AuthService

class MenuPrincipal(MenuBase):
    def __init__(self):
        super().__init__()
        self.opciones = [
            "1. Iniciar sesión",
            "2. Salir"
        ]
    
    def mostrar(self):
        """
        Bucle principal del menu principal
        """
        while True:
            self.mostrar_encabezado("Supermarket Purchase System", 40)
            
            for opcion in self.opciones:
                print(f"\t{opcion}")
            
            seleccion = self.pedir_opcion(self.opciones)
            
            if seleccion == "1":
                self.inicio_sesion()
            elif seleccion == "2":
                print("-" * 43)
                print("Gracias por visitarnos. ¡Hasta pronto!\n")
                self.pausa(2)
                self.limpiar_consola()
                break
            else:
                print("Opción no válida. Vuelve a intentarlo.")
                self.pausa(2)
                self.limpiar_consola()
    
    def inicio_sesion(self):
        """
        Permite iniciar sesión en el sistema
        """
        self.mostrar_encabezado("Iniciar sesión", 40, simbolo="-", es_salto_de_linea=True)
        
        try:
            print("Escriba '0' en usuario para salir del inicio de sesión")
            
            usuario_input = input(">>> Ingrese su usuario: ")
            if usuario_input == "0": 
                self.limpiar_consola()
                return
            contrasena_input = input(">>> Ingrese su contraseña: ")
            
            servicio_auth = AuthService()
            usuario_logueado = servicio_auth.login(usuario_input, contrasena_input)
            print(f"\n\t--- Bienvenido {usuario_logueado.username}! ---")
            self.pausa(1)
            
            if usuario_logueado.rol == 'admin':
                self.limpiar_consola()
                menu_admin = MenuAdmin(usuario_logueado)
                menu_admin.mostrar()
            else:
                if usuario_logueado.es_primer_ingreso:
                    print("-" * 40 + "\nEs tu primer ingreso, por favor cambia tu contraseña.")
                    contrasena_nueva = input(">>> Ingrese una nueva contraseña: ")
                    
                    servicio_auth.cambiar_contrasena(usuario_logueado, contrasena_nueva)
                    print("Contraseña cambiada con éxito.")
                    self.pausa(2)
                
                self.limpiar_consola()
                menu_cliente = MenuCliente(usuario_logueado)
                menu_cliente.mostrar()
        except Exception as e:
            print(f"Error: {e}")
            self.pausa(2)
            self.limpiar_consola()