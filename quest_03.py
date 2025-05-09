def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matirz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matirz += [fila]
    
    return matirz

matriz_a = inicializar_matriz(4, 4, 0)
matriz_b = inicializar_matriz(4, 4, 0)


def carga_matriz_secuencialmente(matriz:list):
    #Agrega validaciones/retorno que sean necesarias

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Fila {i} Columna {j}: "))

# carga_matriz_secuencialmente(matriz_a)


def cargar_matriz_aleatoriamente(matriz:list):
    #Agrega validaciones/retorno que sean necesarias
    seguir = "S"
    while seguir == "S":
        fila = int(input("Indice de fila: "))
        columna = int(input("Indice de columna: "))
        dato = int(input("Ingrese el número a cargar: "))
        matriz[fila][columna] = dato

        seguir = input("Desea seguir cargando? S/N: ")

def validar_mismo_tamanio_matriz(matriz_a: list[list], matriz_b: list[list]) -> bool:
    """
    Parámetros: Recibe 2 matrices
    
    ¿Qué hace?: Obtiene primero la cantidad de filas de cada matriz.
    Luego recorre la cantidad de columnas de cada matriz.
    Y al final, compara que tanto la matriz a, como la matriz b, sean
    idénticas

    ¿Qué Retorna?:Retorna un booleano con true en caso de que sean iguales
    O false en caso de que tengan distintas dimensiones. 
    """
    #Definimos las variables de filas y columnas
    filas_a = len(matriz_a)
    filas_b = len(matriz_b)
    columnas_a = 0
    columnas_b = 0

    print(f"filas_a: {filas_a}")
    print(f"filas_b: {filas_b}")
    #Recorremos la cantidad de columnas de cada matriz
    for index in range(filas_a):
        columnas_a += len(matriz_a[index])

    for column in range(len(matriz_b[index])):
        columnas_b += len(matriz_b[index])
    #Dividimos la cantidad de columnas por la cantidad de filas
    cantidad_columnas_a = columnas_a / filas_a
    cantidad_columnas_b = columnas_b / filas_b

    """ 
    Esto puede servir para calcular la cantidad de elementos de cada matriz
    for index in range(filas_b):
        for column in range(len(matriz_b[index])):
            columnas_b += column
    """

    #Creamos los valores para ver que coincidan filas y columnas
    igualdad_filas = filas_a == filas_b
    igualdad_columnas = cantidad_columnas_a == cantidad_columnas_b

    validacion = igualdad_filas & igualdad_columnas

    print(f"igualdad_filas: {igualdad_filas}")
    print(f"igualdad_columnas: {igualdad_columnas}")
    print(f"Validación: {validacion}")
    return validacion
    

def suma_matrices(matriz_a: list[list], matriz_b: list[list]) -> list[list]:
    matriz_resultante = []
    if validar_mismo_tamanio_matriz(matriz_a, matriz_b):
        pass
    else:
        print("ERROR: Las matrices no tienen el mismo tamaño.")
    return matriz_resultante

#cargar_matriz_aleatoriamente(matriz_a)

suma_matrices(matriz_a, matriz_b)

print(matriz_a)
