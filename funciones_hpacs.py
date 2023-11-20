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



def eliminarHistorialPaciente(parametros, archivo_citas='./DB/citas.csv', archivo_pacientes='./DB/pacientes.csv'):
    parametros = parametros.split("-")
    rut = parametros[0]
    dia = parametros[1]
    mes = parametros[2]
    hora = parametros[3]
    id_paciente = obtenerIDPaciente(rut, archivo_pacientes)
    if id_paciente is None:
        print("Paciente no encontrado.")
        return False

    filas_actualizadas = []
    eliminado = False
    with open(archivo_citas, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            # Comprueba si la fila corresponde a la cita que se quiere eliminar
            if fila[1] == id_paciente and fila[4] == dia and fila[5] == mes and fila[6] == hora:
                eliminado = True
                continue  # No añadir esta fila a filas_actualizadas para eliminarla
            filas_actualizadas.append(fila)

    if eliminado:
        with open(archivo_citas, 'w', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerows(filas_actualizadas)

    return eliminado



def editarHistorialPaciente(parametros, archivo_citas='./DB/citas.csv', archivo_pacientes='./DB/pacientes.csv'):
    parametros = parametros.split("-")
    rut = parametros[0]
    dia_antiguo = parametros[1]
    mes_antiguo =   parametros[2]
    hora_antigua =  parametros[3]
    dia_nuevo =    parametros[4]
    mes_nuevo =   parametros[5]
    hora_nueva = parametros[6]
    id_paciente = obtenerIDPaciente(rut, archivo_pacientes)
    if id_paciente is None:
        print("Paciente no encontrado.")
        return False

    filas_actualizadas = []
    editado = False
    with open(archivo_citas, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            # Verifica que la fila tenga todos los elementos esperados
            if len(fila) < 9:  # Asegúrate de que este número sea correcto según tu estructura de datos
                continue  # Si no los tiene, ignora esta fila y continúa con la siguiente
            if fila[1] == id_paciente and fila[4] == dia_antiguo and fila[5] == mes_antiguo and fila[6] == hora_antigua:
                print("Encontré la fila a editar")
                fila[4] = dia_nuevo
                fila[5] = mes_nuevo
                fila[6] = hora_nueva
                editado = True
            filas_actualizadas.append(fila)

    if editado:
        with open(archivo_citas, 'w', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerows(filas_actualizadas)

    return editado


