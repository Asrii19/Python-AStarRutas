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
    "Dakota Del Norte": (-99.7840, 47.5515),
    "Dakota Del Sur": (-99.4388, 44.3668),
    "Nebraska": (-99.9018, 41.4925),
    "Kansas": (-98.3804, 38.5266),
    "Texas": (-99.9018, 31.9686),
    "Oklahoma": (-97.5164, 35.0078),
    "Arkansas": (-92.3020, 34.7465),
    "Missouri": (-92.4638, 38.5733),
    "Iowa": (-93.0977, 41.8780)
}

city_prices = {
    "Washington": {"Oregon": (142), "Idaho": (115)},
    "Oregon": {"Washington": (142), "California": (132), "Idaho": (108), "Nevada": (163)},
    "California": {"Oregon": (132), "Nevada": (74), "Arizona": (398)},
    "Nevada": {"Oregon": (163), "California": (74), "Arizona": (313), "Utah": (109), "Idaho": (211)},
    "Idaho": {"Washington": (115), "Oregon": (108), "Nevada": (211), "Utah": (121), "Wyoming": (138), "Montana": (118)},
    "Montana": {"Idaho": (118), "Wyoming": (206), "Dakota Del Norte": (191), "Dakota Del Sur": (210)},
    "Wyoming": {"Montana": (206), "Idaho": (138), "Utah": (65), "Colorado": (62), "Nebraska": (117), "Dakota Del Sur": (123)},
    "Utah": {"Nevada": (109), "Idaho": (121), "Wyoming": (65), "Colorado": (89),"Nuevo Mexico": (116), "Arizona": (106)},
    "Arizona": {"California": (398), "Nevada": (313), "Utah": (109), "Nuevo Mexico": (56)},
    "Colorado": {"Wyoming": (62), "Nebraska": (117), "Kansas": (112), "Oklahoma": (140), "Nuevo Mexico": (101) , "Utah": (89)},
    "Nuevo Mexico": {"Arizona": (56), "Utah": (116), "Colorado": (101), "Oklahoma": (123), "Texas": (152)},
    "Dakota Del Norte": {"Montana": (191), "Dakota Del Sur": (70)},
    "Dakota Del Sur": {"Montana": (210), "Wyoming": (123), "Nebraska": (129), "Iowa": (90), "Dakota Del Norte": (70)},
    "Nebraska": {"Wyoming": (117), "Dakota Del Sur": (129), "Iowa": (263), "Colorado": (117), "Kansas": (115), "Missouri": (129)},
    "Kansas": {"Colorado": (112), "Nebraska": (115), "Missouri": (109), "Oklahoma": (101)},
    "Texas": {"Nuevo Mexico": (152), "Oklahoma": (116), "Arkansas": (176)},
    "Oklahoma": {"Kansas": (101), "Nuevo Mexico": (123), "Texas": (116), "Arkansas": (160), "Missouri": (158)},
    "Arkansas": {"Missouri": (157), "Oklahoma": (160), "Texas": (176)},
    "Missouri": {"Iowa": (186), "Nebraska": (129), "Kansas": (109), "Oklahoma": (158), "Arkansas": (157)},
    "Iowa": {"Dakota Del Sur": (90), "Nebraska": (263), "Missouri": (186)}
}

