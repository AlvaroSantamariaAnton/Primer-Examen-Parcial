from datos import localidades

def es_conexo(localidades):
    # Elegimos una localidad de inicio arbitraria
    inicio = next(iter(localidades))
    
    # Conjunto para rastrear localidades visitadas
    visitadas = set()
    
    # Función auxiliar para DFS
    def dfs(localidad):
        # Marcamos la localidad como visitada
        visitadas.add(localidad)
        
        # Recorremos cada localidad conectada
        for vecino, _ in localidades[localidad]:
            if vecino not in visitadas:
                dfs(vecino)
    
    # Iniciamos DFS desde la localidad de inicio
    dfs(inicio)
    
    # Verificamos si todas las localidades han sido visitadas
    return len(visitadas) == len(localidades)

# Ejemplo de uso
if es_conexo(localidades):
    print("El grafo es conexo: es posible llegar a cualquier localidad desde cualquier otra.")
else:
    print("El grafo no es conexo: hay localidades que no están conectadas con otras.")