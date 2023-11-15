import socket
from funciones_aturp import *

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el servidor está escuchando
server_address = ('localhost', 5001)  # Actualiza con la dirección y puerto correctos
print('Conectando a {} puerto {}'.format(*server_address))
sock.connect(server_address)

try:
    # Registrar el servicio en el bus, utilizando los últimos 5 caracteres como nombre del servicio
    message = b'00009sinitaturp'
    print('Enviando {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = int(sock.recv(5))

    while amount_received < amount_expected:
        data = sock.recv(amount_expected - amount_received)
        amount_received += len(data)
        print('Recibido {!r}'.format(data))

    while True:
        print("Esperando transacción")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        data = b''

        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            print('Recibido {!r}'.format(data))

        accion = data.decode()[5:7]
        parametros = data.decode()[8:]
        print(accion)
        print(parametros)
        resp = b''
        print("Procesando...")

        if accion == 'gn':
            result = generarNumero()
            resp = f'00007aturp{result}'.encode()

        if accion == 'an':
            result = avanzarNumero()
            resp = f'00009aturp{result}'.encode()

        print('Enviando {!r}'.format(resp))
        sock.sendall(resp)

        # Receiving the response from the 'an' action and printing it
        

finally:
    print('Cerrando el socket')
    sock.close()
