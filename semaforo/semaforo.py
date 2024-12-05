class Semaforo:
    def __init__(self):
        self.estado = "rojo"  # Puede ser "rojo", "amarillo", "verde"

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"Semáforo cambiado a {self.estado}")
