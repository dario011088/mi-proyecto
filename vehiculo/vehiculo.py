class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad

    def avanzar(self):
        print(f"{self.tipo} avanzando a {self.velocidad} km/h")
