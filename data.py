import math
# coordenadas de las ciudades
city_locations = { #longitud, latitud
    "Washington": (-120.7401, 47.7511),
    "Oregon": (-122.3321, 43.8041),
    "California": (-119.4179, 36.7783),
    "Nevada": (-116.7939, 38.8026),
    "Idaho": (-114.7420, 44.0682),
    "Montana": (-110.4544, 46.8797),
    "Wyoming": (-107.2903, 43.0750),
    "Utah": (-111.0937, 39.3200),
    "Arizona": (-111.0937, 34.0489),
    "Colorado": (-105.7821, 39.5501),
    "Nuevo Mexico": (-106.2485, 34.5199),
    "Dakota del Norte": (-99.7840, 47.5515),
    "Dakota del Sur": (-99.4388, 44.3668),
    "Nebraska": (-99.9018, 41.4925),
    "Kansas": (-98.3804, 38.5266),
    "Texas": (-99.9018, 31.9686),
    "Oklahoma": (-97.5164, 35.0078),
    "Arkansas": (-92.3020, 34.7465),
    "Missouri": (-92.4638, 38.5733),
    "Iowa": (-93.0977, 41.8780)
}

mapa = {
    "Washington": {"Oregon": (-122.3321, 43.8041), "Idaho": (-114.7420, 44.0682)},
    "Oregon": {"Washington": (-120.7401, 47.7511), "California": (-119.4179, 36.7783), "Idaho": (-114.7420, 44.0682), "Nevada": (-116.7939, 38.8026)},
    "California": {"Oregon": (-122.3321, 43.8041), "Nevada": (-116.7939, 38.8026), "Arizona": (-111.0937, 34.0489)},
    "Nevada": {"Oregon": (-122.3321, 43.8041), "California": (-119.4179, 36.7783), "Arizona": (-111.0937, 34.0489), "Utah": (-111.0937, 39.3200), "Idaho": (-114.7420, 44.0682)},
    "Idaho": {"Washington": (-120.7401, 47.7511), "Oregon": (-122.3321, 43.8041), "Nevada": (-116.7939, 38.8026), "Utah": (-111.0937, 39.3200), "Wyoming": (-107.2903, 43.0750), "Montana": (-110.4544, 46.8797)},
    "Montana": {"Idaho": (-114.7420, 44.0682), "Wyoming": (-107.2903, 43.0750), "Dakota del Norte": (-99.7840, 47.5515), "Dakota del Sur": (-99.4388, 44.3668)},
    "Wyoming": {"Montana": (-110.4544, 46.8797), "Idaho": (-114.7420, 44.0682), "Utah": (-111.0937, 39.3200), "Colorado": (-105.7821, 39.5501), "Nebraska": (-99.9018, 41.4925), "Dakota del Sur": (-99.4388, 44.3668)},
    "Utah": {"Nevada": (-116.7939, 38.8026), "Idaho": (-114.7420, 44.0682), "Wyoming": (-107.2903, 43.0750), "Colorado": (-105.7821, 39.5501), "Arizona": (-111.0937, 34.0489)},
    "Arizona": {"California": (-119.4179, 36.7783), "Nevada": (-116.7939, 38.8026), "Utah": (-111.0937, 39.3200), "Nuevo Mexico": (-106.2485, 34.5199)},
    "Colorado": {"Wyoming": (-107.2903, 43.0750), "Nebraska": (-99.9018, 41.4925), "Kansas": (-98.3804, 38.5266), "Oklahoma": (-97.5164, 35.0078), "Nuevo Mexico": (-106.2485, 34.5199) , "Utah": (-111.0937, 39.3200)},
    "Nuevo Mexico": {"Arizona": (-111.0937, 34.0489), "Utah": (-111.0937, 39.3200), "Colorado": (-105.7821, 39.5501), "Oklahoma": (-97.5164, 35.0078), "Texas": (-99.9018, 31.9686)},
    "Dakota del Norte": {"Montana": (-110.4544, 46.8797), "Dakota del Sur": (-99.4388, 44.3668)},
    "Dakota del Sur": {"Montana": (-110.4544, 46.8797), "Wyoming": (-107.2903, 43.0750), "Nebraska": (-99.9018, 41.4925), "Iowa": (-93.0977, 41.8780), "Dakota del Norte": (-99.7840, 47.5515)},
    "Nebraska": {"Wyoming": (-107.2903, 43.0750), "Dakota del Sur": (-99.4388, 44.3668), "Iowa": (-93.0977, 41.8780), "Colorado": (-105.7821, 39.5501), "Kansas": (-98.3804, 38.5266), "Missouri": (-92.4638, 38.5733)},
    "Kansas": {"Colorado": (-105.7821, 39.5501), "Nebraska": (-99.9018, 41.4925), "Missouri": (-92.4638, 38.5733), "Oklahoma": (-97.5164, 35.0078)},
    "Texas": {"Nuevo Mexico": (-106.2485, 34.5199), "Oklahoma": (-97.5164, 35.0078), "Arkansas": (-92.3020, 34.7465)},
    "Oklahoma": {"Kansas": (-98.3804, 38.5266), "Nuevo Mexico": (-106.2485, 34.5199), "Texas": (-99.9018, 31.9686), "Arkansas": (-92.3020, 34.7465), "Missouri": (-92.4638, 38.5733)},
    "Arkansas": {"Missouri": (-92.4638, 38.5733), "Oklahoma": (-97.5164, 35.0078), "Texas": (-92.3020, 34.7465)},
    "Missouri": {"Iowa": (-93.0977, 41.8780), "Nebraska": (-99.9018, 41.4925), "Kansas": (-98.3804, 38.5266), "Oklahoma": (-97.5164, 35.0078), "Arkansas": (-92.3020, 34.7465)},
    "Iowa": {"Dakota del Sur": (-99.4388, 44.3668), "Nebraska": (-99.9018, 41.4925), "Missouri": (-92.4638, 38.5733)}
}

def hallar_maximos():
    array_distancias = []
    for city1 in city_locations.keys():
        for city2 in city_locations.keys():
            x1, y1 = city_locations[city1]
            x2, y2 = city_locations[city2]
            array_distancias.append(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    return array_distancias
