from .cosmetico import Cosmetico

class CosmeticoBasico(Cosmetico):
    def __init__(self, precio_base, ubicacion= None, importe_adicional=0):
        super().__init__(precio_base, ubicacion, importe_adicional)
        self.subtipo= "Básico"

    def calcular_precio(self, extra=0):
        return self.precio_base * 0.90 + extra

    def texto(self):
        return "Cosmético Básico"