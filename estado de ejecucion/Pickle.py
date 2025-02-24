import pickle
import os

# Definir la clase que representa el estado de la aplicación
class EstadoAplicacion:
    def __init__(self, contador=0):
        self.contador = contador

    def incrementar(self):
        self.contador += 1

    def __str__(self):
        return f"Contador: {self.contador}"

# Función para guardar el estado en un archivo
def guardar_estado(estado, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(estado, archivo)

# Función para cargar el estado desde un archivo
def cargar_estado(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            return pickle.load(archivo)
    else:
        return EstadoAplicacion()  # Estado inicial si no existe el archivo

# Nombre del archivo de checkpoint
archivo_checkpoint = 'estado_app.pkl'

# Cargar el estado existente o crear uno nuevo
estado = cargar_estado(archivo_checkpoint)
print("Estado inicial:", estado)

# Simular la ejecución de la aplicación
try:
    for _ in range(5):
        estado.incrementar()
        print("Estado actualizado:", estado)
        # Guardar el estado después de cada incremento
        guardar_estado(estado, archivo_checkpoint)
except Exception as e:
    print("Ocurrió un error:", e)
    # Guardar el estado en caso de excepción
    guardar_estado(estado, archivo_checkpoint)
