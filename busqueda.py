import time
import random
import pandas as pd

# Cargar archivo CSV
df = pd.read_csv("Data/books.csv", on_bad_lines='skip')

# Convertir DataFrame a lista de diccionarios
libros = df.to_dict(orient="records")

#Función para elegir autor aleatorio
def elegir_autor_aleatorio(dataset):
  return random.choice(dataset)['authors']

# Función de búsqueda lineal:
# Recorre la lista comparando el autor objetivo con el autor de cada elemento del dataset.
# La comparación ignora mayúsculas y minúsculas (convierte ambos nombres a minúsculas).
def busqueda_lineal(lista, autor_objetivo):
  for i in range(len(lista)):
    if lista[i]['authors'].lower() == autor_objetivo.lower():
      return i
  return -1

#Elegir autor aleatorio
autor_buscado = elegir_autor_aleatorio(libros)

#Medir tiempo de busqueda lineal:
inicio=time.time()
resultado=busqueda_lineal(libros, autor_buscado)
fin=time.time()
tiempo_busqueda_lineal = fin - inicio



#Búsqueda binaria:

# Ordenar la lista alfabéticamente por autor (ignorando mayúsculas/minúsculas)
libros_ordenados= sorted(libros, key=lambda x: x['authors'].lower())

# Función de búsqueda binaria:
# Requiere una lista ordenada alfabéticamente por autor (en minúsculas para comparación insensible a mayúsculas).
# Utiliza un bucle while para dividir la lista en mitades hasta encontrar el autor buscado o agotar las posibilidades.
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

# Medir tiempo de búsqueda binaria
inicio_binaria = time.time()
resultado_binaria = busqueda_binaria(libros_ordenados, autor_buscado)
fin_binaria = time.time()
tiempo_busqueda_binaria=fin_binaria - inicio_binaria



#Resultado lineal:
print('Tiempo de ejecucioón con una busqueda lineal')
if resultado != -1:
  print(f"Autor: {libros[resultado]['authors']}. Posición: {resultado}")
else:
  print('Autor no encontrado')
print(f"Tiempo de búsqueda lineal: {tiempo_busqueda_lineal:.6f} segundos")

print("\n")  

#Resultado binario:
print('Tiempo de ejecución con una busqueda binaria')
if resultado_binaria != -1:
  print(f"Autor: {libros_ordenados[resultado_binaria]['authors']}. Posición: {resultado_binaria}")
else:
  print('Autor no encontrado.')
print(f"Tiempo de búsqueda binaria: {tiempo_busqueda_binaria:.6f} segundos")


#Comparación entre búsqeuda lineal y binaria:
print("\n")    
print('COMPARACION:')
print(f"Tiempo de búsqueda lineal: {tiempo_busqueda_lineal:.6f} segundos")
print(f"Tiempo de búsqueda binaria: {tiempo_busqueda_binaria:.6f} segundos")
