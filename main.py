import time
import random
import pandas as pd
from busqueda import busqueda_lineal, busqueda_binaria
from ordenamiento import bubble_sort, merge_sort, quick_sort

# Cargar archivo CSV
df = pd.read_csv("Data/books.csv", on_bad_lines='skip')

# Convertir DataFrame a lista de diccionarios
libros = df.to_dict(orient="records")

#Función para elegir autor aleatorio
def elegir_autor_aleatorio(dataset):
  return random.choice(dataset)['authors']

# --- PRUEBAS DE BÚSQUEDA ---

print("\n--- PRUEBAS DE BÚSQUEDA ---")

# Elegir autor aleatorio
autor_buscado = elegir_autor_aleatorio(libros)
print(f"Autor aleatorio buscado: '{autor_buscado}'")

# Medir tiempo de búsqueda lineal
print('\n--- Búsqueda Lineal ---')
inicio = time.time()
resultado = busqueda_lineal(libros, autor_buscado)
fin = time.time()
tiempo_busqueda_lineal = fin - inicio


# Ordenar la lista alfabéticamente por autor (ignorando mayúsculas/minúsculas)
libros_ordenados= sorted(libros, key=lambda x: x['authors'].lower())

# Medir tiempo de búsqueda binaria
inicio_binaria = time.time()
resultado_binaria = busqueda_binaria(libros_ordenados, autor_buscado)
fin_binaria = time.time()
tiempo_busqueda_binaria=fin_binaria - inicio_binaria

#Resultado lineal:
print('Tiempo de ejecución con una busqueda lineal')
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

#Comparación entre búsqueda lineal y binaria:
print("\n")
print('COMPARACION:')
print(f"Tiempo de búsqueda lineal: {tiempo_busqueda_lineal:.6f} segundos")
print(f"Tiempo de búsqueda binaria: {tiempo_busqueda_binaria:.6f} segundos")


# --- PRUEBAS DE ORDENAMIENTOS ---
print("\n--- PRUEBAS DE ORDENAMIENTO ---")

# Usamos copias para no alterar el dataset original
libros_bubble = libros.copy()
libros_merge = libros.copy()
libros_quick = libros.copy()

# --- Bubble Sort ---
inicio = time.time()
bubble_sort(libros_bubble, key=lambda x: x['authors'].lower())
fin = time.time()
tiempo_bubble = fin - inicio
print(f"Bubble Sort: {tiempo_bubble:.6f} segundos")

# --- Merge Sort ---
inicio = time.time()
libros_merge = merge_sort(libros_merge, key=lambda x: x['authors'].lower())
fin = time.time()
tiempo_merge = fin - inicio
print(f"Merge Sort : {tiempo_merge:.6f} segundos")

# --- Quick Sort ---
inicio = time.time()
quick_sort(libros_quick, key=lambda x: x['authors'].lower())
fin = time.time()
tiempo_quick = fin - inicio
print(f"Quick Sort : {tiempo_quick:.6f} segundos")
