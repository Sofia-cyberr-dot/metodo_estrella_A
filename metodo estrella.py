import heapq  # para la cola de prioridad

# Representamos al grafo (distancias en km)
grafo = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'D': 5, 'E': 10},
    'C': {'A': 3, 'F': 4, 'G': 8},
    'D': {'B': 5, 'H': 7},
    'E': {'B': 10, 'I': 6, 'J': 15},
    'F': {'C': 4, 'G': 2, 'H': 6},
    'G': {'C': 8, 'F': 2, 'I': 9},
    'H': {'D': 7, 'F': 6, 'I': 5},
    'I': {'H': 5, 'G': 9, 'E': 6, 'J': 4},
    'J': {'E': 15, 'I': 4}
}

# Heurística h(n): estimación de la distancia restante al nodo J 
heuristica = {
    'A': 20, 'B': 3, 'C': 15, 'D': 12, 'E': 8,
    'F': 10, 'G': 9, 'H': 7, 'I': 4, 'J': 0
}

# Algoritnmo Estrella A*
def a_estrella(inicio, fin):
    #llevara un formmato de prioridas: (f, nodo, camino, g)
    frontera = [(heuristica[inicio], inicio, [inicio], 0)]
    visitados = []  # para mostrar el orden de exploración

    while frontera:
        f, nodo, camino, g = heapq.heappop(frontera)
        visitados.append(nodo)

        # devolvemos los resultados una vez llegamos al destino
        if nodo == fin:
            return camino, g, visitados

        # los vecinos seran expandidos

        for vecino, costo in grafo[nodo].items():
            if vecino not in visitados:
                g_nuevo = g + costo
                f_nuevo = g_nuevo + heuristica[vecino]
                heapq.heappush(frontera, (f_nuevo, vecino, camino + [vecino], g_nuevo))

    return None, float('inf'), visitados

# main
camino, costo_total, explorados = a_estrella('A', 'J')

# impresion en pantalla
print("Camino óptimo encontrado:", " → ".join(camino))
print("Costo total del recorrido:", costo_total, "km")
print("Nodos explorados (en orden):", explorados)