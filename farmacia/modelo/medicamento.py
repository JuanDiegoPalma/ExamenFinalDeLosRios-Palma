from .producto import Producto


class Medicamento(Producto):
    def __init__(self, precio_base, ubicacion=None, importe_adicional=0):
        super().__init__(
            "Medicamento",
            precio_base,
            ubicacion,
            importe_adicional,
        )

    def calcular_precio(self, extra=0):
        return super().calcular_precio(extra) + self.importe_adicional

    def texto(self):
        descripcion = super().texto()
        if self.importe_adicional > 0:
            descripcion += f" + importe adicional {self.importe_adicional}"
        return descripcion
    
    def generar_ubicacion(self, fila, columna):
        ubicacion = super().generar_ubicacion(fila, columna)
        return f"Medicamento ubicado en {ubicacion}"
    
    def __str__(self):
        return f"Medicamento(precio_base={self.precio_base}, ubicacion='{self.ubicacion}', importe_adicional={self.importe_adicional})"
