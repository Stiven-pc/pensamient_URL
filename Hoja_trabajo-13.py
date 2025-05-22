matriz = [
    [0,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
]

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(str(celda) for celda in fila))
    print()  

def siguiente_generacion(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    nueva_matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            vecinos_vivos = 0
            if j > 0:
                vecinos_vivos += tablero[i][j-1]
            if j < columnas-1:
                vecinos_vivos += tablero[i][j+1]

            
            if tablero[i][j] == 1:
                if vecinos_vivos == 1 or vecinos_vivos == 2:
                    nueva_matriz[i][j] = 1  
                else:
                    nueva_matriz[i][j] = 0  
            else:
                if vecinos_vivos == 1:
                    nueva_matriz[i][j] = 1  
                else:
                    nueva_matriz[i][j] = 0  

    return nueva_matriz

print("Generación 0:")
imprimir_tablero(matriz)

generacion_1 = siguiente_generacion(matriz)
print("Generación 1:")
imprimir_tablero(generacion_1)

generacion_2 = siguiente_generacion(generacion_1)
print("Generación 2:")
imprimir_tablero(generacion_2)
