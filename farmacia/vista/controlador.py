from farmacia.modelo.persona import Persona
from farmacia.modelo.estanteria import Estanteria
from farmacia.modelo.medicamentoRecetado import MedicamentoRecetado
from farmacia.modelo.medicamentoVentaLibre import MedicamentoVentaLibre
from farmacia.modelo.cosmeticoPremium import CosmeticoPremium
from farmacia.modelo.cosmeticoBasico import CosmeticoBasico
from farmacia.modelo.medicamento import Medicamento


class ControladorFarmacia:
    SUBTIPOS_POR_CATEGORIA = {
        "Medicamento": ("Recetado", "VentaLibre"),
        "Cosmetico": ("Premium", "Basico"),
    }

    def __init__(self):
        self.estanteria = Estanteria()

    def crear_cliente(self, nombre, edad_texto):

        try:
            edad = int(edad_texto)

        except (ValueError, TypeError):
            raise ValueError("La edad debe ser un número entero.")

        cliente = Persona(nombre, edad)

        return cliente

    def crear_producto(self, categoria, subtipo, precio_texto, adicional_texto=0):
        if categoria not in self.SUBTIPOS_POR_CATEGORIA:
            raise ValueError("Seleccione una categoría válida.")
        if subtipo not in self.SUBTIPOS_POR_CATEGORIA[categoria]:
            raise ValueError("Seleccione un subtipo válido para la categoría.")

        try:
            precio = float(precio_texto)
            adicional = float(adicional_texto) if str(adicional_texto).strip() else 0.0
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


    def confirmar_producto(self, producto, cliente):

        ## Comprobar la edad para comprar medicamentos
        if isinstance(producto, Medicamento):

            if cliente.get_edad() < 18:
                raise ValueError(
                    "El cliente debe tener al menos 18 años "
                    "para comprar medicamentos."
                )

        ## Almacenar el producto si cumple las condiciones
        self.estanteria.almacenar_producto(producto)

        return producto.ubicacion