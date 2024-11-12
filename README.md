# Proyecto de Rutas y Conectividad de Localidades

Este proyecto implementa varias funcionalidades para manejar y analizar un grafo de localidades conectadas por carreteras, representado en un diccionario en Python. Cada archivo `.py` contiene una función específica para trabajar con el grafo.

## Estructura del Proyecto

- **datos.py**: Contiene el diccionario `localidades`, que representa el grafo de localidades y las distancias entre ellas.
- **ruta_mas_corta.py**: Implementa la función `ruta_mas_corta` para encontrar la ruta más corta entre dos localidades usando el algoritmo de Dijkstra.
- **conexiones_cortas.py**: Contiene la función `localidades_con_conexiones_cortas` para identificar las localidades donde todas las conexiones son menores a una distancia específica.
- **es_conexo.py**: Implementa la función `es_conexo` para verificar si el grafo es conexo, utilizando DFS.
- **rutas_alternativas.py**: Contiene la función `rutas_alternativas` que encuentra todas las rutas sin ciclos entre dos localidades usando BFS.

## Complejidad Computacional

Cada función tiene una complejidad específica, que se detalla a continuación:

1. **`ruta_mas_corta`** (Algoritmo de Dijkstra):
   - **Big O (peor caso)**: \( O(E \log V) \)
   - **Omega (mejor caso)**: \( \Omega(V \log V) \)
   - **Theta (caso promedio)**: \( \Theta(E \log V) \)

2. **`localidades_con_conexiones_cortas`**:
   - **Big O (peor caso)**: \( O(V + E) \)
   - **Omega (mejor caso)**: \( \Omega(V) \)
   - **Theta (caso promedio)**: \( \Theta(V + E) \)

3. **`es_conexo`** (Búsqueda en Profundidad - DFS):
   - **Big O (peor caso)**: \( O(V + E) \)
   - **Omega (mejor caso)**: \( \Omega(V) \)
   - **Theta (caso promedio)**: \( \Theta(V + E) \)

4. **`rutas_alternativas`** (Búsqueda en Anchura - BFS):
   - **Big O (peor caso)**: \( O(b^d) \), donde \( b \) es el factor de ramificación promedio y \( d \) es la profundidad de las rutas exploradas.
   - **Omega (mejor caso)**: \( \Omega(V) \)
   - **Theta (caso promedio)**: \( \Theta(b^d) \)

### Nota
- \( V \): Número de localidades (nodos).
- \( E \): Número de conexiones entre localidades (aristas).
- **Complejidad general**: La función `rutas_alternativas` presenta la mayor complejidad en el peor caso debido a su crecimiento exponencial \( O(b^d) \).