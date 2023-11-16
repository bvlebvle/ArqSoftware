import csv

def obtenerIDMedico(rut, archivo_medicos='./DB/medicos.csv'):
    with open(archivo_medicos, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if not fila:  # Ignora las filas vacías
                continue
            if len(fila) < 2:
                continue
            if fila[1] == rut:
                return fila[0]  # Retorna el ID del médico
    return None  # Retorna None si no encuentra el RUT

def verHistorialMedico(rut, archivo_citas='./DB/citas.csv', archivo_medicos='./DB/medicos.csv'):
    id_medico = obtenerIDMedico(rut, archivo_medicos)
    if id_medico is None:
        print("Médico no encontrado.")
        return []

    historial = []
    with open(archivo_citas, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if not fila:  # Ignora las filas vacías
                continue
            if len(fila) < 3:
                continue
            if fila[2] == id_medico:
                historial.append({
                    'id_cita': fila[0],
                    'id_paciente': fila[1],
                    'id_medico': fila[2],
                    'dia_semana': fila[3],
                    'dia': fila[4],
                    'mes': fila[5],
                    'hora': fila[6],
                    'estado': fila[7],
                    'monto': fila[8]
                })
    return historial

def eliminarHistorialMedico(rut, archivo_citas='./DB/citas.csv', archivo_medicos='./DB/medicos.csv'):
    id_medico = obtenerIDMedico(rut, archivo_medicos)
    if id_medico is None:
        print("Médico no encontrado.")
        return False

    filas_actualizadas = []
    eliminado = False
    with open(archivo_citas, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if not fila:  # Ignora las filas vacías
                continue
            if len(fila) < 3:
                continue
            if fila[2] != id_medico:
                filas_actualizadas.append(fila)
            else:
                eliminado = True

    with open(archivo_citas, 'w', newline='') as archivo:
        csv_writer = csv.writer(archivo, delimiter='|')
        csv_writer.writerows(filas_actualizadas)
    
    return eliminado

def editarHistorialMedico(parametros, archivo_citas='./DB/citas.csv', archivo_medicos='./DB/medicos.csv'):
    print("Estoy editando")
    divido = parametros.split("-")
    rut_medico = divido[0]
    fecha_antigua_dia = divido[1]
    fecha_antigua_mes = divido[2]
    fecha_antigua_ano = divido[3]
    fecha_nueva_dia = divido[4]
    fecha_nueva_mes = divido[5]
    fecha_nueva_ano = divido[6]

    id_medico = obtenerIDMedico(rut_medico, archivo_medicos)
    if id_medico is None:
        print("Médico no encontrado.")
        return False

    filas_actualizadas = []
    editado = False
    with open(archivo_citas, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if not fila:  # Ignora las filas vacías
                continue
            if len(fila) < 9:
                continue
            if fila[2] == id_medico and fila[4] == fecha_antigua_dia and fila[5] == fecha_antigua_mes and fila[6] == fecha_antigua_ano:
                print("Encontré la fila")
                fila[3] = fecha_nueva_dia
                fila[4] = fecha_nueva_mes
                fila[5] = fecha_nueva_ano
                editado = True
            filas_actualizadas.append(fila)

    with open(archivo_citas, 'w', newline='') as archivo:
        csv_writer = csv.writer(archivo, delimiter='|')
        csv_writer.writerows(filas_actualizadas)
    
    return editado
