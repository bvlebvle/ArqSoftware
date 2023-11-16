
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
    print("2. Editar historial médico de un médico")
    print("3. Eliminar historial médico de un médico")
    print("4. Volver al menú principal")
    opcion = input("Ingrese el número de la opción que desea: ")
    return opcion


def menuBhora():
    print("Bloqueo de horas")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Bloquear horas")
    print("2. Desbloquear horas")
    #print("3. Agregar horas")  # Agregar dps quiza
    print("4. Volver al menú principal")
    opcion = input("Ingrese el número de la opción que desea: ")
    return opcion
