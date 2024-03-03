from Arbol import Nodo

def buscar_solucion_BFS_rec(nodo_incial, solucion, visitados):
    visitados.append(nodo_incial.get_datos())
    if nodo_incial.get_datos() == solucion:
        return nodo_incial  # Debe retornar el nodo, no la lista solución
    else:
        # Expandir los nodos sucesores (hijos)
        dato_nodo = nodo_incial.get_datos()
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
        hijo_izquierdo.padre = nodo_incial  # Asignar el padre manualmente
        
        hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
        hijo_central.padre = nodo_incial
        
        hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])
        hijo_derecho.padre = nodo_incial
        
        nodo_incial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])
        
        for nodo_hijo in nodo_incial.get_hijos():
            if nodo_hijo.get_datos() not in visitados:
                # Llamada Recursiva
                sol = buscar_solucion_BFS_rec(nodo_hijo, solucion, visitados)
                if sol is not None:
                    return sol
    
    return None

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_solucion = buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados)
    
    # Mostrar Resultado
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        print(resultado)
    else:
        print("No se encontró una solución.")

