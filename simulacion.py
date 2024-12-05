from time import sleep

class Simulacion:
    def __init__(self, semaforo, vehiculos):
        self.semaforo = semaforo
        self.vehiculos = vehiculos

    def iniciar(self):
        # Ciclo de simulación (puedes ajustar este ciclo más tarde)
        for _ in range(5):
            print("Simulando...")
            for vehiculo in self.vehiculos:
                if self.semaforo.estado == "verde":
                    vehiculo.avanzar()
                else:
                    print(f"{vehiculo.tipo} detenido por el semáforo {self.semaforo.estado}")
            sleep(1)
            # Cambiar el semáforo entre verde y rojo
            self.semaforo.cambiar_estado("verde" if self.semaforo.estado == "rojo" else "rojo")
