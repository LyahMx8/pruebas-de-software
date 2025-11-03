class CarritoCompras:
    def __init__ (self, nombreProducto, cantidad, precio=0):
        self.nombreProducto = nombreProducto
        self.cantidad = cantidad
        self.precio = precio

    carrito = []

    def agregarProducto(self, nombreProducto, cantidad, precio):
        if cantidad <= 0:
            raise ValueError("Debes agregar más de un producto")
        else:
            for i, producto in enumerate(self.carrito):
                if producto.get("nombreProducto") == nombreProducto:
                    self.carrito[i].cantidad += cantidad
                    break
                else:
                    self.carrito.append({nombreProducto,cantidad,precio})

    def eliminarProducto(self, nombreProducto):
        for i, producto in enumerate(self.carrito):
            if producto.get("nombreProducto") == nombreProducto:
                self.carrito.pop(i)
                break

    def consultarTotal(self):
        total = 0
        for i, producto in enumerate(self.carrito):
            total += producto.cantidad

