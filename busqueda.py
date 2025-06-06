# Función de búsqueda lineal:
# Recorre la lista comparando el autor objetivo con el autor de cada elemento del dataset.
# La comparación ignora mayúsculas y minúsculas (convierte ambos nombres a minúsculas).
def busqueda_lineal(lista, autor_objetivo):
  for i in range(len(lista)):
    if lista[i]['authors'].lower() == autor_objetivo.lower():
      return i
  return -1

# Función de búsqueda binaria:
# Requiere una lista ordenada alfabéticamente por autor (en minúsculas para 
# comparación insensible a mayúsculas).
# Utiliza un bucle while para dividir la lista en mitades hasta encontrar 
# el autor buscado o agotar las posibilidades.
def busqueda_binaria(lista, autor_objetivo):
  izquierda, derecha= 0, len(lista) -1
  objetivo = autor_objetivo.lower()

  while izquierda <= derecha:
    mitad = (izquierda + derecha) // 2 
    autor_mitad= lista[mitad]['authors'].lower()

    if autor_mitad == objetivo:
      return mitad #retorna el valor del medio (mejor caso)
    elif autor_mitad < objetivo:
      izquierda = mitad +1 # El autor está en la mitad derecha
    else:
      derecha= mitad -1 # El autor está en la mitad izquierda
  return -1       # Autor no encontrado




