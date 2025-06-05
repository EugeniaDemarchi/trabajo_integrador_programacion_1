# Itera cada elemento y lo va comparando con su adyacente.
# Si es mayor, lo mueve un lugar en la lista y sigue comparando
# Parametro key para definir atributo a ordenar
def bubble_sort(lista, key=lambda x: x):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if key(lista[j]) > key(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Divide la lista en mitades hasta que cada lista tenga un solo elemento,
# se utiliza la recursividad y un condicional que verifica cuando exista un elemento en la lista y da por finalizada la recursión
# Parametro key para definir atributo a ordenar
def merge_sort(lista, key=lambda x: x):
    # Condición para detener la recursión
    if len(lista) == 1:
        return lista

    # División de la lista utilizando slicing
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Recursividad
    izquierda_ordenada = merge_sort(izquierda, key)
    derecha_ordenada = merge_sort(derecha, key)

    # Retorna las listas ordenadas
    return merge(izquierda_ordenada, derecha_ordenada, key)

# Función para unificar los valores en una lista nueva
def merge(izquierda, derecha, key):
    lista_ordenada = []
    i = 0
    j = 0

    # Bucle comparativo entre ambas listas
    while i < len(izquierda) and j < len(derecha):
        if key(izquierda[i]) < key(derecha[j]):
            lista_ordenada.append(izquierda[i])
            i += 1
        else:
            lista_ordenada.append(derecha[j])
            j += 1

    # El while finaliza cuando una de las listas se ha recorrido completamente
    # La otra lista puede aun contener elementos, que serán agregados a continuación en la lista nueva
    lista_ordenada.extend(izquierda[i:])
    lista_ordenada.extend(derecha[j:])

    return lista_ordenada

# Funcion de ordenamiento que utiliza un pivote y divida la lista en partes
# Parametro key para definir atributo a ordenar
def quick_sort(lista, key=lambda x: x):
    # Condición para detener la recursión
    if len(lista) <= 1:
        return lista

    # Elección del Pivote
    # Se elige el del medio ya que se considera el mejor caso
    mitad = len(lista) // 2
    pivote = lista[mitad]

    menores = []
    iguales = []
    mayores = []

    for elemento in lista:
        if key(elemento) < key(pivote):
            menores.append(elemento)
        elif key(elemento) == key(pivote):
            iguales.append(elemento)
        else: # key(elemento) > key(pivote)
            mayores.append(elemento)

    # Recursividad y combinación
    return quick_sort(menores, key) + iguales + quick_sort(mayores, key)