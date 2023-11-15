import socket
# Asumiendo que tienes un módulo funciones_gboxs con las funciones necesarias para gestionar las salas
from funciones_gboxs import *

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el servidor está escuchando
server_address = ('localhost', 5001)
print('Connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Inscribir servicio en el bus, se hace para cada servicio
    # Los últimos 5 caracteres son el nombre del servicio
    message = b'00010sinitgboxs'
    print('Sending {!r}'.format(message))
    sock.sendall(message)
    
    amount_received = 0
    amount_expected = int(sock.recv(5))
    # Leer respuesta de bus cuando se hace el sinit
    while amount_received < amount_expected:
        data = sock.recv(amount_expected - amount_received)
        amount_received += len(data)
        print('Received {!r}'.format(data))
    
    # Esperar mensaje para el servicio
    while True:
        print("Waiting for transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        data = b''
        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            print('Received {!r}'.format(data))
      
        accion = data.decode()[5:7]
        parametros = data.decode()[8:]
        print(accion)
        print(parametros)
        resp = b''
        print("Processing ...")
      
        # Aquí añadirías el manejo de acciones para 'gboxs' como crear sala, asignar sala, etc.
        # Por ejemplo:
        if accion == 'as':  # 'as' podría ser la acción para 'asignar sala'
            print ("los parametros son: ",parametros)
            result = asignar_sala(parametros)
            if result: 
                resp = b'00017gboxsSalaAsignada'
            else: 
                resp = b'00019gboxsSalaNoAsignada'  
        elif accion == 'cr': 
            result = crear_sala(parametros)
            if result: 
                resp = b'00015gboxsSalacreada'
            else: 
                resp = b'00018gboxsSalaNocreada'
        print('Sending {!r}'.format(resp))
        sock.sendall(resp)

finally:
    print('Closing socket')
    sock.close()
