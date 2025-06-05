import pandas as pd
import random

def cargar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv, on_bad_lines='skip')
    return df.to_dict(orient="records")

def elegir_autor_aleatorio(dataset):
    return random.choice(dataset)['authors']

def ordenar_por_autor(lista):
    return sorted(lista, key=lambda x: x['authors'].lower())
