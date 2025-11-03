import unittest
from CarritoCompras import CarritoCompras

class TestCarritoCompras(unittest.TestCase):
    def setUp(self):
        self.cuenta = CarritoCompras("Juan Perez", 100) 
    
    def test_depositar(self):
        self.cuenta.depositar(50)

if __name__ == '__main__':
    unittest.main()