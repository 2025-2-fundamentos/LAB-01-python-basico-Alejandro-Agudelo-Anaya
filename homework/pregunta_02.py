"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """

    from collections import defaultdict

    def mapreduce(columna):
        def mapper(line):
            parts = line.strip().split("\t")
            return (parts[columna], 1)

        def shuffle_Group():
            groups = defaultdict(list)
            with open("./files/input/data.csv", "r") as f:
                for line in f:
                    k, v = mapper(line)
                    groups[k].append(v)
            return groups

        def reducer(key, values):
            return (key, sum(values))

        groups = shuffle_Group()
        result = [reducer(k, v) for k, v in groups.items()]
        return sorted(result)

    return mapreduce(0)
