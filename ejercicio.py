import threading
import queue
import time
import random

TOTAL_IMAGENES = 20

cola_imagenes = queue.Queue()
imagenes_procesadas = 0
lock = threading.Lock()
finalizado = threading.Event()

archivo_receptor = open("receptor.txt", "w", encoding="utf-8")
archivo_procesador = open("procesador.txt", "w", encoding="utf-8")

def receptor():
    for i in range(TOTAL_IMAGENES):
        imagen = f"imagen_{i}"
        cola_imagenes.put(imagen)
        archivo_receptor.write(f"Llegó la imagen: {imagen}\n")
        time.sleep(random.choice([
            random.uniform(0.1, 0.4),
            random.uniform(1.5, 2.5)
        ]))
    cola_imagenes.put(None)  # Señal de parada
    archivo_receptor.write("Fin de recepción de imágenes.\n")
    archivo_receptor.flush()

def procesador():
    global imagenes_procesadas
    while True:
        imagen = cola_imagenes.get()
        if imagen is None:
            break  # Ya no se vuelve a meter el None
        archivo_procesador.write(f"Procesando imagen: {imagen}\n")
        time.sleep(random.uniform(1.0, 2.0))
        archivo_procesador.write(f"Imagen procesada: {imagen}\n")
        archivo_procesador.flush()
        with lock:
            imagenes_procesadas += 1
            if imagenes_procesadas == TOTAL_IMAGENES:
                finalizado.set()
        cola_imagenes.task_done()

def monitor():
    while not finalizado.is_set():
        with lock:
            print(f"[MONITOR] Cola: {cola_imagenes.qsize()} | Imágenes procesadas: {imagenes_procesadas}")
        time.sleep(1)

    # Print final
    time.sleep(1)
    with lock:
        print(f"[MONITOR] Cola: {cola_imagenes.qsize()} | Imágenes procesadas: {imagenes_procesadas} (final)")

# Lanzar hilos
h1 = threading.Thread(target=receptor)
h2 = threading.Thread(target=procesador)
h3 = threading.Thread(target=monitor)

h1.start()
h2.start()
h3.start()

h1.join()
h2.join()
h3.join()

archivo_receptor.close()
archivo_procesador.close()

print("\n✅ Todo ha terminado. Revisa 'receptor.txt' y 'procesador.txt'")
