def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list[list]:
    """
    Parámetros: La cantidad de filas, columnas, y en caso de tener, un valor inicial opcional
    
    ¿Qué hace?: Tomando en cuenta los valor por parámetros, crea un listado
    Que se almacena en una lista vacía, lo cual al final del proceso termina creando
    una matriz. Con la cantidad de filas y columnas indicadas por el usuario. Como
    así también un valor por defecto (en caso de tener uno).

    ¿Qué Retorna?: Retorna una matriz, una lista de listas. 
    """
    matirz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matirz += [fila]
    
    return matirz

def carga_matriz_secuencialmente(matriz:list) -> None:
    """
    Parámetros: Una matriz con una estructura para recorrer
    
    ¿Qué hace?: Toma la matriz obtenida por parámetro para recorrerla.
    Y para cada elemento de la matriz, arroja un input al usuario para que 
    coloque el valor numérico que desee para "poblar" la matriz
    (asegurando que sea un válido). 
    IMPORTANTE: Solo acepta valores enteros y positivos.

    ¿Qué Retorna?: No retorna nada puntualmente, pero ya actualiza el 
    valor de la matriz que se pasó por parámetro sin necesidad de retornarla 
    """
    #Agrega validaciones/retorno que sean necesarias

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            nuevo_valor = None
            while nuevo_valor == None or not nuevo_valor.isdigit():
                nuevo_valor = input(f"Fila {i} Columna {j}: ")
                matriz[i][j] = int(nuevo_valor)

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
    return validacion


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

    #Visualización más acorde de la Matriz
    print(f"Matriz Multiplicada: ")
    for index in range(len(matriz_resultante)):
        for column in range(len(matriz_resultante[index])):
            print(matriz_resultante[index][column], end=" ")
        print("")
    return matriz_resultante
#cargar_matriz_aleatoriamente(matriz_a)

#Matrices de ejemplos
matriz_1 = [
    [5,3],
    [-2,9],
    [7,-4],
]
matriz_2 = [
    [-2,8,5,3],
    [5,-6,7,-7],
]

multiplicar_matrices(matriz_1, matriz_2)

#--- Shortcut de función para crear matrices personalizadas y multiplicarlas: --- 
    #Elegir cantidad de filas y columnas de c/ matriz
# matriz_a = inicializar_matriz(3, 2, 0)
# matriz_b = inicializar_matriz(2, 4, 0)
# print(f"matriz_a: {matriz_a}")
# print(f"matriz_b: {matriz_b}")
    #Cargar los datos de las mismas:
# carga_matriz_secuencialmente(matriz_a)
# carga_matriz_secuencialmente(matriz_b)
    #Enviar por parámetro las mismas funciones para multiplicar
# multiplicar_matrices(matriz_a, matriz_b)