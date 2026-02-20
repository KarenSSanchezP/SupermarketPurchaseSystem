from .menu_base import MenuBase
from supermarket_app.src.services.producto_service import ProductoService

class MenuCliente(MenuBase):
    def __init__(self, usuario_logueado):
        super().__init__()
        self.usuario = usuario_logueado
        self.producto_service = ProductoService()
        self.opciones = [
            "1. Comprar productos",
            "2. Ver facturas pasadas",
            "3. Actualizar mis datos",
            "4. Cerrar sesión",
        ]
    
    def mostrar(self):
        """
        Bucle principal del menu Cliente
        """
        while True:
            self.mostrar_encabezado(f"Panel de cliente - {self.usuario.username}", 40)
            
            for opcion in self.opciones:
                print(f"\t{opcion}")
            
            seleccion = self.pedir_opcion(self.opciones)
            
            if seleccion == "1":
                self.comprar_productos()
            elif seleccion == "2":
                self.ver_facturas()
            elif seleccion == "3":
                self.actualizar_datos()
            elif seleccion == "4":
                print("-" * 43)
                print("Cerrando sesión del cliente...\n")
                self.pausa(2)
                self.limpiar_consola()
                break
            else:
                print("Opción no válida. Vuelve a intentarlo.")
                self.pausa(2)
                self.limpiar_consola()
    
    def comprar_productos(self):
        """
        Permite comprar productos del sistema
        """
        self.mostrar_encabezado("Comprar productos", 40, simbolo="-", es_salto_de_linea=True)
        print("En construcción...")
        self.continuar()
        self.limpiar_consola()
    
    def ver_facturas(self):
        """
        Permite ver las facturas del cliente
        """
        self.mostrar_encabezado("Ver facturas pasadas", 40, simbolo="-", es_salto_de_linea=True)
        print("En construcción...")
        self.continuar()
        self.limpiar_consola()
    
    def actualizar_datos(self):
        """
        Permite actualizar los datos del cliente
        """
        self.mostrar_encabezado("Actualizar mis datos", 40, simbolo="-", es_salto_de_linea=True)
        print("En construcción...")
        self.continuar()
        self.limpiar_consola()