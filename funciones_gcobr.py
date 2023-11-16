
import csv
from funciones_gmeds import obtenerIdMedico
from funciones_rmeds import obtenerEspecialidadMedico


def agregarCobro(parametros):
    print("Agregar cobro")
    rutM = parametros
    id_medico = obtenerIdMedico(rutM)
    especialidad = obtenerEspecialidadMedico(id_medico)
    monto = ""

    if especialidad == "GENERAL":
        monto = "5.590"
        print("Cobro por consulta $5.590 por ser médico general")
    else:
        monto = "12.590"
        print("Cobro por consulta $12.590 por ser especialista")

    archivo_csv = './DB/cobros.csv'
    with open(archivo_csv, 'a') as archivo:
        csv_writer = csv.writer(archivo, delimiter='|')
        csv_writer.writerow([id_medico, monto])

    return True


def obtenerMonto(id_medico):
    archivo_csv = './DB/cobros.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 0 and fila[0] == id_medico:
                return fila[1]

    return 0
