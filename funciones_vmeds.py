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
    print("Agenda del día", dia_semana, dia, "/", mes)
    citas_del_dia = obtenerCitasDia(str(dia), str(mes))

    if nombre == "":
        if len(citas_del_dia) == 0:
            print("No hay citas agendadas")
        else:
            for cita in citas_del_dia:
                id_medico = cita[0]
                hora = cita[1]
                nombre_medico = obtenerNombreMedico(id_medico)
                print("Médico:", nombre_medico, "- Hora:", hora)
    else:
        if len(citas_del_dia) == 0:
            print("No hay citas agendadas")
        else:
            for cita in citas_del_dia:
                id_medico = cita[0]
                hora = cita[1]
                nombre_medico = obtenerNombreMedico(id_medico)
                if nombre == nombre_medico:
                    print("Médico:", nombre_medico, "- Hora:", hora)
    return True


def visualizarAgendaSemana(dia, mes, nombre):
    print("Agenda de la semana")
    print("-------------------------")
    for i in range(7):
        visualizarAgendaDiaria(dia, mes, nombre)
        print("")
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
    return True


def diaMedico(dia, mes, data):
    # data nombreM-ApellidoM
    nombre = data[0:data.find('-')].upper()
    apellido = data[data.find('-')+1:].upper()
    nombre_medico = nombre + " " + apellido

    visualizarAgendaDiaria(dia, mes, nombre_medico)
    return True


def semanaMedico(dia, mes, data):
    # data nombreM-ApellidoM
    nombre = data[0:data.find('-')].upper()
    apellido = data[data.find('-')+1:].upper()
    nombre_medico = nombre + " " + apellido
    visualizarAgendaSemana(dia, mes, nombre_medico)
    return True


# fecha = datetime.datetime.now()
# dia = fecha.day
# mes = fecha.month
# visualizarAgendaDiaria(dia, mes, "")
# diaMedico("roberto-sanchez")

# print("")
# visualizarAgendaSemana(dia, mes, "")
# semanaMedico("juan-perez")
