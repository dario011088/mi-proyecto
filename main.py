from vehiculo.vehiculo import Vehiculo
from semaforo.semaforo import Semaforo
from simulacion import Simulacion

def main():
    # Crear semáforo
    semaforo = Semaforo()

    # Crear vehículos
    vehiculos = [Vehiculo("Auto", 1), Vehiculo("Camión", 2)]

    # Iniciar simulación
    simulacion = Simulacion(semaforo, vehiculos)
    simulacion.iniciar()

if __name__ == "__main__":
    main()

