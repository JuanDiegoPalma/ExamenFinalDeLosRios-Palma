class Persona:

## Inicialización de atributos

    def __init__(self, nombre, edad):
        self._nombre = ""
        self._edad = 0

        self.set_nombre(nombre)
        self.set_edad(edad)

# Setters y Getters
    def set_nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un texto")
        nombre = nombre.strip()

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")

        if any(character.isdigit() for character in nombre):
            raise ValueError("El nombre no puede contener números")

        self._nombre = nombre

    def get_nombre(self):
        return self._nombre


    def set_edad(self, edad):

        if not isinstance(edad, int) or isinstance(edad, bool):
            raise ValueError("La edad debe ser un número entero")

        if edad <= 0:
            raise ValueError("Edad incorrecta, la edad debe ser mayor a 0")

        if edad < 18:
            raise ValueError("Edad incorrecta, el cliente debe ser mayor de 18 años para registrarse")

        self._edad = edad

    def get_edad(self):
        return self._edad

## Mostrar datos

    def mostrar_datos(self, detallado=False):
        if detallado:
            return f"Nombre: {self._nombre} | Edad: {self._edad} años"
        else:
            return f"{self._nombre}"
