
import datetime
import re
import json

def crearData(data):
    cant = len(data)
    payload = ""
    for i in range(cant):
        if i == cant - 1:
            payload += data[i]
        else:
            payload += data[i] + "-"
    return payload


def crearMsg(data, servicio):
    payload = crearData(data)
    resp = '{:05d}'.format(len(servicio) + len(payload)) + servicio + payload

    return resp


def menuPrincipal():
    print("Puede escoger entre los siguientes servicios:")
    print("1. Gestión de médicos")
    print("2. Gestión de horarios de médicos")
    print("3. Gestión de citas")
    print("4. Ranking de médicos")
    print("5. Visualizar agenda de médicos")
    print("6. Generar monto a pagar por consulta")
    print("7. Historial de pacientes")
    print("8. Gestión de boxs")
    print("9. Segimiento de médicos")
    print("10. Historial para médicos")
    print("11. Bloqueo de horarios")
    print("12. Siguiente turno")
    print("0. Salir de sistema")
    opcion = input("Ingrese el número de la opción que desea: ")
    return opcion


def menuPaciente():
    print("1. Avisar llegada")
    print("0. Salir de sistema")
    opcion = input("Ingrese el número de la opción que desea: ")
    return opcion


def menuGmeds():
    print("Gestión de médicos")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Crear médico")
    print("2. Editar médico")
    print("3. Eliminar médico")
    print("4. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion


def menuCrhor():
    print("Gestión de horarios de médicos")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Crear horario")
    print("2. Editar horario")
    print("3. Eliminar horario")
    print("4. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion


def menuGcita():
    print("Gestión de citas")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Crear cita")
    print("2. Editar cita")
    print("3. Eliminar cita")
    print("4. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion


def menuRmeds():
    print("Ranking de médicos")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Ranking general de médicos")
    print("2. Ranking de médicos por especialidades")
    print("3. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion


def menuVmeds():
    print("Visualización de agenda de médicos")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Agenda diaria de todos los medicos")
    print("2. Agenda semanal de todos los medicos")
    print("3. Agenda diaria de un medico")
    print("4. Agenda semanal de un medico")
    print("5. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion


def menuGcobr():
    print("Generar monto a pagar por consulta")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Monto a pagar por consulta")
    print("2. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion


data = ["cr", "nombre", "apellido", "especialidad"]
servicio = "crmed"
crearMsg(data, servicio)


def menuHpacs():
    print("Historial de pacientes")
    print("Puede escoger entre los siguientes servicios:")
    print("1. ver historial de paciente")
    print("2. editar historial de paciente")
    print("3. eliminar historial de paciente")
    print("4. Volver al menú principal")
    opcion = input("Ingrese el número de la opción que desea: ")
    return opcion


def menuGboxs():
    print("Gestión de boxs")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Crear box")
    print("2. Asignar box")
    print("3. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion


def menuSmeds():
    print("Puede escoger entre las siguientes opciones:")
    print("1. Horas trabajadas por medico")
    print("2. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion


def menuHmeds():
    print("Historial para médicos")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Ver historial médico de un médico")
    print("2. Volver al menú principal")
    opcion = input("Ingrese el número de la opción que desea: ")
    return opcion


def menuBhora():
    print("Bloqueo de horas")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Bloquear horas")
    print("2. Desbloquear horas")
    # print("3. Agregar horas")  # Agregar dps quiza
    print("3. Volver al menú principal")
    opcion = input("Ingrese el número de la opción que desea: ")
    return opcion

def printDataHmeds(cadena):
    print("")
    indice_inicio = cadena.find("[")
    indice_fin = cadena.rfind("]")

    # Extraer el contenido dentro de los corchetes
    contenido_dentro_corchetes = cadena[indice_inicio + 1:indice_fin]
    neto = contenido_dentro_corchetes.replace("'", "")
    neto = neto.split("}, {")  # Separar cada conjunto de datos

    for elemento in neto:
        datos = elemento.split(", ")
        print("Datos del historial médico:")
        for dato in datos:
            clave, valor = dato.split(": ")
            print(f" - {clave}: {valor}")
        print("------")

def printDataRmeds2(cadena):
   # OK['TRAUMATOLOGIA', '3-JUAN-PEREZ', '2-JUAN3-PEREZ', '1-JUAN2-PEREZ', 'GENERAL', '1-VALE-DIAZ', 'GINECOLOGIA', '1-MARTIN-SAAVEDRA']
  # Busca el índice del primer corchete "[" y del último corchete "]"
    print("")
    indice_inicio = cadena.find("[")
    indice_fin = cadena.rfind("]")

    # Extrae el contenido dentro de los corchetes
    contenido_dentro_corchetes = cadena[indice_inicio + 1:indice_fin]
    neto = contenido_dentro_corchetes.replace("'", "")
    neto = neto.split(", ")

    for i in range(len(neto)):
        if neto[i][1] == "-":
            cantidad, nombre, apellido = neto[i].split("-")
            print(f"Dr: {nombre} {apellido}, Cantidad de citas: {cantidad}")
        else:
            print("")
            print(f"Especialidad: {neto[i]}")


def printDataVmeds(cadena):
    print("")
    indice_inicio = cadena.find("[")
    indice_fin = cadena.rfind("]")

    contenido_dentro_corchetes = cadena[indice_inicio + 1:indice_fin]
    neto = contenido_dentro_corchetes.replace("'", "")
    neto = neto.split(", ")
    inicial = neto[0]
    # fecha
    fecha = datetime.datetime.now()
    dia = fecha.day
    mes = fecha.month
    print("Día", dia, "/", mes)
    print("")
    if inicial == "0":
        print("No hay citas agendadas")
    else:
        for i in range(1, len(neto)):
            separado = neto[i].split("-")
            print(f"Dr. {separado[0]}, hora: {separado[1]}")


def printDataVmeds2(cadena):
    indice_inicio = cadena.find("[")
    indice_fin = cadena.rfind("]")
    contenido_dentro_corchetes = cadena[indice_inicio + 1:indice_fin]
    neto = contenido_dentro_corchetes.split("], [")
    fecha = datetime.datetime.now()
    dia = fecha.day
    mes = fecha.month

    for i in range(len(neto)):
        print("")
        print("Día", dia, "/", mes)
        if neto[i][0] == "[":
            neto[i] = neto[i][1:]
        if neto[i][-1] == "]":
            neto[i] = neto[i][:-1]

        if neto[i] == "0":
            print("No hay citas agendadas")
        else:
            separado = neto[i].split(",")
            citas = int(separado[0])
            for j in range(citas):
                separado[j+1] = separado[j+1].replace("'", "")
                nh = separado[j+1].split("-")
                print(f"Dr. {nh[0]}, hora: {nh[1]}")
            # print(f"Dr. {separado[1]}, hora: {separado[1]}")
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


# [2, 'VALE DIAZ-13:30', 'MARTIN SAAVEDRA-13:30']
# printDataVmeds("[2, 'VALE DIAZ-13:30', 'MARTIN SAAVEDRA-13:30']")
# [[2, 'VALE DIAZ-13:30', 'MARTIN SAAVEDRA-13:30'], [0], [0], [0], [0], [0], [0]]
data = "OK[[2, 'VALE DIAZ-13:30', 'MARTIN SAAVEDRA-13:30'], [0], [0], [0], [0], [0], [0]] "
printDataVmeds2(data)
    
def printlindahpcss(data):
    print("Historial de paciente:")
    try:
        # Eliminar el "OK" del principio
        if data.startswith('OK'):
            data = data[2:]
        # Reemplazar comillas simples por comillas dobles para obtener un JSON válido
        data = data.replace("'", '"')
        # Cargar la cadena como JSON
        citas = json.loads(data)
        for cita in citas:
            print(f"Día de la semana: {cita['dia_semana']}, Día: {cita['dia']}, Mes: {cita['mes']}, "
                  f"Hora: {cita['hora']}, Estado: {cita['estado']}, Monto: {cita['monto']}")
        print("")

    except json.JSONDecodeError as e:
        print("Error al decodificar la respuesta JSON:", e)
    except Exception as e:
        print("Ocurrió un error:", e)
    
