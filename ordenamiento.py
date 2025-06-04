# Itera cada elemento y lo va comparando con su adyacente.
# Si es mayor, lo mueve un lugar en la lista y sigue comparando
def bubble_sort(lista):

    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Divide la lista en mitades hasta que cada lista tenga un solo elemento,
# se utiliza la recursividad y un condicional que verifica cuando exista un elemento en la lista y da por finalizada la recursión
def merge_sort(lista):
    # Condición para detener la recursión
    if len(lista) == 1:
        return lista

    # División de la lista utilizando slicing
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Recursividad
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    # Retorna las listas ordenadas
    return merge(izquierda_ordenada, derecha_ordenada)

# Función para unificar los valores en una lista nueva
def merge(izquierda, derecha):
    lista_ordenada = []
    i = 0
    j = 0

    # Bucle comparativo entre ambas listas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
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

def quick_sort(lista):
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
        if elemento < pivote:
            menores.append(elemento)
        elif elemento == pivote:
            iguales.append(elemento)
        else: # elemento > pivote
            mayores.append(elemento)

    # Recursividad y combinación
    return quick_sort(menores) + iguales + quick_sort(mayores)