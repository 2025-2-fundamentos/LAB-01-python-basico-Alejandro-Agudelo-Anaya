"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
 
def pregunta_12():
    letras = {}

    with open("./files/input/data.csv") as file:
        for fila in file:
            columnas = fila.strip().split("\t")  # separo columnas
            letra = columnas[0]                  # primera columna

            for elemento in columnas[4].split(","):  # quinta columna
                numero = int(elemento.split(":")[1])
                letras[letra] = letras.get(letra, 0) + numero

    return dict(sorted(letras.items()))
