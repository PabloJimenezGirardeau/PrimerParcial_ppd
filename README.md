# 🛰️ Procesamiento Concurrente de Imágenes Satelitales

Este proyecto simula un sistema en tiempo real que recibe imágenes desde satélites, las almacena temporalmente y las procesa de forma secuencial utilizando **concurrencia con hilos** (`threading`) y una **cola segura** (`queue.Queue`) en Python.

---

## 📦 Estructura del sistema

El sistema está compuesto por 3 hilos principales:

### 1. Receptor (`receptor`)
- Simula la llegada de imágenes desde satélites.
- Las imágenes llegan de forma **impredecible** (a veces muy seguidas, a veces con pausas).
- Se almacenan en una cola compartida (`Queue`) para ser procesadas.
- Registra cada imagen recibida en el archivo `receptor.txt`.

### 2. Procesador (`procesador`)
- Extrae imágenes de la cola y las procesa una por una.
- Simula un procesamiento lento.
- Marca cada imagen como procesada en el archivo `procesador.txt`.

### 3. Monitor (`monitor`)
- Muestra en consola el estado del sistema:
  - Número de imágenes en la cola.
  - Número de imágenes procesadas.
- Termina automáticamente cuando se han procesado todas las imágenes.

---

## 🧠 Características clave

- Uso de `threading.Thread` para ejecutar tareas concurrentemente.
- Comunicación segura entre hilos mediante `queue.Queue`.
- Control de concurrencia con `threading.Lock` para evitar condiciones de carrera.
- Uso de `threading.Event` para detectar el momento exacto en que todo el procesamiento ha finalizado.
- Los archivos `receptor.txt` y `procesador.txt` contienen el log completo de actividad.

---

## 🗃️ Archivos generados

- `receptor.txt` → Registra todas las imágenes recibidas.
- `procesador.txt` → Registra todas las imágenes procesadas.

---

## ▶️ Ejecución

Simplemente ejecuta el archivo Python:

```bash
python procesamiento_imagenes.py
