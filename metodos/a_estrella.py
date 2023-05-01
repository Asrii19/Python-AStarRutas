import math
from data import city_locations, city_prices, mapa
from metodos import hallar_maximos, distancia, precio, normalizar

# función evaluadora f(n)
def fevaluadora(ciudad_actual,vecino,destino):
    w1,w2,w3,w4=0.5,0.3,0.1,0.1 #se establecen los pesos
    array_distancias,array_precios = hallar_maximos()

    #OBTENER LAS 4 VARIABLES
    distancia_act = distancia(vecino,destino) #DISTANCIA RECTA DEL VECINO AL OBJETIVO
    """ precio_act = precio(ciudad_actual,vecino) #PRECIO ENTRE CIUDAD ACTUAL Y SU VECINO """

    #NORMALIZAR VARIABLES EN EL RANGO (0,1)
    distancia_norm = normalizar(distancia_act,min(array_distancias),max(array_distancias)) 
    """ precio_norm = normalizar(precio_act,min(array_precios),max(array_precios)) """

    resultado = w1* distancia_norm
    return resultado

# función de búsqueda A*
def astar_search(inicio, destino):
    ruta = [inicio] # lista de ciudades visitadas
    visited = {inicio} # conjunto de ciudades visitadas
    while ruta[-1] != destino: # siempre y cuando la ultima ciudad en el recorrido sea diferente, continúa
        ciudad_actual = ruta[-1] # última ciudad en la ruta

        # lista de tuplas [resultado de f(n),vecinos no visitados]
        vecinos = []
        for vecino in mapa[ciudad_actual].keys() - visited:
            f_evaluada = fevaluadora(ciudad_actual, vecino, destino)
            tupla = (f_evaluada, vecino)
            vecinos.append(tupla)
        
        if not vecinos: #si ya no hay vecinos retorna None
            return None
        _, ciudad_elegida = min(vecinos) # elegir el vecino con menor f(n) / el min("tupla") elige el valor mínimo del primer elemento
        ruta.append(ciudad_elegida) #se agrega a la ruta
        visited.add(ciudad_elegida) #se agrega a los visitados
    return ruta