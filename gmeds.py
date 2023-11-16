import socket
from funciones_gmeds import *
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # inscribir servicio en el bus, se hace para cada servicio
    # los ultimos 5 caracteres son el nombre del servicio
    message = b'00010sinitgmeds'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = int(sock.recv(5))
    # leer repsuesta de bus cuando hace el snit
    while amount_received < amount_expected:
        data = sock.recv(amount_expected - amount_received)
        amount_received += len(data)
        print('received {!r}'.format(data))

    # espera mesaje para el servicio
    while True:
        print("Waiting for transaction")
        amount_received = 0  # lo que ha leido
        amount_expected = int(sock.recv(5))  # lo que espera leer
        data = b''
        while amount_received < amount_expected:

            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            print('received {!r}'.format(data))

        accion = data.decode()[5:7]
        parametros = data.decode()[8:]
        print("Accion:", accion)
        print("Parametros:", parametros)
        resp = b''
        print("Processing ...")

        if accion == 'cr':
            result = crearMedico(parametros)
            if result:
                resp = b'00011gmedsCreado'
            else:
                resp = b'00013gmedsNoCreado'
        if accion == 'el':
            result = eliminarMedico(parametros)
            if result:
                resp = b'00014gmedsEliminado'
            else:
                resp = b'00016gmedsNoEliminado'
        if accion == 'ed':
            result = editarMedico(parametros)
            if result:
                resp = b'00012gmedsEditado'
            else:
                resp = b'00014gmedsNoEditado'

        print('sending {!r}'.format(resp))
        sock.sendall(resp)

finally:
    print('closing socket')
    sock.close()
