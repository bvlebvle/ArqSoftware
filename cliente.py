import socket
from funciones_gmeds import *
from funciones_cliente import *
# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5001)
print ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)

def enviarMsg(message):
    try:
        #enviar mensaje
        print ('sending {!r}'.format (message))
        sock.sendall (message)
        
        #recibir mensaje
        response_len_str = sock.recv(5).decode()
        response_len = int(response_len_str)
        response_service = sock.recv(5).decode()
        response_data = sock.recv(response_len - 5).decode()

        print(f"Received: {response_data}")
    finally:
        print ('closing socket')
        sock.close ()
    return response_data

print("Sistema de gestión de Centro Médico JRG")


data = []
while True:
    #menu principal esta en una funcion de clientes
    print("")
    opcion = menuPrincipal()
    print("")
    #hay un while true por cada opcion del menu principal
    while True:
        if opcion == "1":
            #menu de gestion de medicos esta en una funcion de clientes
            accion = menuGmeds()
            servicio = "gmeds"
            if accion == "1":
                print("Creación de médico")
                nombre = input("Ingrese nombre de médico: ")
                apellido = input("Ingrese apellido de médico: ")
                especialidad = input("Ingrese especialidad de médico: ")
                data.append("cr")
                data.append(nombre)
                data.append(apellido)
                data.append(especialidad)
                msg = crearMsg(data, servicio)
                #envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion =="2":
                print("Edición de médico")
                nombre = input("Ingrese nombre de médico: ")
                apellido = input("Ingrese apellido de médico: ")
                especialidad = input("Ingrese especialidad de médico: ")
                new_nombre = input("Ingrese nuevo nombre de médico: ")
                new_apellido = input("Ingrese nuevo apellido de médico: ")
                new_especialidad = input("Ingrese nuevo especialidad de médico: ")
                data.append("ed")
                data.append(nombre)
                data.append(apellido)
                data.append(especialidad)
                data.append(new_nombre)
                data.append(new_apellido)
                data.append(new_especialidad)
                msg = crearMsg(data, servicio)
                #envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "3":
                print("Eliminación de médico")
                nombre = input("Ingrese nombre de médico: ")
                apellido = input("Ingrese apellido de médico: ")
                especialidad = input("Ingrese especialidad de médico: ")
                data.append("el")
                data.append(nombre)
                data.append(apellido)
                data.append(especialidad)
                msg = crearMsg(data, servicio)
                #envia mensaje a traves del bus
                enviarMsg(msg.encode())
            if accion == "4":
                break
    
         

            



    
