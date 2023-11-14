import csv


def obtenerIdPaciente(rut):
    archivo_csv = './DB/pacientes.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 2 and fila[1] == rut:
                return fila[0]
        return 0


# print(obtenerIdPaciente("1111"))
