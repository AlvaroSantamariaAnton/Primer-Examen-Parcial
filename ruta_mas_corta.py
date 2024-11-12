from datos import localidades
import heapq

def ruta_mas_corta(localidades, origen, destino):
    # Inicializamos la distancia y el camino más corto para cada localidad
    distancias = {localidad: float('inf') for localidad in localidades}
    distancias[origen] = 0
    camino = {localidad: [] for localidad in localidades}
    camino[origen] = [origen]

    # Cola de prioridad para almacenar las localidades a explorar
    cola_prioridad = [(0, origen)]  # (distancia acumulada, localidad actual)
    
    while cola_prioridad:
        distancia_actual, localidad_actual = heapq.heappop(cola_prioridad)

        # Si llegamos a la localidad de destino, terminamos
        if localidad_actual == destino:
            return camino[destino], distancias[destino]

        # Revisamos las localidades vecinas
        for vecino, distancia in localidades[localidad_actual]:
            nueva_distancia = distancia_actual + distancia

            # Si encontramos una ruta más corta hacia el vecino, actualizamos
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                camino[vecino] = camino[localidad_actual] + [vecino]
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    # Si no se encuentra ruta
    return None, float('inf')

# Ejemplo de uso
ruta, distancia_total = ruta_mas_corta(localidades, "Alcorcón", "Torrejón de Ardoz")
print("Ruta más corta:", ruta)
print("Distancia total:", distancia_total)