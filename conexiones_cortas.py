from datos import localidades

def localidades_con_conexiones_cortas(localidades, distancia_maxima=15):
    localidades_cortas = []

    for localidad, conexiones in localidades.items():
        # Verificamos si todas las conexiones tienen distancias menores a la distancia máxima especificada
        if all(distancia < distancia_maxima for _, distancia in conexiones):
            localidades_cortas.append(localidad)
    
    return localidades_cortas

# Ejemplo de uso
localidades_cortas = localidades_con_conexiones_cortas(localidades)
print("Localidades con todas las conexiones menores a 15 km:", localidades_cortas)