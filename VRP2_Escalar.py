import math
from operator import itemgetter

# Parámetros
COSTO_COMBUSTIBLE = 1.2  # costo por km
MAX_COSTO_RUTA = 700
MAX_CARGA = 40
VELOCIDAD_PROMEDIO = 70  # km/h
MAX_TIEMPO_HORAS = 8     # horas

# Casetas entre pares de ciudades (ejemplo)
CASETAS = {
    ('CDMX', 'QRO'): 200,
    ('CDMX', 'PUE'): 150,
    ('SLP', 'QRO'): 100,
    ('SLP', 'GDL'): 200,
    ('MTY', 'SLP'): 250,
    ('MTY', 'SON'): 300,
    ('EDO.MEX', 'MICH'): 180
}

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def costo_ruta(ruta, coord):
    costo = 0
    for i in range(len(ruta) - 1):
        d = distancia(coord[ruta[i]], coord[ruta[i+1]]) * 111
        costo += d * COSTO_COMBUSTIBLE
        key = (ruta[i], ruta[i+1])
        if key in CASETAS:
            costo += CASETAS[key]
        elif (ruta[i+1], ruta[i]) in CASETAS:
            costo += CASETAS[(ruta[i+1], ruta[i])]
    return costo

def tiempo_ruta(ruta, coord):
    total_km = 0
    for i in range(len(ruta) - 1):
        total_km += distancia(coord[ruta[i]], coord[ruta[i+1]])
    return (total_km * 111) / VELOCIDAD_PROMEDIO

def en_ruta(rutas, c):
    for r in rutas:
        if c in r:
            return r
    return None

def peso_ruta(ruta, pedidos):
    return sum(pedidos[c] for c in ruta)

def vrp_voraz(coord, almacen, pedidos, max_carga):
    s = {}
    for c1 in coord:
        for c2 in coord:
            if c1 != c2 and (c2, c1) not in s:
                d_c1_c2 = distancia(coord[c1], coord[c2])
                d_c1_almacen = distancia(coord[c1], almacen)
                d_c2_almacen = distancia(coord[c2], almacen)
                s[c1, c2] = d_c1_almacen + d_c2_almacen - d_c1_c2

    s = sorted(s.items(), key=itemgetter(1), reverse=True)

    rutas = []
    for k, _ in s:
        rc1 = en_ruta(rutas, k[0])
        rc2 = en_ruta(rutas, k[1])
        nueva = None

        if rc1 is None and rc2 is None:
            nueva = [k[0], k[1]]
            if peso_ruta(nueva, pedidos) <= max_carga and \
               costo_ruta(nueva, coord) <= MAX_COSTO_RUTA and \
               tiempo_ruta(nueva, coord) <= MAX_TIEMPO_HORAS:
                rutas.append(nueva)
        elif rc1 and rc2 is None:
            if rc1[0] == k[0]:
                nueva = [k[1]] + rc1
            elif rc1[-1] == k[0]:
                nueva = rc1 + [k[1]]
            if nueva and peso_ruta(nueva, pedidos) <= max_carga and \
               costo_ruta(nueva, coord) <= MAX_COSTO_RUTA and \
               tiempo_ruta(nueva, coord) <= MAX_TIEMPO_HORAS:
                rutas[rutas.index(rc1)] = nueva
        elif rc1 is None and rc2:
            if rc2[0] == k[1]:
                nueva = [k[0]] + rc2
            elif rc2[-1] == k[1]:
                nueva = rc2 + [k[0]]
            if nueva and peso_ruta(nueva, pedidos) <= max_carga and \
               costo_ruta(nueva, coord) <= MAX_COSTO_RUTA and \
               tiempo_ruta(nueva, coord) <= MAX_TIEMPO_HORAS:
                rutas[rutas.index(rc2)] = nueva
        elif rc1 != rc2:
            if rc1[0] == k[0] and rc2[-1] == k[1]:
                nueva = rc2 + rc1
                if peso_ruta(nueva, pedidos) <= max_carga and \
                   costo_ruta(nueva, coord) <= MAX_COSTO_RUTA and \
                   tiempo_ruta(nueva, coord) <= MAX_TIEMPO_HORAS:
                    rutas[rutas.index(rc2)] = nueva
                    rutas.remove(rc1)
            elif rc1[-1] == k[0] and rc2[0] == k[1]:
                nueva = rc1 + rc2
                if peso_ruta(nueva, pedidos) <= max_carga and \
                   costo_ruta(nueva, coord) <= MAX_COSTO_RUTA and \
                   tiempo_ruta(nueva, coord) <= MAX_TIEMPO_HORAS:
                    rutas[rutas.index(rc1)] = nueva
                    rutas.remove(rc2)

    return rutas

if __name__ == "__main__":
    coord = {
        'EDO.MEX': (19.2938258568844, -99.65366252023884),
        'QRO': (20.593537489366717, -100.39004057702225),
        'CDMX': (19.432854452264177, -99.13330004822943),
        'SLP': (22.151725492903953, -100.97657666103268),
        'MTY': (25.673156272083876, -100.2974200019319),
        'PUE': (19.063532268065185, -98.30729139446866),
        'GDL': (20.67714565083998, -103.34696388920293),
        'MICH': (19.702614895389996, -101.19228631929688),
        'SON': (29.075273188617818, -110.95962477655333)
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

    almacen = [19.432854452264177, -99.13330004822943]

    rutas = vrp_voraz(coord, almacen, pedidos, MAX_CARGA)

    for i, ruta in enumerate(rutas, 1):
        print(f"Ruta {i}: {ruta}, Peso: {peso_ruta(ruta, pedidos)}, "
                f"Costo: ${costo_ruta(ruta, coord):.2f}, "
                f"Tiempo: {tiempo_ruta(ruta, coord):.2f}h")
