import csv
from datetime import datetime

def leerDatosMedicos(archivo_medicos='./DB/medicos.csv'):
    medicos = {}
    with open(archivo_medicos, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) >= 6:  # Verifica que la fila tenga al menos 6 elementos
                medicos[fila[1]] = {
                    'idMedico': fila[0],
                    'nombre': fila[2],
                    'apellido': fila[3],
                    'especialidad': fila[4],
                    'box': fila[5]
                }
            else:
                print(f"Advertencia: Fila incompleta encontrada en el archivo: {fila}")
    return medicos


def calcularHorasTrabajadasPorRut(rut, archivo_horarios='./DB/horarios.csv', archivo_medicos='./DB/medicos.csv'):
    medicos = leerDatosMedicos(archivo_medicos)
    if rut not in medicos:
        print(f"No se encontró el médico con RUT: {rut}")
        return 0

    idMedico = medicos[rut]['idMedico']
    horas_trabajadas = 0

    with open(archivo_horarios, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila[1] == idMedico and fila[5] == 'False':
                formato_hora = '%H:%M'
                inicio = datetime.strptime(fila[3], formato_hora)
                fin = datetime.strptime(fila[4], formato_hora)
                duracion = (fin - inicio).seconds / 3600  # Duración en horas
                horas_trabajadas += duracion

    return horas_trabajadas
