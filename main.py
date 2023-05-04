from metodos.a_estrella import astar_search
from metodos.grafico import graficar
from metodos import encontrar_coordenadas, encontrar_ciudad, hallar_totales, hallar_maximos

if __name__ == "__main__":
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
    
    hallar_maximos(goal)

    path = astar_search(start,goal)

    path_x, path_y = encontrar_coordenadas(path)
    hallar_totales(path) #se hallan los totales y se modifica en data
    print(path)
    graficar(path_x,path_y)