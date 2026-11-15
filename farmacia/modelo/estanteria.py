from .producto import Producto


class Estanteria:
    FILAS = 5
    COLUMNAS = 10
    CAPACIDAD_MAXIMA = FILAS * COLUMNAS

    def __init__(self):
        self.matriz = [
            [None for _ in range(self.COLUMNAS)]
            for _ in range(self.FILAS)
        ]

    def buscar_espacio_libre(self):
        for fila in range(self.FILAS):
            for columna in range(self.COLUMNAS):
                if self.matriz[fila][columna] is None:
                    return fila, columna
        return None

    def almacenar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden almacenar productos.")
        
## Evita almacenar el mismo producto mas de una vez 
        for fila_actual in self.matriz:
            for producto_actual in fila_actual:
                if producto_actual is producto:
                    raise ValueError("El producto ya está almacenado.")
        
        posicion_libre = self.buscar_espacio_libre()
        if posicion_libre is None:
            raise OverflowError("La estantería está llena.")

        fila, columna = posicion_libre
        producto.generar_ubicacion(fila, columna)
        self.matriz[fila][columna] = producto
        return posicion_libre

    @property
    def cantidad_ocupados(self):
        return sum(
            producto is not None
            for fila in self.matriz
            for producto in fila
        )

    @property
    def espacios_libres(self):
        return self.CAPACIDAD_MAXIMA - self.cantidad_ocupados

    @property
    def productos_almacenados(self):
        return [
            producto
            for fila in self.matriz
            for producto in fila
            if producto is not None
        ]

    @property
    def estado_posiciones(self):
        return [
            [
                "Ocupada" if producto is not None else "Libre"
                for producto in fila
            ]
            for fila in self.matriz
        ]
