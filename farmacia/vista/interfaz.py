import tkinter as tk
from tkinter import ttk, messagebox

from farmacia.vista.controlador import ControladorFarmacia


class InterfazFarmacia:

    def __init__(self, ventana):
        self.ventana = ventana
        self.controlador = ControladorFarmacia()
        self.producto_pendiente = None

        self.ventana.title("Sistema de Farmacia")
        self.ventana.geometry("550x420")

        formulario = ttk.Frame(self.ventana, padding=20)
        formulario.pack(fill="both", expand=True)

        ttk.Label(
            formulario,
            text="Sistema de ventas - Farmacia",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        # Datos del cliente
        ttk.Label(formulario, text="Nombre del cliente:").pack()
        self.entrada_nombre = ttk.Entry(formulario)
        self.entrada_nombre.pack(fill="x")

        ttk.Label(formulario, text="Edad:").pack()
        self.entrada_edad = ttk.Entry(formulario)
        self.entrada_edad.pack(fill="x")

        # Selección del producto
        ttk.Label(formulario, text="Tipo de producto:").pack()
        self.combo_subtipo = ttk.Combobox(
            formulario,
            values=["Recetado", "VentaLibre", "Premium", "Basico"],
            state="readonly"
        )
        self.combo_subtipo.pack(fill="x")
        self.combo_subtipo.current(0)

        ttk.Label(formulario, text="Precio base:").pack()
        self.entrada_precio = ttk.Entry(formulario)
        self.entrada_precio.pack(fill="x")

        ttk.Label(formulario, text="Importe adicional:").pack()
        self.entrada_adicional = ttk.Entry(formulario)
        self.entrada_adicional.insert(0, "0")
        self.entrada_adicional.pack(fill="x")

        # Resultado del cálculo
        self.resultado = tk.StringVar(value="Precio final: -")

        ttk.Button(
            formulario,
            text="Calcular precio",
            command=self.calcular_precio
        ).pack(pady=12)

        ttk.Label(
            formulario,
            textvariable=self.resultado,
            font=("Arial", 12, "bold")
        ).pack()

    def calcular_precio(self):
        try:
            producto = self.controlador.crear_producto(
                self.combo_subtipo.get(),
                self.entrada_precio.get(),
                self.entrada_adicional.get()
            )

            precio_final = producto.calcular_precio(
                producto.importe_adicional
            )

            self.producto_pendiente = producto
            self.resultado.set(f"Precio final: ${precio_final:.2f}")

        except (ValueError, TypeError) as error:
            self.producto_pendiente = None
            self.resultado.set("Precio final: -")
            messagebox.showerror("Datos incorrectos", str(error))


if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = InterfazFarmacia(ventana)
    ventana.mainloop()
