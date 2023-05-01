import math
from data import city_locations

def encontrar_coordenadas(path):
    path_x = []
    path_y = []
    for point in path: #por cada punto de la ruta
        for city, value in city_locations.items(): #se obtienen las coordenadas correspondientes
            if city == point:
                path_x.append(value[0])
                path_y.append(value[1])
    return path_x, path_y

def hallar_maximos():
    array_distancias = []
    for city1 in city_locations.keys():
        for city2 in city_locations.keys():
            x1, y1 = city_locations[city1]
            x2, y2 = city_locations[city2]
            array_distancias.append(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    return array_distancias
