from supermarket_app.src.repositories.producto_repo import ProductoRepository
from supermarket_app.src.models.productos.producto import Producto

class ProductoService:
    def __init__(self):
        self.producto_repo = ProductoRepository()
        
    def listar_todos_los_productos(self):
        """
        Retorna una lista de todos los productos en el sistema
        """
        try:
            listado_productos = self.producto_repo.obtener_todos_los_productos()
            if not listado_productos:
                raise ValueError("No hay productos en el sistema")
            
            productos_activos = [p for p in listado_productos if p.activo]
            
            if not productos_activos:
                raise ValueError("No hay productos disponibles (todos están inactivos)")
            
            return productos_activos
        except Exception as e:
            raise e
    
    def crear_producto(self, nombre, precio, stock, categoria, descripcion):
        """
        Crea un nuevo producto en el sistema
        """
        try:
            nuevo_id = self.producto_repo.obtener_siguiente_id()
            
            if self.producto_repo.buscar_producto_por_nombre(nombre):
                raise ValueError("Ya existe un producto con ese nombre")
            
            nuevo_producto = Producto(nuevo_id, nombre, precio, stock, categoria, descripcion, True)
            self.producto_repo.guardar_producto(nuevo_producto)
            
            return nuevo_producto
        except Exception as e:
            raise e
    
    def eliminar_producto(self, product_id_a_eliminar):
        """
        Elimina un producto del sistema (Solo lo marca como inactivo)
        """
        try:
            producto_a_eliminar = self.producto_repo.buscar_producto_por_id(product_id_a_eliminar)
            
            if not producto_a_eliminar:
                raise ValueError("Producto no encontrado")
            producto_a_eliminar.activo = False
            
            self.producto_repo.actualizar_producto(producto_a_eliminar)
        except Exception as e:
            raise e
    
    def actualizar_producto(self, producto_actualizado):
        """
        Actualiza un producto existente en el sistema
        """
        try:
            if not self.producto_repo.buscar_producto_por_id(producto_actualizado.product_id):
                raise ValueError("Producto no encontrado")
            
            self.producto_repo.actualizar_producto(producto_actualizado)
        except Exception as e:
            raise e