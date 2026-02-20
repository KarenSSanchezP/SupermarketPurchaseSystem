from .menu_base import MenuBase
from supermarket_app.src.services.producto_service import ProductoService

class MenuAdmin(MenuBase):
    def __init__(self, usuario_logueado):
        super().__init__()
        self.usuario = usuario_logueado
        self.producto_service = ProductoService()
        self.opciones = [
            "1. Crear usuario",
            "2. Gestionar productos",
            "3. Informe de productos",
            "4. Cerrar sesión",
        ]
    
    def mostrar(self):
        """
        Bucle principal del menu Admin
        """
        while True:
            self.mostrar_encabezado(f"Panel de administrador - {self.usuario.username}", 40)
            
            for opcion in self.opciones:
                print(f"\t{opcion}")
            
            seleccion = self.pedir_opcion(self.opciones)
            
            if seleccion == "1":
                self.crear_usuario()
            elif seleccion == "2":
                self.gestionar_productos()
            elif seleccion == "3":
                self.informe_productos()
            elif seleccion == "4":
                print("-" * 43)
                print("Cerrando sesión del administrador...")
                self.pausa(2)
                self.limpiar_consola()
                break
            else:
                print("Opción no válida. Vuelve a intentarlo.")
                self.pausa(2)
                self.limpiar_consola()
    
    def crear_usuario(self):
        """
        Permite crear un nuevo usuario
        """
        self.mostrar_encabezado("Crear usuario", 40, simbolo="-", es_salto_de_linea=True)
        print("En construcción...")
        self.continuar()
        self.limpiar_consola()
    
    def gestionar_productos(self):
        """
        Permite gestionar los productos del sistema
        """
        self.mostrar_encabezado("Gestionar productos", 40, simbolo="-", es_salto_de_linea=True)
        print("En construcción...")
        self.continuar()
        self.limpiar_consola()
    
    def informe_productos(self):
        """
        Permite ver los productos del sistema
        """
        self.mostrar_encabezado("Informe de productos", 40, simbolo="-", es_salto_de_linea=True)
        print("En construcción...")
        self.continuar()
        self.limpiar_consola()