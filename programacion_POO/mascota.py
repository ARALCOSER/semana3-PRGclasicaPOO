# mascota.py

class Mascota:
    """
    Clase que representa una mascota.
    Contiene atributos básicos y métodos para interactuar.
    """

    def __init__(self, nombre: str, especie: str, edad: int):
        # Abstracción: encapsulamos los datos dentro del objeto
        self.nombre = nombre
        self.especie = especie
        self.edad = self.validar_edad(edad)

    def validar_edad(self, edad):
        """
        Valida que la edad sea un número entero positivo.
        """
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        return edad

    def mostrar_informacion(self):
        """
        Muestra la información de la mascota.
        """
        print("\n--- Información de la Mascota ---")
        print(f"Nombre  : {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad   : {self.edad} años")

    def hacer_sonido(self):
        """
        Simula el sonido de la mascota según su especie.
        """
        sonidos = {
            "perro": "Guau Guau 🐶",
            "gato": "Miau Miau 🐱",
            "ave": "Pío Pío 🐦",
            "pez": "Glup Glup 🐟"
        }

        sonido = sonidos.get(self.especie.lower(), "Sonido desconocido 🤔")
        print(f"{self.nombre} dice: {sonido}")
