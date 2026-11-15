from .cosmetico import Cosmetico

class CosmeticoPremium(Cosmetico):
    def __init__ (self, precio_base, ubicacion= None, importe_adicional=0):
        super().__init__(precio_base, ubicacion, importe_adicional)
        self.subtipo= "Premium"

    def calcular_precio(self, extra=0):
        return self.precio_base * 1.20 + extra

    def texto(self):
        return "Cosmético Premium"