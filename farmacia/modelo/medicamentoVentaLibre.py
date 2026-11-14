from .medicamento import Medicamento

class MedicamentoVentaLibre(Medicamento):
    def __init__(self, precio_base, ubicacion= None, importe_adicional=0):
        super().__init__(precio_base, ubicacion, importe_adicional)
        self.subtipo= "Venta Libre"

    def calcular_precio(self, extra= 0):
        return self.precio_base + extra

    def texto(self):
        return "Medicamento de Venta Libre"