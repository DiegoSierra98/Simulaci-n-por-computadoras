import threading
import multiprocessing
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Simulación de tarea I/O-bound con hilos
def io_task(nombre):
    print(f'Hilo {nombre}: Iniciando tarea I/O')
    time.sleep(2)
    print(f'Hilo {nombre}: Tarea I/O completada')

# Simulación de tarea CPU-bound con procesos
def cpu_task(n):
    print(f'Proceso {n}: Calculando...')
    return sum(i * i for i in range(10**6))

# Función para demonio
def demonio_task():
    while True:
        print("Demonio: Ejecutando en segundo plano...")
        time.sleep(1)

# Función asincrónica para asyncio
async def tarea_asincrona(id):
    print(f'Tarea asincrónica {id}: Iniciando')
    await asyncio.sleep(2)
    print(f'Tarea asincrónica {id}: Completada')

def ejemplo_hilos():
    print("\n=== EJEMPLO CON HILOS ===")
    hilos = [threading.Thread(target=io_task, args=(i,)) for i in range(3)]
    
    for hilo in hilos:
        hilo.start()
    
    for hilo in hilos:
        hilo.join()

def ejemplo_procesos():
    print("\n=== EJEMPLO CON PROCESOS ===")
    with ProcessPoolExecutor() as ejecutor:
        resultados = list(ejecutor.map(cpu_task, range(3)))
    
    print("Resultados de procesos:", resultados)

def ejemplo_demonio():
    print("\n=== EJEMPLO CON DEMONIO ===")
    demonio = threading.Thread(target=demonio_task)
    demonio.daemon = True
    demonio.start()
    
    # Dar tiempo para que el demonio se ejecute
    time.sleep(3)
    print("Hilo principal finalizando (demonio será terminado)")

async def ejemplo_asyncio():
    print("\n=== EJEMPLO CON ASYNCIO ===")
    await asyncio.gather(
        tarea_asincrona(1),
        tarea_asincrona(2),
        tarea_asincrona(3)
    )

if __name__ == "__main__":
    inicio = time.time()

    # Ejecutar todos los ejemplos
    ejemplo_hilos()
    ejemplo_procesos()
    ejemplo_demonio()
    asyncio.run(ejemplo_asyncio())

    print(f"\nTiempo total de ejecución: {time.time() - inicio:.2f} segundos")
