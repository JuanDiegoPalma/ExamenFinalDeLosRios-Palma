import tkinter as tk
from tkinter import ttk, messagebox

from farmacia.modelo import producto
from farmacia.vista.controlador import ControladorFarmacia


class InterfazFarmacia:

    def __init__(self, ventana):
        self.ventana = ventana
        self.controlador = ControladorFarmacia()
        self.producto_pendiente = None
        self.datos_calculados = None

        self.ventana.title("Sistema de Farmacia")
        self.ventana.geometry("800x600")

        formulario = ttk.Frame(self.ventana, padding=20)
        formulario.pack(fill="both", expand=True)

        ttk.Label(
            formulario,
            text="Sistema de ventas - Farmacia",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        ## Datos del cliente
        ttk.Label(formulario, text="Nombre del cliente:").pack()
        self.entrada_nombre = ttk.Entry(formulario)
        self.entrada_nombre.pack(fill="x")

        ttk.Label(formulario, text="Edad:").pack()
        self.entrada_edad = ttk.Entry(formulario)
        self.entrada_edad.pack(fill="x")

        ## Selección del producto
        ttk.Label(formulario, text="Categoría:").pack()
        self.combo_categoria = ttk.Combobox(
            formulario,
            values=list(self.controlador.SUBTIPOS_POR_CATEGORIA),
            state="readonly"
        )
        self.combo_categoria.pack(fill="x")
        self.combo_categoria.bind("<<ComboboxSelected>>", self.actualizar_subtipos)

        ttk.Label(formulario, text="Subtipo:").pack()
        self.combo_subtipo = ttk.Combobox(
            formulario,
            state="disabled"
        )
        self.combo_subtipo.pack(fill="x")
        self.combo_subtipo.bind("<<ComboboxSelected>>", self.invalidar_calculo)

        ttk.Label(formulario, text="Precio base:").pack()
        self.entrada_precio = ttk.Entry(formulario)
        self.entrada_precio.pack(fill="x")

        ttk.Label(formulario, text="Importe adicional:").pack()
        self.entrada_adicional = ttk.Entry(formulario)
        self.entrada_adicional.insert(0, "0")
        self.entrada_adicional.pack(fill="x")

        ## Resultado del cálculo
        self.resultado = tk.StringVar(value="Precio final: -")

        ## Invalidar el cálculo cuando el usuario modifica un campo
        for entrada in (
            self.entrada_nombre,
            self.entrada_edad,
            self.entrada_precio,
            self.entrada_adicional
        ):
            entrada.bind("<KeyRelease>", self.invalidar_calculo)

        ## Botón para calcular el precio
        ttk.Button(
            formulario,
            text="Calcular precio",
            command=self.calcular_precio
        ).pack(pady=12)

        ## Botón para confirmar la compra
        ttk.Button(
            formulario,
            text="Confirmar compra",
            command=self.confirmar_compra
        ).pack(pady=8)

        ## Botón para limpiar el formulario
        ttk.Button(
            formulario,
            text="Limpiar formulario",
            command=self.limpiar_formulario
        ).pack(pady=8)

        ttk.Label(
            formulario,
            textvariable=self.resultado,
            font=("Arial", 12, "bold")
        ).pack()
        ## Botón para abrir la ventana de estantería
        ttk.Button(
            formulario,
            text="Abrir estantería",
            command=self.mostrar_estanteria
        ).pack(pady=8)

    def obtener_datos_formulario(self):
        return (
            self.entrada_nombre.get(),
            self.entrada_edad.get(),
            self.combo_categoria.get(),
            self.combo_subtipo.get(),
            self.entrada_precio.get(),
            self.entrada_adicional.get()
        )

    def actualizar_subtipos(self, evento=None):
        categoria = self.combo_categoria.get()
        self.combo_subtipo.configure(
            values=self.controlador.SUBTIPOS_POR_CATEGORIA.get(categoria, ()),
            state="readonly" if categoria else "disabled"
        )
        self.combo_subtipo.set("")
        self.invalidar_calculo()


    def invalidar_calculo(self, evento=None):
        self.producto_pendiente = None
        self.datos_calculados = None
        self.resultado.set("Precio final: -")

    def calcular_precio(self):
        try:
            producto = self.controlador.crear_producto(
                self.combo_categoria.get(),
                self.combo_subtipo.get(),
                self.entrada_precio.get(),
                self.entrada_adicional.get()
            )

            precio_final = producto.calcular_precio(
                producto.importe_adicional
            )

            self.producto_pendiente = producto
            self.datos_calculados = self.obtener_datos_formulario()
            self.resultado.set(f"Precio final: ${precio_final:.2f}")

        except (ValueError, TypeError) as error:
            self.producto_pendiente = None
            self.datos_calculados = None
            self.resultado.set("Precio final: -")
            messagebox.showerror("Datos incorrectos", str(error))

    def confirmar_compra(self):

        if self.producto_pendiente is None:
            messagebox.showwarning(
                "Atención",
                "Primero debe calcular el precio del producto."
            )
            return

        if self.datos_calculados != self.obtener_datos_formulario():

            self.invalidar_calculo()

            messagebox.showwarning(
                "Datos modificados",
                "Los datos cambiaron después del cálculo. "
                "Calculá nuevamente antes de confirmar."
            )

            return


        try:
            cliente = self.controlador.crear_cliente(
                self.entrada_nombre.get(),
                self.entrada_edad.get()
            )

            producto = self.producto_pendiente

            ubicacion = self.controlador.confirmar_producto(producto)

            precio_final = producto.calcular_precio(
                producto.importe_adicional
            )

            messagebox.showinfo("Compra confirmada",
                f"Cliente: {cliente.get_nombre()}\n"
                f"Edad: {cliente.get_edad()}\n"
                f"Categoría: {producto.tipo}\n"
                f"Subtipo: {producto.subtipo}\n"
                f"Precio base: ${producto.precio_base:.2f}\n"
                f"Importe adicional: ${producto.importe_adicional:.2f}\n"
                f"Precio final: ${precio_final:.2f}\n"
                f"Descripción: {producto.texto()}\n"
                f"Ubicación: {ubicacion}")

            self.producto_pendiente = None
            self.datos_calculados = None

        except (ValueError, TypeError, OverflowError) as error:
            messagebox.showerror(
                "Error al confirmar",
                str(error)
            )
    ## Método para limpiar el formulario
    def limpiar_formulario(self):

        # Limpiar datos del cliente
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_edad.delete(0, tk.END)

        # Reiniciar selección
        self.combo_categoria.set("")
        self.actualizar_subtipos()

        # Limpiar precios
        self.entrada_precio.delete(0, tk.END)
        self.entrada_adicional.delete(0, tk.END)
        self.entrada_adicional.insert(0, "0")

        # Reiniciar resultado
        self.resultado.set("Precio final: -")
        self.producto_pendiente = None
        self.datos_calculados = None
        # Posicionar el cursor
        self.entrada_nombre.focus_set()

    ## Método para abrir la estantería de productos
    def mostrar_estanteria(self):

        ventana_estanteria = tk.Toplevel(self.ventana)
        ventana_estanteria.title("Estantería de productos")
        ventana_estanteria.geometry("1050x500")

        ttk.Label(
            ventana_estanteria,
            text="Estado de la estantería",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        marco = ttk.Frame(ventana_estanteria)
        marco.pack(padx=15, pady=10)

        for fila in range(5):
            for columna in range(10):

                producto = self.controlador.estanteria.matriz[fila][columna]

                ubicacion = f"F{fila + 1}-C{columna + 1}"

                if producto is None:
                    texto = f"{ubicacion}\nLibre"
                    color = "#D8F3DC"
                else:
                    precio_final = producto.calcular_precio(producto.importe_adicional)
                    categoria_visible = ("Cosmético"
                    if producto.tipo == "Cosmetico"
                    else producto.tipo
                    )
                    texto = (
                        f"{ubicacion}\n"
                        f"{categoria_visible}\n"
                        f"{producto.subtipo}\n"
                        f"${precio_final:.2f}"
                    )
                    color = "#FFCDD2"

                etiqueta = tk.Label(
                    marco,
                    text=texto,
                    bg=color,
                    fg="#202020",
                    width=11,
                    height=4,
                    relief="solid",
                    borderwidth=1
                )

                etiqueta.grid(
                    row=fila,
                    column=columna,
                    padx=3,
                    pady=3
                )

        ocupados = self.controlador.estanteria.cantidad_ocupados
        libres = self.controlador.estanteria.espacios_libres

        ttk.Label(
            ventana_estanteria,
            text=f"Ocupados: {ocupados} | Libres: {libres}",
            font=("Arial", 12, "bold")
        ).pack(pady=12)

if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = InterfazFarmacia(ventana)
    ventana.mainloop()
