import unittest
from cuenta-bancaria import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):
    def setUp(self):
        self.cuenta = CuentaBancaria("Juan Perez", 100) 
    
    def test_depositar(self):
        self.cuenta.depositar(50)

if __name__ == '__main__':
    unittest.main()