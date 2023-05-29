import math
from data import city_locations,city_prices, mapa
from data import array_distancia, array_preciokilometro, array_tiempo
from data import precio_kilometro, totales, velocidad

# distancia en kilometros
def haversine(ciudad_actual, destino):
    lon1, lat1 = city_locations[ciudad_actual]
    lon2, lat2 = city_locations[destino]
    r = 6371  # Radio de la Tierra en km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
 
    a = math.sin(dLat / 2) ** 2 + math.sin(dLon / 2) ** 2 * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.asin(math.sqrt(a))
    
    distance = round(r * c,2)
    return distance

# funcion para calcular el precio de viaje entre la ciudad actual y el vecino
def precio(ciudad_actual, vecino):
    price = city_prices[ciudad_actual][vecino]
    return round(price,2)

# funcion para calcular el tiempo entre 2 ciudades
def tiempo(ciudad_actual, vecino):
    time = haversine(ciudad_actual,vecino)/velocidad # d = v*t -> t = d/v
    return round(time,2)

# normalizar datos
def normalizar(a,a_min,a_max):
    a_norm = (a - a_min) / (a_max - a_min)
    return round(a_norm,2)

def encontrar_coordenadas(path):
    path_x = []
    path_y = []
    for point in path: #por cada punto de la ruta
        for city, value in city_locations.items(): #se obtienen las coordenadas correspondientes
            if city == point:
                path_x.append(value[0])
                path_y.append(value[1])
    return path_x, path_y

def encontrar_ciudad(city):
    for key in city_locations:
        if key == city:
            return True, city
    return False, city

def hallar_totales(ruta): # para la impresión en el resultado
    ruta_distancia=[] #distancia recorrida
    ruta_precio = [] #precio de la ruta optima
    ruta_tiempo = [] #tiempo de la ruta optima
    for i,city in enumerate(ruta):
        if not i+1 == len(ruta):
            ruta_distancia.append(haversine(city,ruta[i+1]))
            ruta_precio.append(precio(city,ruta[i+1]))
            ruta_tiempo.append(tiempo(city,ruta[i+1]))
    totales["distancia_total"] = sum(ruta_distancia)
    totales["precio_total"] = sum(ruta_precio)
    totales["tiempo_total"] = sum(ruta_tiempo)

def definir_data(): # para la normalización
    #distancia
    for city1 in city_locations.keys():
        for city2 in city_locations.keys():
            array_distancia.append(haversine(city1,city2))
    #tiempo
    for city1 in city_locations.keys():
        for city2 in city_locations.keys():
            array_tiempo.append(tiempo(city1,city2))
    #ganancia

    #precio de viaje
    for city, neighbors in mapa.items(): # define un array con todos los precios posibles entre ciudades
        for neighbor in neighbors.keys():
            d=haversine(city,neighbor)
            p=precio(city,neighbor)
            array_preciokilometro.append(round(p/d,2))# precio a su vecino/distancia a su vecino
            promedio = round(sum(array_preciokilometro)/len(array_preciokilometro),2)
    precio_kilometro.append(promedio) # se define el precio promedio por unidad de distancia (km)