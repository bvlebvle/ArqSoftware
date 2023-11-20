import datetime
from funciones_gcobr import *
from funciones_gmeds import *
from funciones_crhor import *
from funciones_gpacs import *


def obtenerDiaSemana(fecha_dia, mes):
    dia = datetime.datetime(2023, int(mes), int(fecha_dia)).weekday()
    if dia == 0:
        return "LUNES"
    elif dia == 1:
        return "MARTES"
    elif dia == 2:
        return "MIERCOLES"
    elif dia == 3:
        return "JUEVES"
    elif dia == 4:
        return "VIERNES"
    elif dia == 5:
        return "SABADO"
    elif dia == 6:
        return "DOMINGO"


def obtenerParametros(data):
    # nombreP-apellidoP-nombreM-ApellidoM-especialidad-dia-mes-hora
    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            pos_caracter.append(i)

    rutP = data[0:pos_caracter[0]]
    rutM = data[pos_caracter[0]+1:pos_caracter[1]]
    dia = data[pos_caracter[1]+1:pos_caracter[2]]
    mes = data[pos_caracter[2]+1:pos_caracter[3]]
    hora = data[pos_caracter[3]+1:]
    return rutP, rutM, dia, mes, hora


def obtenerParametrosEditar(data):

    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            pos_caracter.append(i)
    rutP = data[0:pos_caracter[0]]
    rutM = data[pos_caracter[0]+1:pos_caracter[1]]
    dia_antiguo = data[pos_caracter[1]+1:pos_caracter[2]]
    mes_antiguo = data[pos_caracter[2]+1:pos_caracter[3]]
    hora_antiguo = data[pos_caracter[3]+1:pos_caracter[4]]
    dia_nuevo = data[pos_caracter[4]+1:pos_caracter[5]]
    mes_nuevo = data[pos_caracter[5]+1:pos_caracter[6]]
    hora_nuevo = data[pos_caracter[6]+1:]

    return rutP, rutM, dia_antiguo, mes_antiguo, hora_antiguo, dia_nuevo, mes_nuevo, hora_nuevo


def obtenerParametrosEliminar(data):
    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            pos_caracter.append(i)

    rutP = data[0:pos_caracter[0]]
    rutM = data[pos_caracter[0]+1:pos_caracter[1]]
    dia = data[pos_caracter[1]+1:pos_caracter[2]]
    mes = data[pos_caracter[2]+1:pos_caracter[3]]
    hora = data[pos_caracter[3]+1:]
    return rutP, rutM, dia, mes, hora


def obtenerIdCita(id_paciente, id_medico, dia, mes, hora):
    archivo_csv = './DB/citas.csv'
    print ("obtener cita")
    print ("id paciente: ", id_paciente)
    print ("id medico: ", id_medico)
    print ("dia: ", dia)
    print ("mes: ", mes)
    print ("hora: ", hora)
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 2 and fila[1] == id_paciente and fila[2] == id_medico and fila[4] == dia and fila[5] == mes and fila[6] == hora:
                return fila[0]
        return 0


