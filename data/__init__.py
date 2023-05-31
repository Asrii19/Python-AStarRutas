# coordenadas de las ciudades
city_locations = { #longitud, latitud
    "Amazonas": (-77.8697, -6.2329),
    "Ancash": (-77.5714, -9.4946),
    "Apurimac": (-73.0014, -14.0464),
    "Arequipa": (-71.5375, -16.4090),
    "Ayacucho": (-74.2247, -13.1639),
    "Cajamarca": (-78.8118, -7.1646),
    "Cusco": (-71.5375, -13.5319),
    "Huancavelica": (-74.9667, -12.7822),
    "Huanuco": (-76.2476, -9.9249),
    "Ica": (-75.7221, -14.0679),
    "Junin": (-75.1496, -11.1103),
    "La Libertad": (-79.0337, -8.1092),
    "Lambayeque": (-79.9062, -6.7714),
    "Lima": (-76.9974, -12.0464),
    "Madre De Dios": (-69.9597, -11.7669),
    "Moquegua": (-70.9352, -17.1939),
    "Pasco": (-76.2398, -10.6838),
    "Piura": (-80.6327, -5.1945),
    "Puno": (-70.0337, -15.8435),
    "San Martin": (-76.2450, -6.4963),
    "Tacna": (-70.2513, -18.0127),
    "Tumbes": (-80.4572, -3.5669),
    "Ucayali": (-73.4050, -9.2609)
}