mapa = {
    "Washington": {"Oregon": (-122.3321, 43.8041), "Idaho": (-114.7420, 44.0682)},
    "Oregon": {"Washington": (-120.7401, 47.7511), "California": (-119.4179, 36.7783), "Idaho": (-114.7420, 44.0682), "Nevada": (-116.7939, 38.8026)},
    "California": {"Oregon": (-122.3321, 43.8041), "Nevada": (-116.7939, 38.8026), "Arizona": (-111.0937, 34.0489)},
    "Nevada": {"Oregon": (-122.3321, 43.8041), "California": (-119.4179, 36.7783), "Arizona": (-111.0937, 34.0489), "Utah": (-111.0937, 39.3200), "Idaho": (-114.7420, 44.0682)},
    "Idaho": {"Washington": (-120.7401, 47.7511), "Oregon": (-122.3321, 43.8041), "Nevada": (-116.7939, 38.8026), "Utah": (-111.0937, 39.3200), "Wyoming": (-107.2903, 43.0750), "Montana": (-110.4544, 46.8797)},
    "Montana": {"Idaho": (-114.7420, 44.0682), "Wyoming": (-107.2903, 43.0750), "Dakota Del Norte": (-99.7840, 47.5515), "Dakota Del Sur": (-99.4388, 44.3668)},
    "Wyoming": {"Montana": (-110.4544, 46.8797), "Idaho": (-114.7420, 44.0682), "Utah": (-111.0937, 39.3200), "Colorado": (-105.7821, 39.5501), "Nebraska": (-99.9018, 41.4925), "Dakota Del Sur": (-99.4388, 44.3668)},
    "Utah": {"Nevada": (-116.7939, 38.8026), "Idaho": (-114.7420, 44.0682), "Wyoming": (-107.2903, 43.0750), "Colorado": (-105.7821, 39.5501),"Nuevo Mexico": (-106.2485, 34.5199), "Arizona": (-111.0937, 34.0489)},
    "Arizona": {"California": (-119.4179, 36.7783), "Nevada": (-116.7939, 38.8026), "Utah": (-111.0937, 39.3200), "Nuevo Mexico": (-106.2485, 34.5199)},
    "Colorado": {"Wyoming": (-107.2903, 43.0750), "Nebraska": (-99.9018, 41.4925), "Kansas": (-98.3804, 38.5266), "Oklahoma": (-97.5164, 35.0078), "Nuevo Mexico": (-106.2485, 34.5199) , "Utah": (-111.0937, 39.3200)},
    "Nuevo Mexico": {"Arizona": (-111.0937, 34.0489), "Utah": (-111.0937, 39.3200), "Colorado": (-105.7821, 39.5501), "Oklahoma": (-97.5164, 35.0078), "Texas": (-99.9018, 31.9686)},
    "Dakota Del Norte": {"Montana": (-110.4544, 46.8797), "Dakota Del Sur": (-99.4388, 44.3668)},
    "Dakota Del Sur": {"Montana": (-110.4544, 46.8797), "Wyoming": (-107.2903, 43.0750), "Nebraska": (-99.9018, 41.4925), "Iowa": (-93.0977, 41.8780), "Dakota Del Norte": (-99.7840, 47.5515)},
    "Nebraska": {"Wyoming": (-107.2903, 43.0750), "Dakota Del Sur": (-99.4388, 44.3668), "Iowa": (-93.0977, 41.8780), "Colorado": (-105.7821, 39.5501), "Kansas": (-98.3804, 38.5266), "Missouri": (-92.4638, 38.5733)},
    "Kansas": {"Colorado": (-105.7821, 39.5501), "Nebraska": (-99.9018, 41.4925), "Missouri": (-92.4638, 38.5733), "Oklahoma": (-97.5164, 35.0078)},
    "Texas": {"Nuevo Mexico": (-106.2485, 34.5199), "Oklahoma": (-97.5164, 35.0078), "Arkansas": (-92.3020, 34.7465)},
    "Oklahoma": {"Kansas": (-98.3804, 38.5266), "Nuevo Mexico": (-106.2485, 34.5199), "Texas": (-99.9018, 31.9686), "Arkansas": (-92.3020, 34.7465), "Missouri": (-92.4638, 38.5733)},
    "Arkansas": {"Missouri": (-92.4638, 38.5733), "Oklahoma": (-97.5164, 35.0078), "Texas": (-92.3020, 34.7465)},
    "Missouri": {"Iowa": (-93.0977, 41.8780), "Nebraska": (-99.9018, 41.4925), "Kansas": (-98.3804, 38.5266), "Oklahoma": (-97.5164, 35.0078), "Arkansas": (-92.3020, 34.7465)},
    "Iowa": {"Dakota Del Sur": (-99.4388, 44.3668), "Nebraska": (-99.9018, 41.4925), "Missouri": (-92.4638, 38.5733)}
}

# DATA PARA HALLAR COSTO
velocidad = 35 # km/h

# DATA PARA LA HEURÍSTICA
array_distancia=[]
array_preciokilometro=[]
array_tiempo=[]

precio_kilometro = []

# COSTO TOTAL
totales = {
    "distancia_total":0,
    "precio_total":0,
    "tiempo_total":0
}