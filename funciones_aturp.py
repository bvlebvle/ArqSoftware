import csv

def obtenerIDPaciente(rut, archivo_pacientes='./DB/pacientes.csv'):
    with open(archivo_pacientes, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila[1] == rut:
                return fila[0]  # Retorna el ID del paciente
    return None  # Retorna None si no encuentra el RUT

def obtenerIDPaciente(rut, archivo_pacientes='./DB/pacientes.csv'):
    with open(archivo_pacientes, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila[1] == rut:
                return fila[0]  # Retorna la ID del paciente
    return None  # Retorna None si no encuentra el RUT

def generarNumero(rut):
    id_paciente = obtenerIDPaciente(rut)
    if id_paciente is None:
        return "Paciente no registrado"

    turnos = []
    with open('./DB/turnos.csv', 'r') as archivo_turnos:
        csv_reader = csv.DictReader(archivo_turnos, delimiter='|')
        for fila in csv_reader:
            if fila['id_paciente'] == id_paciente:
                turnos.append(int(fila['turno']))

    if turnos:
        turno_asignado = max(turnos)
        return f"Ya tienes un número, tu turno es {turno_asignado}"
    else:
        nuevo_turno = max(turnos, default=0) + 1
        with open('./DB/turnos.csv', 'a', newline='') as archivo_turnos:
            csv_writer = csv.writer(archivo_turnos, delimiter='|')
            csv_writer.writerow([len(turnos) + 1, id_paciente, nuevo_turno, 'esperando'])
        return f"Tu turno es {nuevo_turno}"


def avanzarNumero(archivo_turnos='./DB/turnos.csv'):
    menor_turno = None
    fila_menor_turno = None
    rows = []

    # Leer el archivo y almacenar sus filas
    with open(archivo_turnos, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='|')
        rows = list(reader)

    # Encontrar el menor turno
    for row in rows[1:]:
        if len(row) >= 3:  # Verificar si la fila tiene al menos 3 elementos
            turno_actual = int(row[2])
            if menor_turno is None or turno_actual < menor_turno:
                menor_turno = turno_actual
                fila_menor_turno = row

    # Eliminar la fila con el menor turno encontrado
    if fila_menor_turno:
        rows.remove(fila_menor_turno)

    # Escribir todas las filas en el archivo
    with open(archivo_turnos, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerows(rows)

    return f"turno: {menor_turno}" if menor_turno is not None else "No hay turnos disponibles"


menor_turno_encontrado = avanzarNumero()
print(f"Menor turno encontrado y eliminado: {menor_turno_encontrado}")
