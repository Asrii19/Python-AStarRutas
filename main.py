from metodos.a_estrella import astar_search
from metodos.grafico import graficar
from metodos import encontrar_coordenadas

if __name__ == "__main__":
    start=str(input("Ingrese el punto de inicio: ")).capitalize()
    goal=str(input("Ingrese el punto de llegada: ")).capitalize()
    path = astar_search(start,goal)

    path_x, path_y = encontrar_coordenadas(path)

    graficar(path_x,path_y)
    print(path)