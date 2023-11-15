import socket
from funciones_cliente import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5001)
print('Conectando a {} puerto {}'.format(*server_address))
sock.connect(server_address)

def enviarMsg(message):
    try:
        # enviar mensaje
        # print ('sending {!r}'.format (message))
        sock.sendall(message)

        # recibir mensaje
        response_len_str = sock.recv(5).decode()
        response_len = int(response_len_str)
        response_service = sock.recv(5).decode()
        response_data = sock.recv(response_len - 5).decode()

        print(f"Received: {response_data} ")
    finally:
        # print ('closing socket')
        # sock.close ()
        return response_data

print("")
print("Sistema de gestión de Centro Médico JRG")

data = []
while True:
    # menu principal esta en una funcion de clientes
    print("")
    opcion = menuPaciente()
    print("")
    # hay un while true por cada opcion del menu principal
    if opcion == "1":
        data = []
        servicio = "aturp"
        print("Generando numero")
        rut = input("Ingrese su rut: ")
        data.append("gn")
        data.append(rut)
        msg = crearMsg(data, servicio)
        enviarMsg(msg.encode())
        

    if opcion == "0":
        print("Saliendo del sistema")
        sock.close()
        break
