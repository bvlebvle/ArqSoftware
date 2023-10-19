
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
    print("0. Salir")
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
