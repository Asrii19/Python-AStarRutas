import math
from data import city_locations,city_time,city_ingresos,city_egresos,city_prices,city_prices_estudiante, mapa, pesos
from data import array_distancia, array_preciokilometro, array_tiempokilometro, array_gananciakilometro
from data import precio_kilometro, tiempo_kilometro, ganancia_kilometro,totales, nro_ejercicio

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

# funcion para calcular el tiempo entre 2 ciudades
def tiempo(ciudad_actual, vecino):
    time = city_time[ciudad_actual][vecino]
    return round(time,2)

# funcion para calcular la ganancia en una ciudad
def ganancia(vecino):
    earnings = city_ingresos[vecino]-city_egresos[vecino]
    return round(earnings,2)
# funcion para calcular el precio de viaje entre la ciudad actual y el vecino
def precio(ciudad_actual, vecino):
    if nro_ejercicio[0]==3:
        price = city_prices[ciudad_actual][vecino]
    elif(nro_ejercicio[0]==4):
        price = city_prices_estudiante[ciudad_actual][vecino]
    return round(price,2)

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
    ruta_tiempo = [] #tiempo de la ruta optima
    ruta_ganancia = [] #ganancia de la ruta optima
    ruta_precio = [] #precio de la ruta optima
    for i,city in enumerate(ruta):
        if not i+1 == len(ruta):
            if nro_ejercicio[0]==3:
                ruta_distancia.append(haversine(city,ruta[i+1]))
                ruta_tiempo.append(tiempo(city,ruta[i+1]))
                ruta_ganancia.append(ganancia(ruta[i+1]))
                ruta_precio.append(precio(city,ruta[i+1]))
            elif(nro_ejercicio[0]==4):
                ruta_distancia.append(haversine(city,ruta[i+1]))
                ruta_tiempo.append(tiempo(city,ruta[i+1]))
                ruta_precio.append(precio(city,ruta[i+1]))
    totales["distancia_total"] = sum(ruta_distancia)
    totales["tiempo_total"] = sum(ruta_tiempo)
    totales["ganancia_total"] = sum(ruta_ganancia)
    totales["precio_total"] = sum(ruta_precio)

def definir_data(numero_ejercicio): # para la normalización
    #definir diccionario 
    if numero_ejercicio==4:
        pesos["distancia"],pesos["tiempo"]=0.1,0.3
        pesos["ganancia"],pesos["precio"]=0,0.6
    elif(numero_ejercicio==3):
        pesos["distancia"],pesos["tiempo"]=0.25,0.4
        pesos["ganancia"],pesos["precio"]=0.25,0.1
        """ pesos["distancia"],pesos["tiempo"]=0.1,0.1
        pesos["ganancia"],pesos["precio"]=0.8,0 """
    nro_ejercicio.append(numero_ejercicio)
    print(pesos)
    #distancia
    for city1 in city_locations.keys():
        for city2 in city_locations.keys():
            array_distancia.append(haversine(city1,city2))
    #tiempo, ganancia y precio de viaje
    for city, neighbors in mapa.items(): # define un array con todos los precios posibles entre ciudades
        for neighbor in neighbors.keys():
            d=haversine(city,neighbor)
            t=tiempo(city,neighbor) #tiempo
            g=ganancia(neighbor) #ganancia
            p=precio(city,neighbor) #precio

            array_tiempokilometro.append(round(t/d,2))# tiempo a su vecino/distancia a su vecino
            array_gananciakilometro.append(round(g/d,2))# ganancia/ distancia a su vecino
            array_preciokilometro.append(round(p/d,2))# precio a su vecino/distancia a su vecino

            promedio_tiempokilometro = round(sum(array_tiempokilometro)/len(array_tiempokilometro),2)
            promedio_gananciakilometro = round(sum(array_gananciakilometro)/len(array_gananciakilometro),2)
            promedio_preciokilometro = round(sum(array_preciokilometro)/len(array_preciokilometro),2)
    tiempo_kilometro.append(promedio_tiempokilometro) # se define el tiempo promedio por unidad de distancia (km)
    ganancia_kilometro.append(promedio_gananciakilometro) # se define la ganancia estimafa por unidad de distancia (km)
    precio_kilometro.append(promedio_preciokilometro) # se define el precio promedio por unidad de distancia (km)
    print("DATOS: \n\tTiempoKm: ",tiempo_kilometro,
          "\n\tGananciaKm: ",ganancia_kilometro,"\n\tPrecioKm: ",precio_kilometro)