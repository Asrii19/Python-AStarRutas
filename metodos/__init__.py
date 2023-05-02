import math
from data import city_locations, city_prices, totales, mapa

# función para calcular la distancia entre la ciudad actual y el destino
def distancia(ciudad_actual, destino):
    x1, y1 = city_locations[ciudad_actual]
    x2, y2 = city_locations[destino]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

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
    
    distance = r * c
    return distance

# funcion para calcular el precio entre la ciudad actual y el vecino
def precio(ciudad_actual, vecino):
    price = city_prices[ciudad_actual][vecino]
    return float(price)

# normalizar datos
def normalizar(a,a_min,a_max):
    a_norm = (a - a_min) / (a_max - a_min)
    return a_norm

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

def hallar_totales(ruta):
    #distancia recorrida
    ruta_distancia=[]
    for i,city in enumerate(ruta):
        if not i+1 == len(ruta):
            ruta_distancia.append(haversine(city,ruta[i+1]))
        totales["distancia_total"] = sum(ruta_distancia)
    #precio total
    

def hallar_maximos(destino):
    array_dlr = []
    array_distancias = []
    array_precios = []
    # hallar dlr maximo
    for city1 in city_locations.keys():
        x1, y1 = city_locations[city1]
        x2, y2 = city_locations[destino]
        array_dlr.append(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    # hallar distancia maxima
    for city1,vecinos in mapa.items():
        for value in vecinos.values():
            x1, y1 = city_locations[city1]
            x2, y2 = value
            array_distancias.append(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    """ for value in city_prices.values():
        for price in value.values():
            array_precios.append(price) """

    return array_dlr, array_distancias, array_precios
