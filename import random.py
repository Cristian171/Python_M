import random

# Función para simular la llegada de clientes con distribución uniforme entre 10 y 30 minutos
def llegada_clientes():
    return random.randint(10, 30)

# Función para simular el tiempo de atención del asesor con distribución uniforme entre 15 y 25 minutos
def tiempo_atencion():
    return random.randint(15, 25)

# Simulación de la jornada laboral de 8 horas
tiempo_jornada = 8 * 60  # Convertir horas a minutos
tiempo_total_clientes = 0
cola = []
tiempo_inactividad = 0
tiempo_actual = 0

while tiempo_actual < tiempo_jornada:
    tiempo_llegada_siguiente_cliente = llegada_clientes()
    tiempo_actual += tiempo_llegada_siguiente_cliente
    if tiempo_actual < tiempo_jornada:
        tiempo_total_clientes += 1
        tiempo_atencion_cliente = tiempo_atencion()
        if tiempo_actual > tiempo_inactividad:
            tiempo_inactividad += tiempo_actual - tiempo_inactividad
        else:
            tiempo_inactividad += tiempo_llegada_siguiente_cliente
        cola.append((tiempo_actual, tiempo_atencion_cliente))

tiempo_cliente_actual = 0
tiempo_total_espera = 0
tiempo_termino_ultima_atencion = 0

print("Cantidad de clientes que llegaron durante la jornada:", tiempo_total_clientes)

for cliente in cola:
    tiempo_llegada_cliente, tiempo_atencion_cliente = cliente
    tiempo_espera = max(0, tiempo_cliente_actual - tiempo_llegada_cliente)
    tiempo_total_espera += tiempo_espera
    tiempo_cliente_actual = max(tiempo_llegada_cliente, tiempo_termino_ultima_atencion)
    tiempo_termino_atencion = tiempo_cliente_actual + tiempo_atencion_cliente
    tiempo_termino_ultima_atencion = tiempo_termino_atencion
    print("Tiempo de llegada del cliente:", tiempo_llegada_cliente, "Tiempo de atención:", tiempo_atencion_cliente, "Tiempo de espera:", tiempo_espera)

clientes_en_cola_final = len(cola) - (tiempo_total_clientes - len(cola))
print("Cantidad de clientes en cola luego de terminarse la jornada:", clientes_en_cola_final)
print("Tiempo de inactividad del asesor:", tiempo_jornada - tiempo_inactividad)
