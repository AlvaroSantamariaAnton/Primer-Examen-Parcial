# Proyecto de Rutas y Conectividad de Localidades

Este proyecto implementa varias funcionalidades para manejar y analizar un grafo de localidades conectadas por carreteras, representado en un diccionario en Python. Cada archivo `.py` contiene una función específica para trabajar con el grafo.

## Estructura del Proyecto

- **datos.py**: Contiene el diccionario `localidades`, que representa el grafo de localidades y las distancias entre ellas.
- **ruta_mas_corta.py**: Implementa la función `ruta_mas_corta` para encontrar la ruta más corta entre dos localidades usando el algoritmo de Dijkstra.
- **conexiones_cortas.py**: Contiene la función `localidades_con_conexiones_cortas` para identificar las localidades donde todas las conexiones son menores a una distancia específica.
- **es_conexo.py**: Implementa la función `es_conexo` para verificar si el grafo es conexo, utilizando DFS.
- **rutas_alternativas.py**: Contiene la función `rutas_alternativas` que encuentra todas las rutas sin ciclos entre dos localidades usando BFS.