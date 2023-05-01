import math
from data import city_locations, hallar_maximos, mapa
from grafico import graficar

# función para calcular la distancia entre la ciudad actual y el destino
def distancia(ciudad_actual, destino):
    x1, y1 = city_locations[ciudad_actual]
    x2, y2 = city_locations[destino]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def normalizar(a,a_min,a_max):
    a_norm = (a - a_min) / (a_max - a_min)
    return a_norm

# función evaluadora f(n)
def fevaluadora(ciudad_actual,vecino,destino):
    w1,w2,w3,w4=0.5,0.3,0.1,0.1 #se establecen los pesos
    array_distancias = hallar_maximos()

    distancia_norm = normalizar(distancia(vecino,destino),min(array_distancias),max(array_distancias)) #DISTANCIA RECTA DEL VECINO AL OBJETIVO
    
    resultado = 0.5 * distancia_norm
    return resultado

# función de búsqueda A*
def astar_search(inicio, destino):
    ruta = [inicio] # lista de ciudades visitadas
    visited = {inicio} # conjunto de ciudades visitadas
    while ruta[-1] != destino: # siempre y cuando la ultima ciudad en el recorrido sea diferente, continúa
        ciudad_actual = ruta[-1] # última ciudad en la ruta
        vecinos = [(fevaluadora(ciudad_actual,vecino,destino), vecino) for vecino in mapa[ciudad_actual].keys() - visited] # lista de tuplas [resultado de f(n),vecinos no visitados]
        if not vecinos: #si ya no hay vecinos retorna None
            return None
        _, ciudad_elegida = min(vecinos) # elegir el vecino con menor f(n) / el min("tupla") elige el valor mínimo del primer elemento
        ruta.append(ciudad_elegida) #se agrega a la ruta
        visited.add(ciudad_elegida) #se agrega a los visitados
    return ruta

def encontrar_coordenadas(path):
    path_x = []
    path_y = []
    for point in path: #por cada punto de la ruta
        for city, value in city_locations.items(): #se obtienen las coordenadas correspondientes
            if city == point:
                path_x.append(value[0])
                path_y.append(value[1])
    return path_x, path_y

# MÉTODO MAIN
if __name__ == "__main__":
    start=str(input("Ingrese el punto de inicio: "))
    goal=str(input("Ingrese el punto de llegada: "))
    path = astar_search(start,goal)

    path_x, path_y = encontrar_coordenadas(path)

    graficar(path_x,path_y)
    print(path)