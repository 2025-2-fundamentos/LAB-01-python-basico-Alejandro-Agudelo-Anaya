"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    recuento = {}
    with open("./files/input/data.csv", "r") as file:

        for line in file:
            parts = line.strip().split("\t")
            letra = parts[4].split(",")
            claves_vistas = set()
            for item in letra:
                clave, _ = item.split(":")
                if clave not in claves_vistas:
                    if clave in recuento:
                        recuento[clave] += 1
                    else:
                        recuento[clave] = 1
                    claves_vistas.add(clave)
    return recuento