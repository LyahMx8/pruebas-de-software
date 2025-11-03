class CuentaBancaria:
    def __init__ (self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            raise ValueError("La cantidad a depositar debe ser positiva")

    def consultar_saldo(self):
        return self.saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError ("Fondos insuficientes")
        elif cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva")
        else:
            self.saldo -= cantidad

