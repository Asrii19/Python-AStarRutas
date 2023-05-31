from data import mapa,array_distancia,precio_kilometro,tiempo_kilometro, ganancia_kilometro
from metodos import haversine, normalizar, precio, tiempo, ganancia
from models.ciudad import Ciudad as Nodo

# Función de búsqueda A*
def astar_search(inicio, destino):
    openset = []  # Lista de nodos por evaluar
    closedset = set()  # Conjunto de nodos evaluados

    # Crear el nodo inicial
    ruta_inicial = [inicio]
    nodo_inicial = Nodo(inicio, 0, heuristica(inicio, destino), ruta_inicial)
    openset.append(nodo_inicial)

    while openset:
        # Obtener el nodo con el menor valor en f(x)
        for city in openset:
            print("OPENSET: \n",city)
        nodo_actual = min(openset, key=lambda x: x.f_x)

        # Si se llega al destino, retornar la ruta
        if nodo_actual.ciudad == destino:
            return nodo_actual.ruta

        # Mover el nodo actual de openset a closedset
        openset.remove(nodo_actual)

        # Generar los nodos vecinos y evaluarlos
        vecinos = generar_vecinos(nodo_actual.ciudad)
        print("nodo actual: ",nodo_actual)
        for vecino in vecinos:
            # Calcular el nuevo g_x acumulado
            nuevo_g_x = nodo_actual.g_x + calcular_costo(nodo_actual.ciudad, vecino.ciudad)

            if vecino.ciudad in closedset:
                continue  # El vecino ya fue evaluado, continuar con el siguiente
            
            if vecino not in openset:
                # Añadir el vecino a openset si no está presente
                vecino.g_x = nuevo_g_x
                vecino.h_x = heuristica(vecino.ciudad, destino)
                vecino.f_x = vecino.g_x + vecino.h_x
                vecino.ruta = nodo_actual.ruta + [vecino.ciudad]
                openset.append(vecino)
            else:
                print("hola")
                # Actualizar el vecino existente si se encuentra una ruta más corta
                if nuevo_g_x < vecino.g_x:
                    print("dentro")
                    vecino.g_x = nuevo_g_x
                    vecino.f_x = vecino.g_x + vecino.h_x
                    vecino.ruta = nodo_actual.ruta + [vecino.ciudad]
                    for dep in openset:
                        if dep.ciudad == vecino.ciudad:
                            dep=vecino
            print("\tvecino: ",vecino)
        print("---SE ELEGIÓ NODO---")
        closedset.add(nodo_actual.ciudad)

    # Si no se encontró una ruta, retornar None
    print("NADA")
    return None

w1,w2,w3,w4 = 0.25,0.4,0.25,0.1 #declaracion de pesos (distancia,tiempo,ganancia,precio)
# Función para calcular el costo entre dos ciudades
def calcular_costo(ciudad_actual, ciudad_vecino): #g_x
    # g(x) (costo)
    # OBTENER VARIABLES (4)
    # distancia
    distancia_act = haversine(ciudad_actual,ciudad_vecino)
    distancia_norm = normalizar(distancia_act,min(array_distancia),max(array_distancia)) # normalizar
    # tiempo
    tiempo_act = tiempo(ciudad_actual,ciudad_vecino)
    tiempo_norm = normalizar(tiempo_act,min(array_distancia)*tiempo_kilometro[0],
                             max(array_distancia)*tiempo_kilometro[0]) # normalizar
    # ganancia
    ganancia_act = ganancia(ciudad_vecino)
    ganancia_norm = normalizar(ganancia_act,min(array_distancia)*ganancia_kilometro[0],
                               max(array_distancia)*ganancia_kilometro[0]) # normalizar
    # precio del viaje
    precio_act = precio(ciudad_actual,ciudad_vecino)
    precio_norm = normalizar(precio_act,min(array_distancia)*precio_kilometro[0],
                             max(array_distancia)*precio_kilometro[0]) # normalizar
    # costo acumulado (mininimizar_distancia,minimizar_tiempo,maximizar_ganancia,minimizar_precio)
    g_x = distancia_norm*w1 + tiempo_norm*w2 - ganancia_norm*w3 +precio_norm*w4 
    return g_x  # Costo trivial, no considera ninguna variable adicional

# Función de heurística
def heuristica(vecino, destino): #h_x
    # h(x) (heurística, estimación)
    # OBTENER ESTIMACIÓN DE LAS VARIABLES (4)
    # distancia en linea recta al destino (dlr)
    dlr_act = haversine(vecino,destino) # distancia estimada
    dlr_norm = normalizar(dlr_act,min(array_distancia),max(array_distancia)) # normalizar
    # tiempo en linea recta al destino (tlr)
    tlr_act = dlr_act*tiempo_kilometro[0]
    tlr_norm = normalizar(tlr_act,min(array_distancia)*tiempo_kilometro[0],
                          max(array_distancia)*tiempo_kilometro[0]) # normalizar
    # ganancia en linea recta al destino (glr)
    glr_act = dlr_act*ganancia_kilometro[0]
    glr_norm = normalizar(glr_act,min(array_distancia)*ganancia_kilometro[0],
                               max(array_distancia)*ganancia_kilometro[0]) # normalizar
    # precio en linea recta al destino (clr)
    plr_act = dlr_act*precio_kilometro[0]
    plr_norm = normalizar(plr_act,min(array_distancia)*precio_kilometro[0],
                          max(array_distancia)*precio_kilometro[0]) # normalizar
    # heurística (mininimizar_distancia,minimizar_tiempo,maximizar_ganancia,minimizar_precio)
    h_x = dlr_norm*w1 + tlr_norm*w2 - glr_norm*w3 + plr_norm*w4
    return h_x  # Heurística trivial, no considera ninguna variable adicional

# Función para generar los vecinos de un nodo
def generar_vecinos(ciudad_actual):
    vecinos = []
    for city in mapa[ciudad_actual].keys():
        vecino = Nodo("",0,0,[])
        vecino.ciudad=city
        vecinos.append(vecino)
    return vecinos