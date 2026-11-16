
import tkinter as tk

from farmacia.vista.interfaz import InterfazFarmacia


def main():
    # Crear la ventana principal
    ventana = tk.Tk()

    # Inicializar el sistema de farmacia
    aplicacion = InterfazFarmacia(ventana)

    # Mantener la ventana abierta
    ventana.mainloop()


if __name__ == "__main__":
    main()
