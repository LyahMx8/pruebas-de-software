import unittest

from carrito_compras import CarritoCompras 

class TestCarritoCompras(unittest.TestCase):
    
    def setUp(self):
        self.carrito = CarritoCompras()
        
        # Productos de ejemplo para los tests
        self.prod_a = {"nombre": "Leche", "cantidad": 2, "precio": 2500}
        self.prod_b = {"nombre": "Pan", "cantidad": 1, "precio": 1200}
        self.prod_c = {"nombre": "Manzanas", "cantidad": 5, "precio": 2500}

    # --- Tests para agregarProducto --
    def test_agregar_producto_nuevo(self):
        """Prueba que un producto se agrega correctamente al carrito."""
        self.carrito.agregarProducto(self.prod_a['nombre'], self.prod_a['cantidad'], self.prod_a['precio'])
        self.assertEqual(len(self.carrito.carrito), 1)
        self.assertEqual(self.carrito.carrito[0]['nombre'], "Leche")
        self.assertEqual(self.carrito.carrito[0]['cantidad'], 2)

    def test_agregar_producto_existente_aumenta_cantidad(self):
        """Prueba que agregar un producto existente aumenta la cantidad."""
        # 1. Agregamos el producto inicial (cantidad 2)
        self.carrito.agregarProducto(self.prod_a['nombre'], self.prod_a['cantidad'], self.prod_a['precio'])
        
        # 2. Agregamos más unidades del mismo producto (cantidad 3)
        self.carrito.agregarProducto(self.prod_a['nombre'], 3, self.prod_a['precio'])
        
        self.assertEqual(len(self.carrito.carrito), 1)
        self.assertEqual(self.carrito.carrito[0]['cantidad'], 5) # 2 + 3 = 5
        
    def test_agregar_cantidad_cero_o_negativa_levanta_error(self):
        """Prueba que agregar cantidad <= 0 levanta un ValueError."""
        with self.assertRaises(ValueError):
            self.carrito.agregarProducto("Agua", 0, 1000)
        with self.assertRaises(ValueError):
            self.carrito.agregarProducto("Agua", -5, 1000)


    # --- Tests para eliminarProducto ---
    def test_eliminar_una_unidad_disminuye_cantidad(self):
        """Prueba que eliminar una unidad disminuye la cantidad si hay más de una."""
        self.carrito.agregarProducto(self.prod_c['nombre'], 5, self.prod_c['precio']) # 5 unidades
        self.carrito.eliminarProducto(self.prod_c['nombre'], 1) # Elimina 1 unidad
        
        self.assertEqual(len(self.carrito.carrito), 1)
        self.assertEqual(self.carrito.carrito[0]['cantidad'], 4) # De 5 pasa a 4

    def test_eliminar_producto_con_cantidad_completa_lo_borra(self):
        """Prueba que eliminar la cantidad total del producto lo borra del carrito."""
        self.carrito.agregarProducto(self.prod_b['nombre'], 1, self.prod_b['precio']) # 1 unidad
        
        # Eliminar la única unidad que existe
        self.carrito.eliminarProducto(self.prod_b['nombre'], 1) 
        
        self.assertEqual(len(self.carrito.carrito), 0) # El carrito queda vacío

    def test_eliminar_producto_con_cantidad_mayor_a_la_existente_lo_borra(self):
        """Prueba que si se intenta eliminar más de lo que hay, se borra el producto."""
        self.carrito.agregarProducto(self.prod_a['nombre'], 2, self.prod_a['precio']) # 2 unidades
        
        # Intenta eliminar 5, pero solo hay 2. Debería borrarlo.
        self.carrito.eliminarProducto(self.prod_a['nombre'], 5)
        
        self.assertEqual(len(self.carrito.carrito), 0)


    # --- Tests para consultarTotal ---
    def test_consultar_total_carrito_vacio_es_cero(self):
        """Prueba que el total es 0 si el carrito está vacío."""
        self.assertEqual(self.carrito.consultarTotal(), 0.0)

    def test_consultar_total_un_producto(self):
        """Prueba el cálculo total con un solo tipo de producto."""
        self.carrito.agregarProducto(self.prod_a['nombre'], 2, 2500) # 2 * 2500 = 5000
        self.assertEqual(self.carrito.consultarTotal(), 5000)

    def test_consultar_total_multiples_productos(self):
        """Prueba el cálculo total con varios tipos de productos."""
        # Leche: 2 * 2500 = 5000
        self.carrito.agregarProducto(self.prod_a['nombre'], self.prod_a['cantidad'], self.prod_a['precio']) 
        # Pan: 1 * 1200 = 1200
        self.carrito.agregarProducto(self.prod_b['nombre'], self.prod_b['cantidad'], self.prod_b['precio']) 
        # Manzanas: 5 * 2500 = 12500
        self.carrito.agregarProducto(self.prod_c['nombre'], self.prod_c['cantidad'], self.prod_c['precio']) 
        
        # Total esperado: 5000 + 1200 + 12500 = 18700
        self.assertEqual(self.carrito.consultarTotal(), 18700)


if __name__ == '__main__':
    unittest.main()