import math
from numbers import Real


class Producto:
    def __init__(
        self,
        tipo,
        precio_base,
        ubicacion=None,
        importe_adicional=0,
    ):
        self.tipo = tipo
        self.set_precio_base(precio_base)
        self.ubicacion = ubicacion if ubicacion is not None else ""
        self.set_importe_adicional(importe_adicional)
        self.fila = None
        self.columna = None

    def set_precio_base(self, precio_base):
        if (
            isinstance(precio_base, bool)
            or not isinstance(precio_base, Real)
            or not math.isfinite(precio_base)
            or precio_base <= 0
        ):
            raise ValueError("El precio base debe ser un número positivo.")
        self.precio_base = precio_base

    def set_importe_adicional(self, importe_adicional):
        if (
            isinstance(importe_adicional, bool)
            or not isinstance(importe_adicional, Real)
            or not math.isfinite(importe_adicional)
            or importe_adicional < 0
        ):
            raise ValueError("El importe adicional debe ser un número no negativo.")
        self.importe_adicional = importe_adicional

    def calcular_precio(self, extra=0):
        return self.precio_base + extra

    def generar_ubicacion(self, fila, columna):
        if (
            isinstance(fila, bool)
            or not isinstance(fila, int)
            or fila < 0
            or isinstance(columna, bool)
            or not isinstance(columna, int)
            or columna < 0
        ):
            raise ValueError("La fila y la columna deben ser enteros no negativos.")
        self.fila = fila
        self.columna = columna
        self.ubicacion = f"F{fila + 1}-C{columna + 1}"
        return self.ubicacion

    def texto(self):
        descripcion = f"{self.tipo}: precio base {self.precio_base}"
        if self.ubicacion:
            descripcion += f", ubicación {self.ubicacion}"
        return descripcion