def crearCita(parametros):
    print("------------------------------")
    print("Creando cita...")
    archivo_csv = './DB/citas.csv'
    rutP, rutM, fecha_dia, mes, hora = obtenerParametros(
        parametros)

    # paciente
    id_paciente = obtenerIdPaciente(rutP)
    print ("rut_p: ", rutP)
    print ("rut_m: ", rutM)
    if id_paciente == 0:
        print("Paciente no existe")
        return False

    # medico
    id_medico = obtenerIdMedico(rutM)
    if id_medico == 0:
        print("Medico no existe")
        return False
    print("id medico: ", id_medico)
    print("id paciente: ", id_paciente)

    # horario
    dia_semana = obtenerDiaSemana(fecha_dia, mes)
    id_horario = buscarIdHorario(id_medico, dia_semana, hora)
    print("id horario: ", id_horario)
    if id_horario == 0:
        print("Horario no existe")
        return False

    # verificar si horario esta disponible
    id_cita = obtenerIdCita(id_paciente, id_medico, fecha_dia, mes, hora)
    if id_cita != 0:
        print("Cita ya existe")
        return False

    if disponibilidadHorario(id_horario):
        # crear cita
        ultimo_id = obtener_ultimo_id(archivo_csv)
        id_cita = ultimo_id + 1
        estado = "AGENDADA"

        # agregar cobro
        agregarCobro(rutM)
        monto = obtenerMonto(id_medico)
        print("Monto: ", monto)

        nueva_cita = [id_cita, id_medico, id_paciente, dia_semana,
                      fecha_dia, mes, hora, estado, monto]
        with open(archivo_csv, 'a', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerow(nueva_cita)
        cambioEstadoHorario(id_horario, False)
        print("id cita: ", id_cita)
        print("Se creo cita")

        return True
    else:
        print("Horario no disponible")
        return False


def eliminarCita(parametros):
    print("------------------------------")
    print("Eliminando cita...")
    archivo_csv = './DB/citas.csv'
    rutP, rutM, dia, mes, hora = obtenerParametrosEliminar(parametros)
    id_medico = obtenerIdMedico(rutM)
    id_paciente = obtenerIdPaciente(rutP)
    id_cita = obtenerIdCita(id_paciente, id_medico, dia, mes, hora)
    dia_semana = obtenerDiaSemana(dia, mes)
    id_horario = buscarIdHorario(id_medico, dia_semana, hora)

    print("Id cita: ", id_cita)

    if id_cita != 0:
        filas_a_mantener = []
        with open(archivo_csv, 'r') as archivo:
            csv_reader = csv.reader(archivo, delimiter='|')
            cita_encontrada = False
            for fila in csv_reader:
                if len(fila) > 2:
                    if fila[0] == id_cita:
                        cita_encontrada = True
                    else:
                        filas_a_mantener.append(fila)

        if cita_encontrada:
            with open(archivo_csv, 'w', newline='') as archivo:
                csv_writer = csv.writer(archivo, delimiter='|')
                csv_writer.writerows(filas_a_mantener)
            cambioEstadoHorario(id_horario, True)
            print("Se elimino cita")
            return True
        else:
            print("No se encontro cita")
            return False
    else:
        print("No se encontro cita")
        return False


def editarCita(parametros):
    print("--------------------------------------------")
    print("Editando cita...")
    archivo_csv = './DB/citas.csv'
    rutP, rutM, dia_antiguo, mes_antiguo, hora_antiguo, dia_nuevo, mes_nuevo, hora_nuevo = obtenerParametrosEditar(
        parametros)
    id_medico = 0
    # data antigua
    data_antigua = rutP + "-" + rutM + "-" + \
        dia_antiguo + "-" + mes_antiguo + "-" + hora_antiguo
    # data nueva
    data_nueva = rutP + "-" + rutM + "-" + \
        dia_nuevo + "-" + mes_nuevo + "-" + hora_nuevo

    id_cita = obtenerIdCita(rutP, rutM, dia_antiguo, mes_antiguo, hora_antiguo)

    # ver si el horario esta disponible
    id_medico = obtenerIdMedico(rutM)
    dia_semana_nuevo = obtenerDiaSemana(dia_nuevo, mes_nuevo)

    id_horario = buscarIdHorario(id_medico, dia_semana_nuevo, hora_nuevo)
    if id_horario == 0:
        print("Horario no disponible para cita nueva")
        return False

    id_paciente = obtenerIdPaciente(rutP)
    id_cita = obtenerIdCita(id_paciente, id_medico,
                            dia_antiguo, mes_antiguo, hora_antiguo)
    print ("id cita: ", id_cita)
    print ("id horario: ", id_horario)
    print ("id medico: ", id_medico)
    print ("id paciente: ", id_paciente)
    print ("dia semana nuevo: ", dia_semana_nuevo)
    print ("hora nueva: ", hora_nuevo)
    print ("dia nuevo: ", dia_nuevo)
    print ("mes nuevo: ", mes_nuevo)
    print ("hora antiguo: ", hora_antiguo)
    print ("dia antiguo: ", dia_antiguo)
    print ("mes antiguo: ", mes_antiguo)
    if id_cita == 0:
        print("Cita no existe")
        return False

    if disponibilidadHorario(id_horario):
        if crearCita(data_nueva):
            if eliminarCita(data_antigua):
                print("Se edito cita")
                return True
            else:
                print("No se encontro cita")
                return False
        else:
            print("No se pudo crear cita")
            return False
    else:
        print("Horario no disponible para cita nueva")
        return False


parametros = "987654321-123456789-20-11-09:00"
# eliminar = "1111-1000-23-10-11:00"
# print(obtenerParametros(parametros))
crearCita(parametros)
# eliminarCita(eliminar)
# parametros_editar = "1111-1000-23-10-11:00-23-10-10:30"
# print(obtenerParametrosEditar(parametros_editar))
# editarCita(parametros_editar)
# print(obtenerParametrosEliminar(eliminar))


# id , medico_id, paciente_id, dia, mes, hora, estado, monto
parametros = "123456-123456-14-11-15:30-14-11-16:00"
editarCita(parametros)