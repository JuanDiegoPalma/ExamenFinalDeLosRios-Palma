from .medicamento import Medicamento

class MedicamentoRecetado(Medicamento):
    
    def __init__(self, precio_base, ubicacion=None, importe_adicional=0):
        
        super().__init__(precio_base, ubicacion, importe_adicional)
        
        self.subtipo= "Recetado"
    
    def calcular_precio(self, extra=0):
        return self.precio_base * 0.60 + extra
    
    def texto(self):
        return "Medicamento de venta bajo receta"