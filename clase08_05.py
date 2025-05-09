""" from utn_fra.datasets import {
    lista_autos_marcas,
    lista_autos_modelos,
    lista_autos_cantidades,
    lista_autos_precios,
    lista_autos_ganancias,
} """


def buscar_en_matriz(matriz: list[list], indice_donde_buscar: int, valor_a_buscar: str) -> int:
    indice_encontrado = -1
    indice = 0
    for indice in range(len(matriz[indice_donde_buscar])):
        if matriz[indice_donde_buscar][indice] == valor_a_buscar:
            indice_encontrado = indice
            break
    # O
    while indice < len(matriz[indice_donde_buscar]):
        if matriz[indice_donde_buscar][indice] == valor_a_buscar:
            indice_encontrado = indice
            break
        indice += 1

    return indice_encontrado

def buscar_en_matriz(matriz: list[list], indice_donde_buscar: int, valor_a_buscar: str) -> list[list]:
    lista_indices_encontrados = []
    indice = 0

    while indice < len(matriz[indice_donde_buscar]):
        if matriz[indice_donde_buscar][indice] == valor_a_buscar:
            lista_indices_encontrados.append(indice)
            
            
        indice += 1
    
    return lista_indices_encontrados

def mostrar_informacion_de_autos(matriz: list[list], indice_donde_buscar: int, valor_a_buscar: str) -> None:
    lista_indices = buscar_en_matriz(matriz, indice_donde_buscar, valor_a_buscar)

    for indice_columna in range(lista_indices):

        indice_elegido = lista_indices[indice_columna]
        
        texto = ''
        for indice_fila in range(len(matriz)):
            dato = matriz[indice_fila][indice_elegido]
            if type(dato) == str:
                texto = f'{texto} | {dato:10}'
            elif type(dato) == int:
                texto = f'{texto} | {dato:07}'
            elif type(dato) == float:
                texto = f'{texto} | {dato:7.2}'
        texto = f'{texto} |'
        print(matriz[indice_fila][indice_elegido])

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matirz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matirz += [fila]
    
    return matirz
def crear_matriz_traspuesta(matriz_a: list[list]) -> list[list]:
    #Recorrer columnas x Filas
    cant_columnas = len(matriz_a[0])
    cant_filas = len(matriz_a)
    matriz_resultante = inicializar_matriz(cant_columnas, cant_filas, None)

    for indice_columna in range(cant_columnas):
        for indice_fila in range(cant_filas):
            matriz_resultante[indice_columna[indice_fila]] = matriz_a[indice_fila][indice_columna]
    
    return matriz_resultante

def mostrar_matriz(matriz_t: list[list]) -> None:
    
    for fila in range(len(matriz_t)):
        texto = ''
        for columna in range(len(matriz_t[fila])):
            dato = matriz_t[fila][columna]
            if type(dato) == float:
                texto = f'{texto} | {dato:08.1f}' #Al ponerle la f, indicamos que NO lo tome cono N° grande, para que no muestre texto
            else:
                texto = f'{texto} | {dato}'
        texto = f'{texto} |'
        print(texto)

mostrar_informacion_de_autos([[]], indice_donde_buscar=1, valor_a_buscar='Argo')