"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():


    from collections import defaultdict

    def mapreduce(columna):
        def mapper(line):
            parts = line.strip().split("\t")
            fecha = parts[columna]
            mes = fecha[5:7]
            return (mes, 1)

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

    return mapreduce(2)

