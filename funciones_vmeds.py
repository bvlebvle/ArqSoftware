# visualizar agenda del dia de todos los medicos
import csv
import datetime

from funciones_gcita import obtenerDiaSemana


def obtenerNombreMedico(id_medico):
    archivo_csv = './DB/medicos.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 0:
                if fila[0] == id_medico:
                    nombre = fila[2]
                    apellido = fila[3]
                    nombre_medico = nombre + " " + apellido

                    return nombre_medico
    return None


def obtenerCitasDia(dia, mes):
    archivo_csv = './DB/citas.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        citas_del_dia = []
        for fila in csv_reader:
            if len(fila) > 0:
                if fila[4] == dia and fila[5] == mes:
                    id_medico = fila[2]
                    hora = fila[6]
                    tupla = [id_medico, hora]
                    citas_del_dia.append(tupla)
    return citas_del_dia


def visualizarAgendaDiaria(dia, mes, nombre):
    dia_semana = obtenerDiaSemana(dia, mes)
    # print("Agenda del día", dia_semana, dia, "/", mes)
    citas_del_dia = obtenerCitasDia(str(dia), str(mes))
    result = []

    if nombre == "":
        result.append(len(citas_del_dia))
        for cita in citas_del_dia:
            id_medico = cita[0]
            hora = cita[1]
            nombre_medico = obtenerNombreMedico(id_medico)
            linea = nombre_medico + "-" + hora
            result.append(linea)
    else:
        cont = 0
        for cita in citas_del_dia:
            id_medico = cita[0]
            hora = cita[1]
            nombre_medico = obtenerNombreMedico(id_medico)
            if nombre == nombre_medico:
                cont = cont + 1
        result.append(cont)
        for cita in citas_del_dia:
            id_medico = cita[0]
            hora = cita[1]
            nombre_medico = obtenerNombreMedico(id_medico)
            if nombre == nombre_medico:
                linea = nombre_medico + "-" + hora
                result.append(linea)
    return result


def visualizarAgendaSemana(dia, mes, nombre):
    result = []
    for i in range(7):
        un_dia = visualizarAgendaDiaria(dia, mes, nombre)
        result.append(un_dia)
        dia = int(dia) + 1
        if mes == 2 and dia > 28:
            dia = 1
            mes = int(mes) + 1
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 30:
                dia = 1
                mes = int(mes) + 1
        else:
            if dia > 31:
                dia = 1
                mes = int(mes) + 1
    return result


def diaMedico(dia, mes, data):
    # data nombreM-ApellidoM
    nombre = data[0:data.find('-')].upper()
    apellido = data[data.find('-')+1:].upper()
    nombre_medico = nombre + " " + apellido
    result = visualizarAgendaDiaria(dia, mes, nombre_medico)
    return result


def semanaMedico(dia, mes, data):
    # data nombreM-ApellidoM
    nombre = data[0:data.find('-')].upper()
    apellido = data[data.find('-')+1:].upper()
    nombre_medico = nombre + " " + apellido
    result = visualizarAgendaSemana(dia, mes, nombre_medico)
    return result


fecha = datetime.datetime.now()
dia = fecha.day
mes = fecha.month
# visualizarAgendaDiaria(dia, mes, "")
print(diaMedico(dia, mes, "juan-perez"))
# print(semanaMedico(dia, mes, "juan-perez"))

# print("")
# visualizarAgendaSemana(dia, mes, "")
# semanaMedico("juan-perez")

# print(visualizarAgendaDiaria(dia, mes, ""))
# print(visualizarAgendaSemana(dia, mes, ""))
