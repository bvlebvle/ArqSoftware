
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
    print ("1. Gestión de médicos")
    print ("2. Gestión de horarios de médicos") 
    print ("3. Gestión de citas")
    print ("4. Historial de pacientes")
    print ("5. Gestión de boxs")
    print ("6. Segimiento de médicos")
    print("0. Salir de sistema")
    opcion = input("Ingrese el número de la opción que desea: ")
    return opcion

def menuGmeds():
	print("Gestión de médicos")
	print("Puede escoger entre las siguientes opciones:")
	print("1. Crear médico")
	print("2. Editar médico")
	print("3. Eliminar médico")
	print ("4. Volver al menú principal")
	accion = input("Ingrese el número de la opción que desea: ")
	return accion
 
def menuCrhor():
    print("Gestión de horarios de médicos")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Crear horario")
    print("2. Editar horario")
    print("3. Eliminar horario")
    print ("4. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion   

def menuGcita():
    print("Gestión de citas")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Crear cita")
    print("2. Editar cita")
    print("3. Eliminar cita")
    print ("4. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion

data=["cr","nombre", "apellido", "especialidad"]
servicio = "crmed"
crearMsg(data, servicio)

def menuHpacs():
    print("Historial de pacientes")
    print("Puede escoger entre los siguientes servicios:")
    print ("1. ver historial de paciente")
    print ("2. editar historial de paciente")
    print ("3. eliminar historial de paciente")
    print ("4. Volver al menú principal")
    opcion = input("Ingrese el número de la opción que desea: ")
    return opcion

def menuGboxs():
    print("Gestión de boxs")
    print("Puede escoger entre las siguientes opciones:")
    print("1. Crear box")
    print("2. Asignar box")
    print ("3. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion

def menuSmeds():
    print("Puede escoger entre las siguientes opciones:")
    print("1. Horas trabajadas por medico")
    print ("2. Volver al menú principal")
    accion = input("Ingrese el número de la opción que desea: ")
    return accion

