import os, csv
from supermarket_app.src.models.productos.producto import Producto

class ProductoRepository():
    def __init__(self):
        self.archivo = 'supermarket_app/data/productos.csv'
        os.makedirs(os.path.dirname(self.archivo), exist_ok=True)
        
    def obtener_todos_los_productos(self):
        """
        Lee el archivo CSV y retorna una lista de productos
        """
        if not os.path.exists(self.archivo):
            return [] # Si el archivo no existe, no hay productos
        
        productos = []
        try:
            with open(self.archivo, 'r', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    es_activo = linea['activo'] == 'True'
                    producto = Producto(linea['product_id'], linea['nombre'], linea['precio'], linea['stock'], 
                                        linea['categoria'], linea['descripcion'], es_activo)
                    productos.append(producto)
            return productos
        except Exception as e:
            raise e
        
    def obtener_siguiente_id(self):
        """
        Lee el archivo CSV, encuentra el ID más alto y lo retorna
        incrementado en 1 para asignar al nuevo producto
        """
        if not os.path.exists(self.archivo):
            return 1  # Si el archivo no existe, el primer ID será 1
                
        id_max = 0
        try:
            with open(self.archivo, 'r', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    id_actual = int(linea['product_id'])
                    if id_actual > id_max:
                        id_max = id_actual
        except Exception:
            # Si hay un error al leer el archivo, no hay productos, 
            # el primer ID será 1
            return 1  
        
        return id_max + 1
    
    def guardar_producto(self, producto):
        """
        Guarda un nuevo producto en el archivo CSV
        """
        columnas = ['product_id', 'nombre', 'precio', 'stock', 'categoria', 'descripcion', 'activo']
        archivo_existe = os.path.exists(self.archivo)
        archivo_existe_vacio = os.path.getsize(self.archivo) == 0 if archivo_existe else True
        
        with open(self.archivo, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=columnas)
            if not archivo_existe or archivo_existe_vacio:
                writer.writeheader()
                
            linea = {
                'product_id': producto.product_id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'stock': producto.stock,
                'categoria': producto.categoria,
                'descripcion': producto.descripcion,
                'activo': producto.activo
                }
            writer.writerow(linea)
        
    def actualizar_producto(self, producto_actualizado):
        """
        Actualiza un producto existente en el archivo CSV
        """
        columnas = ['product_id', 'nombre', 'precio', 'stock', 'categoria', 'descripcion', 'activo']
        productos = []
        
        try:
            with open(self.archivo, 'r', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    if str(linea['product_id']) == str(producto_actualizado.product_id):
                        linea['nombre'] = producto_actualizado.nombre
                        linea['precio'] = producto_actualizado.precio
                        linea['stock'] = producto_actualizado.stock
                        linea['categoria'] = producto_actualizado.categoria
                        linea['descripcion'] = producto_actualizado.descripcion
                        linea['activo'] = producto_actualizado.activo
                    productos.append(linea)
            
            with open(self.archivo, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.DictWriter(archivo, fieldnames=columnas)
                writer.writeheader()
                for linea in productos:
                    writer.writerow(linea)
        except Exception as e:
            raise e
    
    def buscar_producto_por_id(self, product_id_buscado):
        """
        Busca un producto en el archivo CSV por su ID
        Retorna la linea del archivo CSV o None si no existe
        """
        if not os.path.exists(self.archivo):
            return None # Si el archivo no existe, no hay productos
        
        try:
            with open(self.archivo, 'r', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    if linea['product_id'] == product_id_buscado:
                        es_activo = linea['activo'] == 'True'
                        producto = Producto(linea['product_id'], linea['nombre'], linea['precio'], linea['stock'], 
                                            linea['categoria'], linea['descripcion'], es_activo)
                        return producto
            return None
        except (ValueError, IndexError):
            raise ValueError("Error al leer el archivo CSV")
    
    def buscar_producto_por_nombre(self, nombre_buscado):
        """
        Busca un producto en el archivo CSV por su nombre
        Retorna la linea del archivo CSV o None si no existe
        """
        if not os.path.exists(self.archivo):
            return None # Si el archivo no existe, no hay productos
        
        try:
            with open(self.archivo, 'r', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for linea in reader:
                    if linea['nombre'] == nombre_buscado:
                        es_activo = linea['activo'] == 'True'
                        producto = Producto(linea['product_id'], linea['nombre'], linea['precio'], linea['stock'], 
                                            linea['categoria'], linea['descripcion'], es_activo)
                        return producto
            return None
        except (ValueError, IndexError):
            raise ValueError("Error al leer el archivo CSV")