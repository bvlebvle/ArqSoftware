# ranking de doctores

import csv


def obtenerCitas():
    archivo_csv = './DB/citas.csv'
    citas = []
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 0:
                citas.append(fila[2])

    # hacer un mapa de id medico con cantidad de citas
    map_veces = {}
    for id_medico in citas:
        if id_medico != "id_medico":
            if id_medico in map_veces:
                map_veces[id_medico] += 1
            else:
                map_veces[id_medico] = 1

    # ordenar el mapa por cantidad de citas
    map_veces = sorted(map_veces.items(), key=lambda x: x[1], reverse=True)
    return map_veces


def triadaMedico():
    map_veces = obtenerCitas()
    triada = []
    for medico in map_veces:
        id_medico = medico[0]
        veces = medico[1]
        especialidad = obtenerEspecialidadMedico(id_medico)
        elemento = [id_medico, veces, especialidad]
        triada.append(elemento)

    return triada


def obtenerNombreMedico(id_medico):
    archivo_csv = './DB/medicos.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 0 and fila[0] == id_medico:
                return fila[2], fila[3]
    return "No encontrado", "No encontrado"


def obtenerEspecialidadMedico(id_medico):
    archivo_csv = './DB/medicos.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 0 and fila[0] == id_medico:
                return fila[4]
        return "No encontrado"


def rankingDoctoresTodos():
    print("Ranking de doctores")
    cont = 1
    map_medicos = obtenerCitas()
    for id_medico, veces in map_medicos:
        if cont == 4:
            break
        nombre, apellido = obtenerNombreMedico(id_medico)
        print(cont, "- Cantidad de citas:", veces, "- Dr.", nombre, apellido,)
        cont += 1
    return True


def rankingDoctoresEspecialidad():
    print("Ranking de doctores por especialidad")
    triada = triadaMedico()

    # separar por especialidad
    especialidades = []
    for medico in triada:
        especialidad = medico[2]
        if especialidad not in especialidades:
            especialidades.append(especialidad)

    for especialidad in especialidades:
        print("Especialidad:", especialidad)
        cont = 1
        for medico in triada:
            if medico[2] == especialidad:
                id_medico = medico[0]
                nombre, apellido = obtenerNombreMedico(id_medico)
                print(cont, "- Cantidad de citas:",
                      medico[1], "- Dr.", nombre, apellido)
        print("")

    return True


# rankingDoctoresTodos()
# print(triadaMedico())
# print(obtenerEspecialidadMedico("1"))
# rankingDoctoresEspecialidad()
