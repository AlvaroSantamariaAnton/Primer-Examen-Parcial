from datos import localidades

def ruta_mas_larga(origen, destino):
    # Función auxiliar de DFS para buscar la ruta más larga sin ciclos
    def dfs(localidad_actual, distancia_actual, ruta_actual):
        # Si llegamos al destino, verificamos si esta es la ruta más larga encontrada
        if localidad_actual == destino:
            nonlocal max_distancia, mejor_ruta
            if distancia_actual > max_distancia:
                max_distancia = distancia_actual
                mejor_ruta = ruta_actual[:]
            return

        # Visitamos cada vecino sin volver a pasar por localidades ya visitadas
        for vecino, distancia in localidades[localidad_actual]:
            if vecino not in ruta_actual:  # Evitar ciclos
                ruta_actual.append(vecino)
                dfs(vecino, distancia_actual + distancia, ruta_actual)
                ruta_actual.pop()

    # Variables para almacenar la máxima distancia y la mejor ruta encontrada
    max_distancia = float('-inf')
    mejor_ruta = []

    # Iniciamos DFS desde la localidad de origen
    dfs(origen, 0, [origen])

    return mejor_ruta, max_distancia

# Ejemplo de uso
# Ruta más larga entre Alcorcón y Madrid
ruta_larga, distancia_larga = ruta_mas_larga("Alcorcón", "Madrid")
print("Ruta más larga:", ruta_larga)
print("Distancia total de la ruta más larga:", distancia_larga)