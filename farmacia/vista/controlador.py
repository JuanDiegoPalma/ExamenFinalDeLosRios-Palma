from farmacia.modelo.persona import Persona
from farmacia.modelo.estanteria import Estanteria
from farmacia.modelo.medicamentoRecetado import MedicamentoRecetado
from farmacia.modelo.medicamentoVentaLibre import MedicamentoVentaLibre
from farmacia.modelo.cosmeticoPremium import CosmeticoPremium
from farmacia.modelo.cosmeticoBasico import CosmeticoBasico


class ControladorFarmacia:

    def __init__(self):
        self.estanteria = Estanteria()

    def crear_cliente(self, nombre, edad_texto):

        try:
            edad = int(edad_texto)

        except (ValueError, TypeError):
            raise ValueError("La edad debe ser un número entero.")

        cliente = Persona(nombre, edad)

        return cliente
    
    def crear_producto(self, subtipo, precio_texto, adicional_texto=0):
        
        try:
            precio = float(precio_texto)
            adicional= float(adicional_texto)
        except (ValueError, TypeError):
            raise ValueError("El precio y el adicional deben ser números.")
        
        if subtipo == "Recetado":
            producto = MedicamentoRecetado(precio, importe_adicional=adicional)
        
        elif subtipo == "VentaLibre":
            producto = MedicamentoVentaLibre(precio, importe_adicional=adicional)
        
        elif subtipo == "Premium":
            producto = CosmeticoPremium(precio, importe_adicional=adicional)

        elif subtipo == "Basico":
            producto = CosmeticoBasico(precio, importe_adicional=adicional)

        else:
            raise ValueError("El subtipo de producto no es válido.")

        return producto
    
    def confirmar_producto(self, producto):
        self.estanteria.agregar_producto(producto)
        return producto.ubicacion       