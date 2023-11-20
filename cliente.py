import subprocess
import socket
from funciones_gmeds import *
from funciones_cliente import *
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)


def ejecutar_script(archivo):
    script_path = "./" + archivo + ".py"
    try:
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script: {e}")


def enviarMsg(message):
    try:
        # enviar mensaje
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # recibir mensaje
        response_len_str = sock.recv(5).decode()
        response_len = int(response_len_str)
        response_service = sock.recv(5).decode()

        response_data = sock.recv(response_len - 5).decode()

        print("")
        print(f"Received: {response_data} ")
        print("")
    finally:
        # print ('closing socket')
        # sock.close ()
        return response_data


print("Sistema de gestión de Centro Médico JRG")


data = []
while True:
    # menu principal esta en una funcion de clientes
    print("")
    opcion = menuPrincipal()
    print("")
    # hay un while true por cada opcion del menu principal
    if opcion == "1":
        while True:
            # menu de gestion de medicos esta en una funcion de clientes
            accion = menuGmeds()
            servicio = "gmeds"
            # ejecutar_script(servicio)
            if accion == "1":
                data = []
                print("Creación de médico")
                rut = input("Ingrese rut de médico: ")
                nombre = input("Ingrese nombre de médico: ")
                apellido = input("Ingrese apellido de médico: ")
                especialidad = input("Ingrese especialidad de médico: ")
                data.append("cr")
                data.append(rut)
                data.append(nombre)
                data.append(apellido)
                data.append(especialidad)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "2":
                data = []
                print("Edición de médico")
                rut = input("Ingrese rut de médico: ")
                new_nombre = input("Ingrese nuevo nombre de médico: ")
                new_apellido = input("Ingrese nuevo apellido de médico: ")
                new_especialidad = input(
                    "Ingrese nuevo especialidad de médico: ")
                data.append("ed")
                data.append(rut)
                data.append(new_nombre)
                data.append(new_apellido)
                data.append(new_especialidad)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "3":
                data = []
                print("Eliminación de médico")
                rut = input("Ingrese rut de médico: ")
                data.append("el")
                data.append(rut)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "4":
                break
    if opcion == "2":
        while True:
            servicio = "crhor"
            accion = menuCrhor()
            if accion == "1":
                data = []
                print("Creación de horario")
                rut = input("Ingrese rut de médico: ")
                dia = input("Ingrese día de horario: ")
                hora_inicio = input("Ingrese hora de inicio de horario: ")
                hora_fin = input("Ingrese hora de fin de horario: ")
                data.append("cr")
                data.append(rut)
                data.append(dia)
                data.append(hora_inicio)
                data.append(hora_fin)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "2":
                data = []
                print("Edición de horario")
                rut = input("Ingrese rut de médico: ")
                dia_antiguo = input("Ingrese día actual: ")
                hora_inicio_antigua = input("Ingrese hora inicio actual: ")
                hora_fin_antigua = input("Ingrese hora termino actual: ")
                dia_nuevo = input("Ingrese día nuevo: ")
                hora_inicio_nueva = input("Ingrese hora inicio nueva: ")
                hora_fin_nueva = input("Ingrese hora termino nueva: ")
                data.append("ed")
                data.append(rut)
                data.append(dia_antiguo)
                data.append(hora_inicio_antigua)
                data.append(hora_fin_antigua)
                data.append(dia_nuevo)
                data.append(hora_inicio_nueva)
                data.append(hora_fin_nueva)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "3":
                data = []
                print("Eliminación de horario")
                rut = input("Ingrese rut de médico: ")
                dia = input("Ingrese día de horario: ")
                hora_inicio = input("Ingrese hora de inicio: ")
                hora_fin = input("Ingrese hora de fin: ")
                data.append("el")
                data.append(rut)
                data.append(dia)
                data.append(hora_inicio)
                data.append(hora_fin)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "4":
                break
    if opcion == "3":
        while True:
            accion = menuGcita()
            servicio = "gcita"
            if accion == "1":
                data = []
                print("Creación de cita")
                rutP = input("Ingrese rut de paciente: ")
                rutM = input("Ingrese rut de médico: ")
                dia = input("Ingrese día de cita: ")
                mes = input("Ingrese mes de cita: ")
                hora = input("Ingrese hora de cita: ")
                data.append("cr")
                data.append(rutP)
                data.append(rutM)
                data.append(dia)
                data.append(mes)
                data.append(hora)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())

            if accion == "2":
                data = []
                print("Edición de cita")
                rutP = input("Ingrese rut de paciente: ")
                rutM = input("Ingrese rut de médico: ")
                dia_antiguo = input("Ingrese día actual: ")
                mes_antiguo = input("Ingrese mes actual: ")
                hora_antigua = input("Ingrese hora actual: ")
                dia_nuevo = input("Ingrese día nuevo: ")
                mes_nuevo = input("Ingrese mes nuevo: ")
                hora_nueva = input("Ingrese hora nueva: ")
                data.append("ed")
                data.append(rutP)
                data.append(rutM)
                data.append(dia_antiguo)
                data.append(mes_antiguo)
                data.append(hora_antigua)
                data.append(dia_nuevo)
                data.append(mes_nuevo)
                data.append(hora_nueva)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())

            if accion == "3":
                data = []
                print("Eliminación de cita")
                rutP = input("Ingrese rut de paciente: ")
                rutM = input("Ingrese rut de médico: ")
                dia = input("Ingrese día de cita: ")
                mes = input("Ingrese mes de cita: ")
                hora = input("Ingrese hora de cita: ")
                data.append("el")
                data.append(rutP)
                data.append(rutM)
                data.append(dia)
                data.append(mes)
                data.append(hora)
                msg = crearMsg(data, servicio)

                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "4":
                break
    if opcion == "4":
        while True:
            print("")
            accion = menuRmeds()
            servicio = "rmeds"
            if accion == "1":
                data = []

                data.append("rg")
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                response = enviarMsg(msg.encode())
                print("")
                print("Ranking general de médicos")
                printDataRmeds2(response)
                print("")
            if accion == "2":
                data = []

                data.append("re")
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                response = enviarMsg(msg.encode())
                print("")
                print("Ranking de médicos por especialidad")
                printDataRmeds2(response)
                print("")

            if accion == "3":
                break
    if opcion == "5":
        while True:
            accion = menuVmeds()
            servicio = "vmeds"
            if accion == "1":
                data = []

                data.append("vd")
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                result = enviarMsg(msg.encode())
                print("")
                print("Agenda diaria de todos los médicos")
                printDataVmeds(result)
                print("")

            if accion == "2":
                data = []
                print("Agenda semanal de todos los médicos")
                data.append("vs")
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                result = enviarMsg(msg.encode())
                print("")
                print("Agenda semanal de todos los médicos")
                printDataVmeds2(result)
                print("")
            if accion == "3":
                data = []
                print("Agenda diaria de un médico")
                nombre = input("Ingrese nombre de médico: ")
                apellido = input("Ingrese apellido de médico: ")
                data.append("dm")
                data.append(nombre)
                data.append(apellido)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                result = enviarMsg(msg.encode())
                print("")
                print("Agenda diaria de", nombre.upper(), apellido.upper())
                printDataVmeds(result)
                print("")
                enviarMsg(msg.encode())
            if accion == "4":
                data = []
                print("Agenda semanal de un médico")
                nombre = input("Ingrese nombre de médico: ")
                apellido = input("Ingrese apellido de médico: ")
                data.append("sm")
                data.append(nombre)
                data.append(apellido)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                result = enviarMsg(msg.encode())
                print("")
                print("Agenda semanal de", nombre.upper(), apellido.upper())
                printDataVmeds2(result)
                print("")
                enviarMsg(msg.encode())
            if accion == "5":
                break
    if opcion == "6":
        while True:
            accion = menuGcobr()
            servicio = "gcobr"
            if accion == "1":
                data = []
                print("Monto a pagar por consulta")
                rutM = input("Ingrese rut de médico: ")
                data.append("gc")
                data.append(rutM)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                result = enviarMsg(msg.encode())
                result = result[2:]
                print("")
                print("Valor a pagar por consulta: $", result)
                print("")
            if accion == "2":
                break

    if opcion == "7":
        while True:
            accion = menuHpacs()
            servicio = "hpcss"
            if accion == "1":
                data = []
                print("Ver historial de paciente")
                rut = input("Ingrese rut de paciente: ")
                data.append("vr")
                data.append(rut)
                print(data)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "2":
                data = []
                print("Editar historial de paciente")
                rut = input("Ingrese rut de paciente: ")
                fecha_antigua_dia = input("Ingrese dia actual de la cita: ")
                fecha_antigua_mes = input("Ingrese mes actual de la cita: ")
                fecha_antigua_hora = input("Ingrese hora actual de la cita: ")
                fecha_nueva_dia = input("Ingrese dia nuevo de la cita: ")
                fecha_nueva_mes = input("Ingrese mes nuevo de la cita: ")
                fecha_nueva_hora = input("Ingrese hora nuevo de la cita: ")
                data.append("ed")
                data.append(rut)
                data.append(fecha_antigua_dia)
                data.append(fecha_antigua_mes)
                data.append(fecha_antigua_hora)
                data.append(fecha_nueva_dia)
                data.append(fecha_nueva_mes)
                data.append(fecha_nueva_hora)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "3":
                data = []
                print("Eliminar historial de paciente")
                rut = input("Ingrese rut de paciente: ")
                data.append("el")
                data.append(rut)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "4":
                break
    if opcion == "8":
        while True:
            accion = menuGboxs()
            servicio = "gboxs"
            if accion == "1":
                data = []
                print("Crear box")
                numero_box = input("Ingrese numero de box: ")
                piso = input("Ingrese piso de box: ")
                data.append("cr")
                data.append(numero_box)
                data.append(piso)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "2":
                data = []
                print("asignar box")
                rut = input("rut del medico: ")
                box = input("id de box asignado: ")
                data.append("as")
                data.append(rut)
                data.append(box)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "3":
                break
    if opcion == "9":
        # realiza el munu para smeds
        while True:
            accion = menuSmeds()
            servicio = "smeds"
            if accion == "1":
                data = []
                print("Ver horas trabajadas")
                rut = input("Ingrese rut de médico: ")
                data.append("ht")
                data.append(rut)
                msg = crearMsg(data, servicio)
                # envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "2":
                break
    if opcion == "10":
        while True:
            accion = menuHmeds()
            servicio = "hmeds"
            if accion == "1":
                data = []
                print("Ver historial médico")
                rut = input("Ingrese rut de médico: ")
                data.append("vr")
                data.append(rut)
                print(data)
                msg = crearMsg(data, servicio)
                # Envía mensaje a través del bus
                enviarMsg(msg.encode())
            if accion == "2":
                print("Editar historial de médico")
                rut = input("Ingrese RUT del médico: ")
                fecha_antigua_dia = input("Ingrese día actual de la cita: ")
                fecha_antigua_mes = input("Ingrese mes actual de la cita: ")
                fecha_antigua_hora = input("Ingrese hora actual de la cita: ")
                fecha_nueva_dia = input("Ingrese día nuevo de la cita: ")
                fecha_nueva_mes = input("Ingrese mes nuevo de la cita: ")
                fecha_nueva_hora = input("Ingrese hora nueva de la cita: ")
                data.append("ed")
                data.append(rut)
                data.append(fecha_antigua_dia)
                data.append(fecha_antigua_mes)
                data.append(fecha_antigua_hora)
                data.append(fecha_nueva_dia)
                data.append(fecha_nueva_mes)
                data.append(fecha_nueva_hora)
                msg = crearMsg(data, servicio)
                # Envía el mensaje a través del bus
                enviarMsg(msg.encode())
            if accion == "3":
                data = []
                print("Eliminar historial médico")
                rut = input("Ingrese rut de médico: ")
                data.append("el")
                data.append(rut)
                msg = crearMsg(data, servicio)
                # Envía mensaje a través del bus
                enviarMsg(msg.encode())
            if accion == "4":
                break

    if opcion == "11":
        while True:
            accion = menuBhora()
            servicio = "bhora"
            if accion == "1":
                data = []
                print("Bloqueo de horario")
                rut = input("Ingrese rut de médico: ")
                dia = input("Ingrese el dia: ")
                hora = input("Ingrese la hora: ")
                data.append("bh")
                data.append(rut)
                data.append(dia)
                data.append(hora)
                msg = crearMsg(data, servicio)
                # Envía mensaje a través del bus
                enviarMsg(msg.encode())
            if accion == "2":
                data = []
                print("Desbloqueo de horario")
                rut = input("Ingrese rut de médico: ")
                dia = input("Ingrese el dia: ")
                hora = input("Ingrese la hora: ")
                data.append("dh")
                data.append(rut)
                data.append(dia)
                data.append(hora)
                msg = crearMsg(data, servicio)
                # Envía el mensaje a través del bus
                enviarMsg(msg.encode())
            if accion == "3":
                data = []
                print("Agregar horario")
                rut = input("Ingrese rut de médico: ")
                dia = input("Ingrese el dia: ")
                hora = input("Ingrese la hora: ")
                data.append("ah")
                data.append(rut)
                data.append(dia)
                data.append(hora)
                msg = crearMsg(data, servicio)
                # Envía mensaje a través del bus
                enviarMsg(msg.encode())
            if accion == "4":
                break
    if opcion == "12":
        servicio = "aturp"
        data.append("an")
        msg = crearMsg(data, servicio)
        enviarMsg(msg.encode())

    if opcion == "0":
        print("Saliendo del sistema")
        sock.close()
        break
