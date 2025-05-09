from utn_fra.datasets import matriz_data_heroes_small

list_nombre_heroes = matriz_data_heroes_small[0]
list_nombres = matriz_data_heroes_small[1]
list_nombre_civil = matriz_data_heroes_small[2]
list_genero = matriz_data_heroes_small[3]
list_poder = matriz_data_heroes_small[4]
list_altura = matriz_data_heroes_small[5]


for index in range(len(matriz_data_heroes_small)):
    print(f"Array N°{index}")
    print(matriz_data_heroes_small[index])
    
#1
def mostrar_nombre(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Recorre la lista dentro de la matriz para mostrar el nombre de los héroes

    ¿Qué retorna?: Nada, solo muestra un print del listado
    '''

    print("Listado de nombres de Héroes: ")
    for index in range(len(matriz[0])):
        print(matriz[0][index])

#2
def mostrar_nombre_y_altura(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Recorre la lista dentro de la matriz y muestra el nombre y altura de los héroes

    ¿Qué retorna?: Nada, solo muestra un print del listado
    '''

    print("Listado de nombres de Héroes junto a su altura: ")
    for index in range(len(matriz[0])):
        print(f"Nombre: {matriz[0][index]} \n Altura: {matriz[5][index]} \n")
        #for name in range()

#3
def mostrar_personaje_debil(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Recorre la lista dentro de la matriz, averigua cual es el que tiene el poder más débil,
    y muestra los datos delmismo.

    ¿Qué retorna?: Hace un print del heroe más debil
    '''

    print("Listado de nombres de Héroes junto a su altura: ")
    max_valor = 100
    indice_heroe = 0
    for index in range(len(matriz[4])):
        if matriz[4][index] < max_valor:
            max_valor = matriz[4][index]
            indice_heroe = index
        
        print(max_valor)
        print(f"Índice de héroe más débil hasta el momento: {indice_heroe}")

    print("\nInformación sobre Héroe más débil:")
    for index in range(len(matriz)):
        print(matriz[index][indice_heroe])

#Como Extra, Pensar en una función con un parámetro extra, que si es mayor o menor, que devuelva un valor o el otro

#4
def mostrar_personaje_fuerte(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Recorre la lista dentro de la matriz, y el último héroe que tenga 100 de poder, 
    devuelve información de ese valor

    ¿Qué retorna?: Hace un print del heroe más fuerte
    '''

    print("Listado de nombres de Héroes junto a su altura: ")
    max_valor = 100
    indice_heroe = -1
    for index in range(len(matriz[4])):
        if matriz[4][index] == max_valor:
            indice_heroe = index

        print(f"Índice de héroe más fuerte hasta el momento: {indice_heroe}")

    print("\nInformación sobre Héroe más potro:")
    for index in range(len(matriz)):
        print(matriz[index][indice_heroe])


#5 OPTIMIZAR JUNTO A LA FUNCIÓN 8, PARA QUE CAMBIE EL PARÁMETRO DE LA MATRIZ A LA CUAL TRAE INFO.
#Ya que en ambos calcula un promedio, en un lado la altura, y en otro el poder. Se re puede optimizar eso.
def mostrar_altura_promedio(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Recorre la lista dentro de la matriz, 
    y calcula el promedio de la altura de los personajes

    ¿Qué retorna?: Hace un print del heroe más fuerte
    '''

    print("Listado de nombres de Héroes junto a su altura: ")
    contenedor = 0
    for index in range(len(matriz[5])):
        contenedor += matriz[5][index]

    promedio = contenedor / len(matriz[5])
    print(f"\nLa altura promedio de los héroes es de: {promedio}")

#6
def mostrar_poder_promedio(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Recorre la lista dentro de la matriz, 
    y calcula el promedio del poder de los personajes. 
    Para luego dividirlo a la mitad

    ¿Qué retorna?: Hace un print del heroe más fuerte
    '''

    print("Listado de nombres de Héroes junto a su altura: ")
    contenedor = 0
    for index in range(len(matriz[4])):
        contenedor += matriz[4][index]

    promedio = contenedor / len(matriz[4])
    mitad_promedio = promedio / 2
    print(f"\nLa mitad del promedio de poder los héroes es de: {mitad_promedio}")

#7
#OPTIMIZAR FUNCIÓN, CON UNA FUNCIÓN INTERNA EN DONDE SE AÑADE PARÁMETRO PARA BUSCAR AL MÁS ALTO O MÁS BAJO
def mostrar_personaje_alto_bajo(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Recorre la lista dentro de la matriz, 
    e informa el personaje más alto y bajo

    ¿Qué retorna?: Hace un print de los heroe más alto y bajo
    '''

    print("Listado de nombres de Héroes junto a su altura: ")
    valor_referencia_alto = matriz[5][0] #El primer héroe de la lista
    valor_referencia_bajo = matriz[5][0] #El primer héroe de la lista
    indice_heroe_alto = -1
    indice_heroe_bajo = -1
    # 6100 & 5.22,
    for index in range(len(matriz[5])):

        if matriz[5][index] < valor_referencia_bajo:
            valor_referencia_bajo = matriz[5][index]
            indice_heroe_bajo = index
        if matriz[5][index] > valor_referencia_alto:
            valor_referencia_alto = matriz[5][index]
            indice_heroe_alto = index
        

        #print(f"Índice de héroe más alto hasta el momento: {indice_heroe_alto}")
        print(f"Índice de héroe más bajo hasta el momento: {indice_heroe_bajo}")

    print(f"\nÍndice de héroe más alto y bajo: {indice_heroe_alto} & {indice_heroe_bajo}:")
    print("\nInformación sobre Héroe más alto:")
    #Info de héroe más alto
    for index in range(len(matriz)):
        print(matriz[index][indice_heroe_alto])

    print("\nInformación sobre Héroe más bajo:")
    #Info de héroe más bajo
    for index in range(len(matriz)):
        print(matriz[index][indice_heroe_bajo])

#8
def mostrar_poder_promedio(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Recorre la lista dentro de la matriz, 
    y calcula el promedio de poder de los personajes.
    Acto seguido, muestra el apodo de los héroes 
    que superan el promedio

    ¿Qué retorna?: Hace un print del heroe más fuerte
    '''

    print("Listado de nombres de Héroes junto a su altura: ")
    contenedor = 0
    #Recorremos el promedio
    for index in range(len(matriz[4])):
        contenedor += matriz[4][index]

    promedio = contenedor / len(matriz[4])
    #Volvemos a recorrer ya con el promedio para ver qué heroes lo superan
    listado_heroes_promedio = []
    #Almacenamos en un listado los heroes que superen promedio
    for index in range(len(matriz[4])):
        if matriz[4][index] > promedio:
            listado_heroes_promedio.append(index)
    
    #Recorremos el listado de buen promedio, y mostramos sus nombres (y más info de ser necesaria)
    print("Información de héroes por encima del promedio: ")
    """ for index in range(len(matriz)):

        for heroe in range(len(listado_heroes_promedio)):
            print(matriz[index][heroe]) """
    #Acá muestra solo el nombre, pero con lo de arriba recorre todo, solo que en listas distintas.
    for heroe in range(len(listado_heroes_promedio)):
        print(matriz[0][heroe])

    print(f"\nLa altura promedio de los héroes es de: {promedio}")
#9
def calcular_total_heroes(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Calcula el total de héroes que se encuentra en la matriz. 
    Para ello recorre cada lista dentro de la matriz, para asegurarse de devolver
    el valor más alto.

    ¿Qué retorna?: Muestra un print del largo del listado
    '''
    contenedor = 0
    for index in range(len(matriz)):
        print(len(matriz[index]))
        if contenedor < len(matriz[index]):
            contenedor = len(matriz[index])
    
    print(f"Fila más larga de la matriz: {contenedor}")
#10
def mostrar_genero_personaje(matriz: list[list]) -> None:
    '''
    Parámetros que recibe: La matríz principal
    
    ¿Qué hace?: Recorre la lista dentro de la matriz, 
    calcula la cantidad de héroes según su género.

    ¿Qué retorna?: Hace un print de la cantidad de héroes:
    Masculinos, Femeninos y No-Binarios
    '''

    print("Listado de nombres de Héroes junto a su altura: ")
    contador_mas = 0
    contador_fem = 0
    contador_nob = 0
    # 6100 & 5.22,
    for index in range(len(matriz[3])):

        if matriz[3][index] == "Masculino":
            contador_mas += 1
            
        elif matriz[3][index] == "Femenino":
            contador_fem += 1
        else:
            contador_nob += 1

    print(f"Listado de género de héroes: ")
    print(f"Genero Masculino: {contador_mas}")
    print(f"Genero Femenino: {contador_fem}")
    print(f"Genero No-Binario: {contador_nob}")



# mostrar_nombre(matriz_data_heroes_small)
#mostrar_nombre_y_altura(matriz_data_heroes_small)
#mostrar_personaje_debil(matriz_data_heroes_small)
#mostrar_personaje_fuerte(matriz_data_heroes_small)
#mostrar_altura_promedio(matriz_data_heroes_small)
#mostrar_personaje_alto_bajo(matriz_data_heroes_small)
#mostrar_poder_promedio(matriz_data_heroes_small)
#calcular_total_heroes(matriz_data_heroes_small)
mostrar_genero_personaje(matriz_data_heroes_small)

#0 Alias
#1 Nombre Completo Civil
#2 Apodo / Cómo es conocido
#3 Genero
#4 Nivel Poder
#5 Altura