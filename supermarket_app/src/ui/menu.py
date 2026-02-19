import os, time
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
            print("=" * 43)
            print("\tSupermarket Purchase System")
            print("=" * 43)
            
            for opcion in self.opciones_inicio:
                print("\t"+opcion)
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.inicio_sesion()
            elif opcion == "2":
                print("-" * 43)
                print("Gracias por visitarnos. ¡Hasta pronto!\n")
                time.sleep(2)
                break
            else:
                print("Opción no válida")
    
    def menu_admin(self, usuario_logueado):
        """
        Muestra el menú de administrador y maneja la selección del usuario
        """
        while True: # Bucle del menú de administrador
            print("=" * 40)
            print(f"\tPanel de administrador - {usuario_logueado.username}")
            print("=" * 40)
            
            for opcion in self.opciones_admin:
                print("\t" + opcion)
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.menu_admin_ver_productos(usuario_logueado)
            elif opcion == "2":
                self.menu_admin_añadir_producto(usuario_logueado)
            elif opcion == "3":
                self.menu_admin_eliminar_producto(usuario_logueado)
            elif opcion == "4":
                print("-" * 43)
                print("Cerrando sesión del administrador...")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Opción no válida. Vuelve a intentarlo.")
    
    def menu_cliente(self, usuario_logueado):
        """
        Muestra el menú de cliente y maneja la selección del usuario
        """
        while True: # Bucle del menú de cliente
            print("\n" + "=" * 40)
            print(f"\tPanel de cliente - {usuario_logueado.username}")
            print("=" * 40)
            
            for opcion in self.opciones_cliente:
                print("\t" + opcion)
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.menu_cliente_ver_productos(usuario_logueado)
            elif opcion == "2":
                self.menu_cliente_comprar_productos(usuario_logueado)
            elif opcion == "3":
                self.menu_cliente_ver_carrito(usuario_logueado)
            elif opcion == "4":
                print("-" * 43)
                print("Cerrando sesión del cliente...\n")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Opción no válida. Vuelve a intentarlo.")
    
    def inicio_sesion(self):
        """
        Maneja el proceso de inicio de sesión
        """
        servicio_auth = AuthService()
        while True: # Bucle de inicio de sesión
            try:
                print("\n" + "-" * 14 + " INICIAR SESIÓN " + "-" * 14,
                    "\nEscriba '0' en usuario para salir del inicio de sesión")
                
                usuario_input = input(">>> Ingrese su usuario: ")
                if usuario_input == "0": return
                contrasena_input = input(">>> Ingrese su contraseña: ")
                
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