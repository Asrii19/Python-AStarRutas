import math
from data import mapa
from metodos import hallar_maximos, haversine

# función evaluadora f(n)
def fevaluadora(ciudad_actual,vecino,destino,openset):
    #g(x)
    #OBTENER VARIABLES (4)
    distancia_act = haversine(ciudad_actual,vecino)

    g_x = openset[ciudad_actual][0] + distancia_act

    #h(x)
    #OBTENER VARIABLES (1)
    dlr_act = haversine(vecino,destino) #DISTANCIA RECTA DEL VECINO AL OBJETIVO

    h_x = dlr_act

    #f(x)
    f_x = g_x + h_x
    return g_x, f_x

# función de búsqueda A*
def astar_search(inicio, destino):
    ruta = [inicio] # lista de ciudades visitadas (ganador)
    closedset = set() # conjunto de ciudades visitadas y evaluadas
    openset = {inicio: (0,[inicio])} # conjunto de ciudades disponibles para visitar /(g(x) costo acumulado,ruta hasta el actual nodo)
    
    while ruta[-1] != destino: # siempre y cuando la ultima ciudad en el recorrido sea diferente, continúa
        openset_aux = {}
        vecinos = [] # lista de tuplas [resultado de f(n),vecinos no visitados]
        for ciudad_actual in openset.keys(): #SE EVALUAN LOS ELEMENTOS DEL OPENSET
            for vecino in mapa[ciudad_actual].keys() - closedset: #SE SACAN LOS VECINOS DEL ELEMENTO ACTUAL DEL OPENSET
                g_evaluada, f_evaluada = fevaluadora(ciudad_actual,vecino,destino,openset)
                
                ruta_aux = openset[ciudad_actual][1] + [vecino]
                #print("AUX: ",ruta_aux)

                tupla = (f_evaluada, vecino)
                if ciudad_actual == ruta[-1]:
                    vecinos.append(tupla)
                
                if vecino not in openset.keys(): # si el vecino no está en openset
                    openset_aux[vecino] = (g_evaluada,ruta_aux) # se añade a la lista
                else: #si ya estaba en la lista
                    if  g_evaluada>openset[vecino][0]: #se evalua la g
                        continue
            #SE AÑADE EL NODO EVALUADO
            closedset.add(ciudad_actual) # se agrega a los visitados y evaluados
        if not vecinos: # si el metodo se adelanta
            ruta1=astar_search(inicio,ruta[-1])
            ruta2=astar_search(ruta[-1],destino)
            return ruta1+ruta2
        _, ciudad_elegida = min(vecinos) # elegir el vecino con menor f(n) / el min("tupla") elige el valor mínimo del primer elemento
        
        ruta.append(ciudad_elegida) #se agrega a la ruta
        print("RUTAAA: ", ruta)
        for ciudad in closedset: # se eliminan los vecinos de las ciudades evaluadas del openset
            if ciudad in openset:
                del openset[ciudad] 
        openset.update(openset_aux)
    return ruta
