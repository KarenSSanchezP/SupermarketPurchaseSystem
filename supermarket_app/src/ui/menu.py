class Menu:
    def __init__(self):
        self.menu_principal = [
            "1. Iniciar sesión",
            "2. Salir"
        ]
    
    def mostrar_menu_principal(self):
        print("=" * 40)
        print("Supermarket Purchase System")
        print("=" * 40)
        
        for opcion in self.menu_principal:
            print(opcion)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            print("Hasta pronto!")
            exit()
        else:
            print("Opción no válida")