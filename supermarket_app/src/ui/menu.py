from supermarket_app.src.services.auth_service import AuthService

class Menu:
    def __init__(self):
        self.opciones_inicio = [
            "1. Iniciar sesión",
            "2. Salir"
        ]
        self.opciones_admin = [
            "1. Ver productos",
            "2. Añadir producto",
            "3. Eliminar producto",
            "4. Salir"
        ]
        self.opciones_cliente = [
            "1. Ver productos",
            "2. Comprar productos",
            "3. Ver carrito",
            "4. Salir"
        ]
    
    def menu_principal(self):
        """
        Muestra el menú principal y maneja la selección del usuario
        """
        while True: # Bucle principal del menú
            print("=" * 40)
            print("Supermarket Purchase System")
            print("=" * 40)
            
            for opcion in self.opciones_inicio:
                print(opcion)
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.inicio_sesion()
            elif opcion == "2":
                print("Hasta pronto!")
                break
            else:
                print("Opción no válida")
    
    def menu_admin(self, usuario_logueado):
        """
        Muestra el menú de administrador y maneja la selección del usuario
        """
        pass
    
    def menu_cliente(self, usuario_logueado):
        """
        Muestra el menú de cliente y maneja la selección del usuario
        """
        pass
    
    def inicio_sesion(self):
        """
        Maneja el proceso de inicio de sesión
        """
        servicio_auth = AuthService()
        while True: # Bucle de inicio de sesión
            try:
                print("\n--- INICIAR SESIÓN ---" 
                    "\nEscriba '0' en usuario para salir del inicio de sesión")
                
                usuario_input = input("Ingrese su usuario: ")
                if usuario_input == "0": return
                contrasena_input = input("Ingrese su contraseña: ")
                
                usuario_logueado = servicio_auth.login(usuario_input, contrasena_input)
                print(f"¡Bienvenido {usuario_logueado.username}!")
                break
            except Exception as e:
                print(f"Error: {e}")
        
        if usuario_logueado.rol == 'admin':
            self.menu_admin(usuario_logueado)
        else:
            if usuario_logueado.es_primer_ingreso:
                print("Es tu primer ingreso, por favor cambia tu contraseña.")
                contrasena_nueva = input("Ingrese una nueva contraseña: ")
                
                servicio_auth.cambiar_contrasena(usuario_logueado, contrasena_nueva)
                print("Contraseña cambiada con éxito.")
            self.menu_cliente(usuario_logueado)