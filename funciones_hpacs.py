import csv

import csv


def obtenerIDPaciente(rut, archivo_pacientes='./DB/pacientes.csv'):
    with open(archivo_pacientes, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila[1] == rut:
                return fila[0]  # Retorna el ID del paciente
    return None  # Retorna None si no encuentra el RUT


def verHistorialPaciente(rut, archivo_citas='./DB/citas.csv', archivo_pacientes='./DB/pacientes.csv'):
    id_paciente = obtenerIDPaciente(rut, archivo_pacientes)
    if id_paciente is None:
        print("Paciente no encontrado.")
        return []

    historial = []
    with open(archivo_citas, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) >= 9 and fila[1] == id_paciente:
                historial.append({
                    'dia_semana': fila[3],
                    'dia': fila[4],
                    'mes': fila[5],
                    'hora': fila[6],
                    'estado': fila[7],
                    'monto': fila[8]
                })
    return historial



def eliminarHistorialPaciente(rut, archivo_citas='./DB/citas.csv', archivo_pacientes='./DB/pacientes.csv'):
    id_paciente = obtenerIDPaciente(rut, archivo_pacientes)
    if id_paciente is None:
        print("Paciente no encontrado.")
        return False

    filas_actualizadas = []
    eliminado = False
    with open(archivo_citas, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila[1] != id_paciente:
                filas_actualizadas.append(fila)
            else:
                eliminado = True

    with open(archivo_citas, 'w', newline='') as archivo:
        csv_writer = csv.writer(archivo, delimiter='|')
        csv_writer.writerows(filas_actualizadas)

    return eliminado


def editarHistorialPaciente(parametros, archivo_citas='./DB/citas.csv', archivo_pacientes='./DB/pacientes.csv'):
    print("Estoy editando")
    divido = parametros.split("-")
    rut = divido[0]
    fecha_antigua_dia = divido[1]
    fecha_antigua_mes = divido[2]
    fecha_antigua_ano = divido[3]
    fecha_nueva_dia = divido[4]
    fecha_nueva_mes = divido[5]
    fecha_nueva_ano = divido[6]

    id_paciente = obtenerIDPaciente(rut, archivo_pacientes)
    if id_paciente is None:
        print("Paciente no encontrado.")
        return False

    filas_actualizadas = []
    editado = False
    with open(archivo_citas, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila[1] == id_paciente and fila[4] == fecha_antigua_dia and fila[5] == fecha_antigua_mes and fila[6] == fecha_antigua_ano:
                print("Encontré la fila")
                fila[4] = fecha_nueva_dia
                fila[5] = fecha_nueva_mes
                fila[6] = fecha_nueva_ano
                editado = True
            filas_actualizadas.append(fila)

    with open(archivo_citas, 'w', newline='') as archivo:
        csv_writer = csv.writer(archivo, delimiter='|')
        csv_writer.writerows(filas_actualizadas)

    return editado
