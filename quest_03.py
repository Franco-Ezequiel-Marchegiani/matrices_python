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

    #Recorremos la cantidad de columnas de cada matriz
    for index in range(filas_a):
        columnas_a += len(matriz_a[index])

    for column in range(len(matriz_b[index])):
        columnas_b += len(matriz_b[column])
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

    return validacion

def validar_multiplicacion_matriz(matriz_a: list[list], matriz_b: list[list]) -> bool:
    """
    Parámetros: Recibe 2 matrices
    
    ¿Qué hace?: Valida que la cantidad de columnas matriz A 
    sea igual que la cantidad de filas de la columna B

    ¿Qué Retorna?:Retorna un booleano con true 
    en caso de que sea válida la multiplicación, o false en caso contrario.
    """
    #Definimos las variables de filas y columnas
    columnas_a = 0
    filas_a = len(matriz_a)
    filas_b = len(matriz_b)

    #Recorremos la cantidad de columnas de la matriz A
    for index in range(len(matriz_a)):
        columnas_a += len(matriz_a[index])
    
    #Dividimos la cantidad de columnas por la cantidad de filas
    cantidad_columnas_a = columnas_a / filas_a

    #Creamos los valores para ver que coincidan filas y columnas
    validacion =  cantidad_columnas_a == filas_b
    print(f"validacion: {validacion}")
    return validacion


def suma_matrices(matriz_a: list[list], matriz_b: list[list]) -> list[list]:
    """
    Parámetros: Recibe 2 matrices
    
    ¿Qué hace?: Primero valida que se pueda realizar la suma entre matrices.
    Acto seguido inicializa una matriz con la cantidad de filas y columnas.
    Para posteriormente recorrer una matriz, para ir sumando los valores entre 
    ambas matrices, y guardar la suma en esta matriz nueva.

    ¿Qué Retorna?:Retorna una matriz que contiene la suma de ambas matrices.
    """
    matriz_resultante = []
    if validar_mismo_tamanio_matriz(matriz_a, matriz_b):
        matriz_resultante = inicializar_matriz(len(matriz_a), len(matriz_a[0]), None)
        print(f"Suma de Matrices:\n")

        for indice_fila in range(len(matriz_a)):
            for indice_columna in range(len(matriz_a[indice_fila])):
                resultado = matriz_a[indice_fila][indice_columna] + matriz_b[indice_fila][indice_columna]
                matriz_resultante[indice_fila][indice_columna] = resultado
                print(matriz_resultante[indice_fila][indice_columna], end=" ")
            print("")

    else:
        print("ERROR: Las matrices no tienen el mismo tamaño.")
    
    return matriz_resultante

def multiplicar_matrices_por_escalar(matriz_a: list[list], multiplo: int) -> list[list]:
    """
    Parámetros: Recibe 2 matrices
    
    ¿Qué hace?: Primero valida que se pueda realizar la suma entre matrices.
    Acto seguido inicializa una matriz con la cantidad de filas y columnas.
    Para posteriormente recorrer una matriz, para ir sumando los valores entre 
    ambas matrices, y guardar la suma en esta matriz nueva.

    ¿Qué Retorna?:Retorna una matriz que contiene la suma de ambas matrices.
    """

    matriz_resultante = inicializar_matriz(len(matriz_a), len(matriz_a[0]), None)
    print(f"Suma de Matrices:\n")

    for indice_fila in range(len(matriz_a)):
        for indice_columna in range(len(matriz_a[indice_fila])):
            resultado = matriz_a[indice_fila][indice_columna] * multiplo
            matriz_resultante[indice_fila][indice_columna] = resultado
            print(matriz_resultante[indice_fila][indice_columna], end=" ")
        print("")

    return matriz_resultante

def multiplicar_matrices(matriz_a: list[list], matriz_b: list[list]) -> list[list]:
    """
    Parámetros: Recibe 2 matrices
    
    ¿Qué hace?: Primero valida que se pueda realizar la suma entre matrices.
    Acto seguido inicializa una matriz con la cantidad de filas y columnas.
    Para posteriormente recorrer una matriz, para ir sumando los valores entre 
    ambas matrices, y guardar la suma en esta matriz nueva.

    ¿Qué Retorna?:Retorna una matriz que contiene el resultado 
    de la multiplicación  de ambas matrices.
    """

    if validar_multiplicacion_matriz(matriz_a, matriz_b):

        matriz_resultante = inicializar_matriz(len(matriz_a), len(matriz_b[0]), None)
        print(f"Multiplica las Matrices:\n")

        #Recorremos la cantidad de veces según las filas de la matriz A
        for indice_fila in range(len(matriz_a)):
            #Dentro, definimos el rango de la cantidad de Columnas de la matriz B
            for columnas_b in range(len(matriz_b[0])):
                #Definimos un valor inicial para guardar el elemento
                valor_a_guardar = 0
                valor_indice = 0
                #Recorremos las FILAS de la matriz B, la cantidad de veces según las columnas (ej: 4)
                for index_matriz_b in range(len(matriz_b)):
                    #Multiplicamos las matrices
                    resultado_multiplicacion = matriz_a[indice_fila][index_matriz_b] * matriz_b[index_matriz_b][columnas_b]
                    #Una vez obtenida la multiplicación, lo asignamos a "valor_indice"
                    #Para que quede el histórico de cuentas y multiplicaciones de este elemento 
                    valor_indice += resultado_multiplicacion

                #Asignamos el valor_indice final, ya con la suma de las multiplicaciones
                valor_a_guardar = valor_indice
                #Y lo asignamos en la posición correspondiente de esta nueva matriz
                matriz_resultante[indice_fila][columnas_b] = valor_a_guardar

    else:
        print("ERROR: No se puede multiplicar las matrices.")

    print(f"matriz_resultante: {matriz_resultante}")
    return matriz_resultante
#cargar_matriz_aleatoriamente(matriz_a)

matriz_1 = [
    [2,3],
    [-2,9],
    [6,-4],
]
matriz_2 = [
    [-2,8,5,3],
    [5,-6,7,-7],

]
#suma_matrices(matriz_1, matriz_2)
#multiplicar_matrices_por_escalar(matriz_1, 3)
multiplicar_matrices(matriz_1, matriz_2)