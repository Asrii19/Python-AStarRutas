import os
from metodos.a_estrella import astar_search
from metodos.grafico import graficar
from metodos import encontrar_coordenadas, encontrar_ciudad, hallar_totales, definir_data
if __name__ == "__main__":
    #limpiar pantalla
    os.system("cls")
    #si es el problema 3 o 4
    while True:
        numero_ejercicio=int(input("¿Resolverás el problema 3 o 4? (Conferencista = 3 / Estudiante = 4): "))
        if(numero_ejercicio==3 or numero_ejercicio==4):
            os.system("cls")
            break
        os.system("cls")
    while True:
        bandera, start=encontrar_ciudad(str(input("Ingrese el punto de inicio: ")).title())
        if bandera == True:
            break
        else:
            print(f"\tNo se encontró la ciudad {start}, por favor digite otra ciudad.")
    while True:
        bandera, goal=encontrar_ciudad(str(input("Ingrese el punto de llegada: ")).title())
        if bandera == True:
            break
        else:
            print(f"\tNo se encontró la ciudad {goal}, por favor digite otra ciudad.")
    
    definir_data(numero_ejercicio)
    path = astar_search(start,goal)

    path_x, path_y = encontrar_coordenadas(path)
    hallar_totales(path) #se hallan los totales y se modifica en data
    print("Ruta elegida: ",path)
    graficar(path_x,path_y)