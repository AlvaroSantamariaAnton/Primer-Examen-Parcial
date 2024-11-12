from datos import localidades
from collections import deque

def rutas_alternativas(localidades, origen, destino):
    # Cola para almacenar rutas; cada elemento es una lista que representa una ruta
    rutas = deque([[origen]])
    rutas_sin_ciclos = []

    # BFS
    while rutas:
        ruta_actual = rutas.popleft()
        localidad_actual = ruta_actual[-1]

        # Si llegamos al destino, guardamos la ruta
        if localidad_actual == destino:
            rutas_sin_ciclos.append(ruta_actual)
        else:
            # Explorar vecinos sin volver a pasar por localidades ya visitadas en la ruta
            for vecino, _ in localidades[localidad_actual]:
                if vecino not in ruta_actual:  # Evitar ciclos
                    nueva_ruta = ruta_actual + [vecino]
                    rutas.append(nueva_ruta)

    return rutas_sin_ciclos

# Ejemplo de uso
origen = "Alcorcón"
destino = "Madrid"
rutas = rutas_alternativas(localidades, origen, destino)

print(f"Rutas alternativas de {origen} a {destino}:")
for i, ruta in enumerate(rutas, 1):
    print(f"Ruta {i}: {' -> '.join(ruta)}")