import matplotlib.pyplot as plt
from data import city_locations, mapa, totales, nro_ejercicio

def graficar(path_x,path_y):
    titulo=""
    if nro_ejercicio[0]==3:
        titulo="Conferencista"
    elif nro_ejercicio[0]==4:
        titulo="Estudiante"
    #OBTENER DATOS (COORDENADAS) DEL MAPA
    labels = [city_location for city_location in city_locations.keys()]
    array_x = [city_location[0] for city_location in city_locations.values()]
    array_y = [city_location[1] for city_location in city_locations.values()]

    # Graficar los PUNTOS 
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(array_x, array_y) #GRAFICAR LOS PUNTOS
    
    #graficar ruta
    for point,value1 in mapa.items():
        for value2 in value1.values():
            x1=city_locations[point][0]
            x2=value2[0]
            y1=city_locations[point][1]
            y2=value2[1]
            ax.plot([x1,x2],[y1,y2], color='#A0CBE2') #UNIR LOS PUNTOS

    #graficar menor ruta y añadir etiquetas
    plt.plot(path_x,path_y, color='red') #UNIR LOS PUNTOS
    for i, txt in enumerate(labels): #AGREGA LA DESCRIPCIÓN A CADA PUNTO
        ax.annotate(txt, (array_x[i], array_y[i])) 

    # Añadir títulos y etiquetas de los ejes
    #variables a mostrar
    distancia = round(totales.get("distancia_total"),2)
    precio = round(totales.get("precio_total"),2)
    tiempo = round(totales.get("tiempo_total"),2)
    ganancia = round(totales.get("ganancia_total",2))
    moneda = "USD"
    ax.text(-0.05, -0.08, f"Distancia: {distancia}km, Tiempo: {tiempo}h",
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'),
        ha='left', va='top',
        transform=ax.transAxes) #cuadro de texto mostrando los valores de las variables
    ax.text(0.75, -0.08, f"Ganancia: {ganancia} {moneda}, Precio: {precio} {moneda}",
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'),
        ha='left', va='top',
        transform=ax.transAxes) #cuadro de texto mostrando los valores de las variables
    ax.set_title(f'Ruta con A* - {titulo}')
    ax.set_xlabel('Longitud')
    ax.set_ylabel('Latitud')
    
    # Mostrar la gráfica
    plt.grid(True)
    plt.show()