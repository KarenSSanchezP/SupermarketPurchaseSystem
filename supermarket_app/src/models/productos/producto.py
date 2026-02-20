class Producto():
    def __init__(self, product_id, nombre, precio, stock, categoria, descripcion, activo=True):
        self._product_id = product_id
        self._nombre = nombre
        self.precio = precio
        self.stock = stock
        self._categoria = categoria
        self._descripcion = descripcion
        self._activo = activo
    
    # Getters y setters de propiedades privadas 
    @property
    def product_id(self):
        return self._product_id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if float(nuevo_precio) <= 0:
            raise ValueError("El precio debe ser mayor a $0.00")
        self._precio = float(nuevo_precio)
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, nuevo_stock):
        if int(nuevo_stock) < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock = int(nuevo_stock)
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def activo(self):
        return self._activo
    
    @activo.setter
    def activo(self, estado):
        self._activo = bool(estado)
    
    def __str__(self):
        return f"[{self._product_id}] {self._nombre} - Precio: ${self._precio:.2f} - Stock: {self._stock} unidades - Categoria: {self._categoria}"