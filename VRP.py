# Alforitmo de VRP
import math
from operator import itemgetter

def distancia(coord1, coord2):
    latitud1 = coord1[0]
    longitud1 = coord1[1]
    latitud2 = coord2[0]
    longitud2 = coord2[1]
    
    return math.sqrt((latitud1 - latitud2)**2 + (longitud1 - longitud2)**2)

def en_ruta(rutas, c):
    ruta = None
    for r in rutas:
        if c in r:
            ruta = r
    return ruta

def peso_ruta(ruta, pedidos):
    total = 0
    for c in ruta:
        total = total + pedidos[c]
    return total

def vrp_voraz(coord, almacen, pedidos, max_carga):
    # Calcular lo ahorros
    s = {}
    for c1 in coord:
        for c2 in coord:
            if c1 != c2:
                if not (c2, c1) in s:
                    d_c1_c2 = distancia(coord[c1], coord[c2])
                    d_c1_almacen = distancia(coord[c1], almacen)
                    d_c2_almacen = distancia(coord[c2], almacen)
                    s[c1, c2] = d_c1_almacen + d_c2_almacen - d_c1_c2
                    
# Ordenar los ahorros
    s = sorted(s.items(), key = itemgetter(1), reverse=True)
    
    # Crear rutas
    rutas = []
    for k,v in s:
        rc1 = en_ruta(rutas, k[0])
        rc2 = en_ruta(rutas, k[1])
        if rc1 == None and rc2 == None:
            # No estan en ninguna ruta, La creamos
            if peso_ruta([k[0], k[1]], pedidos)<= max_carga:
                rutas.append([k[0], k[1]])
        elif rc1 != None and rc2 ==None:
            # Cliente 1 ya cuenta con una ruta, agregamos al el cliente 2
            if rc1[0] == k[0]:
                if peso_ruta(rc1, pedidos) + peso_ruta([k[1]], pedidos) <= max_carga:
                    #rutas[rutas.index(rc1)].append(k[1])
                    rutas[rutas.index(rc1)].insert(0, k[1])
            elif rc1[len(rc1)-1] == k[0]:
                if peso_ruta(rc1, pedidos) + peso_ruta([k[1]], pedidos) <= max_carga:
                    rutas[rutas.index(rc1)].append(k[1])
        elif rc1 == None and rc2 != None:
            # Cliente 2 ya cuenta con una ruta, agregamos al el cliente 1
            if rc2[0] == k[1]:
                if peso_ruta(rc2, pedidos) + peso_ruta([k[0]], pedidos) <= max_carga:
                    #rutas[rutas.index(rc1)].append(k[1])
                    rutas[rutas.index(rc2)].insert(0, k[0])
            elif rc2[len(rc2)-1] == k[1]:
                if peso_ruta(rc2, pedidos) + peso_ruta([k[0]], pedidos) <= max_carga:
                    rutas[rutas.index(rc2)].append(k[0])
        elif rc1 != None and rc2 != None and rc1 != rc2:
            # Ambos clientes ya cuentan con una ruta, unimos las rutas
            if rc1 != None and rc2 != None and rc1 != rc2:
                if rc1[0] == k[0] and rc2[len(rc2)-1] == k[1]:
                    if peso_ruta(rc1, pedidos) +  peso_ruta(rc2, pedidos) <= max_carga:
                        rutas[rutas.index(rc2)] .extend(rc1)
                        rutas.remove(rc1)
                elif rc1[len(rc1)-1] == k[0] and rc2[0] == k[1]:
                    if peso_ruta(rc1, pedidos) +  peso_ruta(rc2, pedidos) <= max_carga:
                        rutas[rutas.index(rc1)] .extend(rc2)
                        
                        rutas.remove(rc2)
                        
    return rutas

if __name__ == "__main__":
    # Cargar Cordenadas
    coord ={
        'EDO.MEX': (19.293617673554333, -99.65338254460296),
        'QRO': (20.59348465205853, -100.38996772873921),
        'CDMX': (19.43283709057628, -99.13303365269418),
        'SLP': (22.150195251189672, -100.97675061592356),
        'MTY': (25.67511699454124, -100.2875701065098),
        'PUE': (19.050881755234542, -98.19785486367275),
        'GDL': (20.677221262504663, -103.34702085125724),
        'MICH':(19.702303570311045, -101.19237006320859),
        'SON': (29.075329282500228, -110.95925086647266)
    }
    pedidos = {
        'EDO.MEX': 10,
        'QRO': 13,
        'CDMX': 7,
        'SLP': 11,
        'MTY': 15,
        'PUE': 8,
        'GDL': 6,
        'MICH': 7,
        'SON': 8
    }
    

    # Cargar Almacen
    almacen = [19.43283709057628, -99.13303365269418]
    max_carga = 40
    # Cargar rutas
    rutas = []
    # Ejecutar el algoritmo
    rutas = vrp_voraz(coord, almacen, pedidos, max_carga)
    # Imprimir rutas
    for ruta in rutas:
        print("Ruta: ", ruta)
        
    
    #Convertir en una dimension escalar