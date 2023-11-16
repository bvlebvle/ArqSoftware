import socket
from funciones_cliente import *
from funciones_bhora import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5001)
print('Connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = b'00010sinitbhora'  # Ajustar el tamaño y el nombre del servicio
    print('Sending {!r}'.format(message))
    sock.sendall(message)
    
    amount_received = 0
    amount_expected = int(sock.recv(5))
    print(amount_expected)
    while amount_received < amount_expected:
        data = sock.recv(amount_expected - amount_received)
        amount_received += len(data)
        print('Received {!r}'.format(data))
    
    while True:
        print("Waiting for transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        data = b''
        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            print('Received prueba {!r}'.format(data))
      
        accion = data.decode()[5:7]
        parametros = data.decode()[8:]
        print(accion)
        print(parametros)
        resp = b''
        print("Processing ...")
        
        if accion == 'bh':  # Bloqueo de horas
            # Aquí llamas a la función correspondiente con los parámetros adecuados
            result = bloquearHoras(parametros)
            resp = f'00009bhora{result}'.encode()

        if accion == 'dh':  # Bloqueo de horas
            # Aquí llamas a la función correspondiente con los parámetros adecuados
            result = desbloquearHoras(parametros)
            resp = f'00009bhora{result}'.encode()
        
        print('Sending {!r}'.format(resp))
        sock.sendall(resp)

finally:
    print('Closing socket')
    sock.close()