# trazado de rutas
mapa = {
    "Amazonas": {"San Martin": (-76.2450, -6.4963), "Cajamarca": (-78.8118, -7.1646), "Piura": (-80.6327, -5.1945)},
    "Ancash": {"La Libertad": (-79.0337, -8.1092), "Lima": (-76.9974, -12.0464), "Huanuco": (-76.2476, -9.9249), "San Martin": (-76.2450, -6.4963)},
    "Apurimac": {"Ayacucho": (-74.2247, -13.1639), "Cusco": (-71.5375, -13.5319), "Arequipa": (-71.5375, -16.4090)},
    "Arequipa": {"Apurimac": (-73.0014, -14.0464),"Moquegua": (-70.9352, -17.1939), "Puno": (-70.0337, -15.8435), "Cusco": (-71.5375, -13.5319), "Ayacucho": (-74.2247, -13.1639), "Ica": (-75.7221, -14.0679)},
    "Ayacucho": {"Apurimac": (-73.0014, -14.0464), "Huancavelica": (-74.9667, -12.7822), "Arequipa": (-71.5375, -16.4090), "Cusco": (-71.5375, -13.5319)},
    "Cajamarca": {"Amazonas": (-77.8697, -6.2329), "Lambayeque": (-79.9062, -6.7714), "La Libertad": (-79.0337, -8.1092)},
    "Cusco": {"Apurimac": (-73.0014, -14.0464), "Arequipa": (-71.5375, -16.4090), "Madre De Dios": (-69.9597, -11.7669), "Puno": (-70.0337, -15.8435), "Ayacucho": (-74.2247, -13.1639)}, 
    "Huancavelica": {"Ayacucho": (-74.2247, -13.1639), "Junin": (-75.1496, -11.1103), "Ica": (-75.7221, -14.0679), "Lima": (-76.9974, -12.0464)},
    "Huanuco": {"Ancash": (-77.5714, -9.4946), "Pasco": (-76.2398, -10.6838), "Ucayali": (-73.4050, -9.2609)},
    "Ica": {"Arequipa": (-71.5375, -16.4090), "Huancavelica": (-74.9667, -12.7822), "Lima": (-76.9974, -12.0464)},
    "Junin": {"Pasco": (-76.2398, -10.6838), "Huancavelica": (-74.9667, -12.7822), "Lima": (-76.9974, -12.0464), "Ucayali": (-73.4050, -9.2609)},
    "La Libertad": {"Ancash": (-77.5714, -9.4946), "Lambayeque": (-79.9062, -6.7714), "Cajamarca": (-78.8118, -7.1646)},
    "Lambayeque": {"La Libertad": (-79.0337, -8.1092), "Cajamarca": (-78.8118, -7.1646), "Piura": (-80.6327, -5.1945)},
    "Lima": {"Ancash": (-77.5714, -9.4946), "Ica": (-75.7221, -14.0679), "Junin": (-75.1496, -11.1103), "Pasco": (-76.2398, -10.6838), "Huancavelica": (-74.9667, -12.7822)},
    "Madre De Dios": {"Puno": (-70.0337, -15.8435), "Cusco": (-71.5375, -13.5319)},
    "Moquegua": {"Tacna": (-70.2513, -18.0127), "Arequipa": (-71.5375, -16.4090), "Puno": (-70.0337, -15.8435)},
    "Pasco": {"Junin": (-75.1496, -11.1103), "Huanuco": (-76.2476, -9.9249), "Lima": (-76.9974, -12.0464), "Ucayali": (-73.4050, -9.2609)},
    "Piura": {"Lambayeque": (-79.9062, -6.7714), "Tumbes": (-80.4572, -3.5669), "Amazonas": (-77.8697, -6.2329)},
    "Puno": {"Cusco": (-71.5375, -13.5319), "Madre De Dios": (-69.9597, -11.7669), "Moquegua": (-70.9352, -17.1939), "Arequipa": (-71.5375, -16.4090), "Tacna": (-70.2513, -18.0127)},
    "San Martin": {"Amazonas": (-77.8697, -6.2329), "Ancash": (-77.5714, -9.4946)},
    "Tacna": {"Moquegua": (-70.9352, -17.1939), "Puno": (-70.0337, -15.8435)},
    "Tumbes": {"Piura": (-80.6327, -5.1945)},
    "Ucayali": {"Pasco": (-76.2398, -10.6838), "Huanuco": (-76.2476, -9.9249), "Junin": (-75.1496, -11.1103)}
}
# Tiempo/hora entre ciudad y ciudad
city_time = {
    "Amazonas": {"San Martin": (9), "Cajamarca": (11), "Piura": (6)},
    "Ancash": {"La Libertad": (4), "Lima": (8), "Huanuco": (7), "San Martin": (4)},
    "Apurimac": {"Ayacucho": (5), "Cusco": (4), "Arequipa": (9)},
    "Arequipa": {"Apurimac": (9), "Moquegua": (2), "Puno": (5), "Cusco": (7), "Ayacucho": (9), "Ica": (10)},
    "Ayacucho": {"Apurimac": (5), "Huancavelica": (6), "Arequipa": (9), "Cusco": (4)},
    "Cajamarca": {"Amazonas": (11), "Lambayeque": (3), "La Libertad": (3)},
    "Cusco": {"Apurimac": (4), "Arequipa": (7), "Madre De Dios": (11), "Puno": (11), "Ayacucho": (4)},
    "Huancavelica": {"Ayacucho": (6), "Junin": (5), "Ica": (4), "Lima": (4)},
    "Huanuco": {"Ancash": (7), "Pasco": (4), "Ucayali": (5)},
    "Ica": {"Arequipa": (10), "Huancavelica": (4), "Lima": (5)},
    "Junin": {"Pasco": (4), "Huancavelica": (5), "Lima": (4), "Ucayali": (7)},
    "La Libertad": {"Ancash": (4), "Lambayeque": (2), "Cajamarca": (3)},
    "Lambayeque": {"La Libertad": (2), "Cajamarca": (3), "Piura": (4)},
    "Lima": {"Ancash": (8), "Ica": (5), "Junin": (4), "Pasco": (4), "Huancavelica": (4)},
    "Madre De Dios": {"Puno": (11), "Cusco": (11)},
    "Moquegua": {"Tacna": (2), "Arequipa": (2), "Puno": (6)},
    "Pasco": {"Junin": (4), "Huanuco": (4), "Lima": (4), "Ucayali": (7)},
    "Piura": {"Lambayeque": (4), "Tumbes": (2), "Amazonas": (6)},
    "Puno": {"Cusco": (11), "Madre De Dios": (11), "Moquegua": (6), "Arequipa": (5), "Tacna": (5)},
    "San Martin": {"Amazonas": (9), "Ancash": (4)},
    "Tacna": {"Moquegua": (2), "Puno": (5)},
    "Tumbes": {"Piura": (2)},
    "Ucayali": {"Pasco": (7), "Huanuco": (5), "Junin": (7)}
}
# precio de viaje entre ciudad y ciudad
city_prices = {
    "Amazonas": {"San Martin": (35), "Cajamarca": (50), "Piura": (40)},
    "Ancash": {"La Libertad": (40), "Lima": (40), "Huanuco": (35), "San Martin": (30)},
    "Apurimac": {"Ayacucho": (22), "Cusco": (21), "Arequipa": (57)},
    "Arequipa": {"Apurimac": (57),"Moquegua": (19), "Puno": (29), "Cusco": (55), "Ayacucho": (50), "Ica": (60)},
    "Ayacucho": {"Apurimac": (22), "Huancavelica": (48), "Arequipa":(50), "Cusco": (22)},
    "Cajamarca": {"Amazonas": (50), "Lambayeque": (25), "La Libertad": (24)},
    "Cusco": {"Apurimac": (22), "Arequipa": (55), "Madre De Dios": (60), "Puno": (60), "Ayacucho": (22)}, 
    "Huancavelica": {"Ayacucho": (48), "Junin": (50), "Ica": (22), "Lima": (14)},
    "Huanuco": {"Ancash": (35), "Pasco": (23), "Ucayali": (25)},
    "Ica": {"Arequipa": (60), "Huancavelica": (22), "Lima": (24)},
    "Junin": {"Pasco": (40), "Huancavelica": (50), "Lima": (34), "Ucayali": (33)},
    "La Libertad": {"Ancash": (40), "Lambayeque": (45), "Cajamarca": (24)},
    "Lambayeque": {"La Libertad": (50), "Cajamarca": (25), "Piura": (50)},
    "Lima": {"Ancash": (40), "Ica": (24), "Junin": (34), "Pasco": (24), "Huancavelica": (14)},
    "Madre De Dios": {"Puno": (35), "Cusco": (60)},
    "Moquegua": {"Tacna": (45), "Arequipa": (19), "Puno": (55)},
    "Pasco": {"Junin": (40), "Huanuco": (23), "Lima": (24), "Ucayali": (80)},
    "Piura": {"Lambayeque": (50), "Tumbes": (13), "Amazonas": (40)},
    "Puno": {"Cusco": (60), "Madre De Dios": (35), "Moquegua": (55), "Arequipa": (29), "Tacna": (9)},
    "San Martin": {"Amazonas": (35), "Ancash": (30)},
    "Tacna": {"Moquegua": (45), "Puno": (9)},
    "Tumbes": {"Piura": (13)},
    "Ucayali": {"Pasco": (80), "Huanuco": (25), "Junin": (33)}
}
city_earnings={

}

# DATA PARA HALLAR COSTO
velocidad = 35 # km/h

# DATA PARA LA HEURÍSTICA
array_distancia=[]
array_tiempo=[]
ganancia_kilometro = []
array_gananciakilometro = []
precio_kilometro = []
array_preciokilometro=[]

# COSTO TOTAL
totales = {
    "distancia_total":0,
    "tiempo_total":0,
    "ganancia_total":0,
    "precio_total":0
}