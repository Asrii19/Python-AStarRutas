import matplotlib.pyplot as plt
from data import city_locations, mapa, totales

def graficar(path_x,path_y):
    #OBTENER DATOS (COORDENADAS) DEL MAPA
    labels = [city_location for city_location in city_locations.keys()]
    array_x = [city_location[0] for city_location in city_locations.values()]
    array_y = [city_location[1] for city_location in city_locations.values()]

    # Graficar los PUNTOS 
    fig, ax = plt.subplots()
    ax.scatter(array_x, array_y) #GRAFICAR LOS PUNTOS
    
    #graficar ruta
    for point,value1 in mapa.items():
        for value2 in value1.values():
            x1=city_locations[point][0]
            x2=value2[0]
            y1=city_locations[point][1]
            y2=value2[1]
            ax.plot([x1,x2],[y1,y2], color='#bbbbbb') #UNIR LOS PUNTOS

    #graficar menor ruta y añadir etiquetas
    plt.plot(path_x,path_y, color='red') #UNIR LOS PUNTOS
    for i, txt in enumerate(labels): #AGREGA LA DESCRIPCIÓN A CADA PUNTO
        ax.annotate(txt, (array_x[i], array_y[i])) 

    # Añadir títulos y etiquetas de los ejes
    distancia = round(totales.get("distancia_total"),2)
    precio = round(totales.get("precio_total"),2)
    ax.text(-0.1, -0.08, f"Distancia: {distancia}km, Precio: {precio}$",
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'),
        ha='left', va='top',
        transform=ax.transAxes)
    ax.set_title('Ruta con A*')
    ax.set_xlabel('Longitud')
    ax.set_ylabel('Latitud')
    
    # Mostrar la gráfica
    plt.show()