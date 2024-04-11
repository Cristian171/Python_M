
## Uso de Colas en Python

En esta solución, utilizamos colas para simular la fila de clientes que esperan ser atendidos por el asesor en el banco. Las colas son estructuras de datos que siguen el principio de "primero en entrar, primero en salir" (FIFO, por sus siglas en inglés), lo que significa que el primer elemento que se agrega a la cola es el primero en ser eliminado. Python proporciona una implementación de colas a través de la clase `Queue` en el módulo `queue`.

## explicacion mas simple 
¡Claro! Imagina que estás en una tienda de helados y hay una cola de personas esperando. La primera persona que llega es la primera en ser atendida, ¿verdad? Bueno, una cola en Python es como esa fila de personas. Puedes agregar nuevos elementos al final de la cola y quitar elementos de la parte delantera. Es como una lista, ¡pero con reglas especiales sobre cómo agregar y quitar elementos!

### Ejemplo de Uso:

1. **Importar la Clase `Queue`:**

   ```python
   from queue import Queue
   
```
# Crear una Cola Vacía:
cola = Queue()
# Agregar Elementos a la Cola:
cola.put(elemento)
# Eliminar y Devolver el Primer Elemento de la Cola:
elemento = cola.get()

## Uso en esta Solución:
En esta solución, utilizamos una cola para gestionar la fila de clientes en el banco. Aquí está cómo se utilizan las colas en esta solución:

# Creamos una cola vacía al inicio de la simulación:
- cola = Queue()

# Agregamos clientes a la cola cuando llegan al banco:
- cola.put((tiempo_actual, tiempo_atencion_cliente))

# Procesamos la cola para atender a los clientes:

- if not cola.empty():
    tiempo_cliente_en_cola = tiempo_simulado - cola.get()
    tiempo_inactivo += tiempo_cliente_en_cola
    tiempo_simulado += tiempo_atencion
    clientes_atendidos += 1

- Calculamos la cantidad de clientes en cola al finalizar la jornada:

clientes_en_cola_final = len(cola) - (tiempo_total_clientes - len(cola))
Las colas nos permiten gestionar eficazmente el orden de atención de los clientes y calcular el tiempo de espera y el tiempo de inactividad del asesor en el banco.

