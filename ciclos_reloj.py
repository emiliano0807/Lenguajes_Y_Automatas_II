import time
import os

def funcion_prueba():
    suma = 0
    for i in range(10**6):  # Bucle que consume CPU
        suma += i
    return suma

# Obtener el tiempo de CPU antes de ejecutar la función
inicio_cpu = os.times().user
inicio_reloj = time.perf_counter()

# Ejecutar la función
funcion_prueba()

# Obtener el tiempo de CPU después de la ejecución
fin_cpu = os.times().user
fin_reloj = time.perf_counter()

# Calcular ciclos de reloj (aproximados en tiempo de CPU)
ciclos_cpu = (fin_cpu - inicio_cpu) * 10**9  # Convertir a nanosegundos
ciclos_reloj = (fin_reloj - inicio_reloj) * 10**9  # Medición de reloj

print(f"Ciclos de CPU (nanosegundos gastados en CPU): {ciclos_cpu:.2f} ns")
print(f"Ciclos de reloj total (nanosegundos): {ciclos_reloj:.2f} ns")
