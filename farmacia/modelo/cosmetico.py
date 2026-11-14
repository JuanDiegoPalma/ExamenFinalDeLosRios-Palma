from .producto import Producto


class Cosmetico(Producto):
    def __init__(self, precio_base, ubicacion=None, importe_adicional=0):
        super().__init__(
            "Cosmetico",
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

    def __str__(self):
        return (
            f"Cosmetico(precio_base={self.precio_base}, "
            f"ubicacion='{self.ubicacion}', "
            f"importe_adicional={self.importe_adicional})"
        )

    def __repr__(self):
        return (
            f"Cosmetico(precio_base={self.precio_base}, "
            f"ubicacion='{self.ubicacion}', "
            f"importe_adicional={self.importe_adicional})"
        )