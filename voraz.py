import math
from data import city_locations
from grafico import graficar

# función para calcular la distancia entre dos ciudades
def distance(city1, city2):
    x1, y1 = city_locations[city1]
    x2, y2 = city_locations[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# función de búsqueda voraz
def greedy_search(start, goal):
    path = [start] # lista de ciudades visitadas
    visited = {start} # conjunto de ciudades visitadas
    while path[-1] != goal: # siempre y cuando la ultima ciudad en el recorrido sea diferente, continúa
        city = path[-1] # última ciudad visitada
        neighbors = [(distance(city, neighbor), neighbor) for neighbor in city_locations.keys() - visited] # lista de tuplas [distancia ciudad - vecino,vecinos no visitados]
        if not neighbors: #si ya no hay vecinos retorna None
            return None
        _, closest_city = min(neighbors) # elegir el vecino más cercano / el min("tupla") elige el valor mínimo del primer elemento
        path.append(closest_city) #se agrega a la ruta
        visited.add(closest_city) #se agrega a los visitados
    return path

def encontrar_coordenadas(path):
    path_x = []
    path_y = []
    for point in path:
        for city, value in city_locations.items():
            if city == point:
                path_x.append(value[0])
                path_y.append(value[1])
    return path_x, path_y

# MÉTODO MAIN
if __name__ == "__main__":
    start=input("Ingrese el punto de inicio: ")
    goal=input("Ingrese el punto de llegada: ")
    path = greedy_search(start,goal)

    path_x, path_y = encontrar_coordenadas(path)

    graficar(path_x,path_y)
    print(path)
