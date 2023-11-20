import socket
from funciones_hmeds import *
from funciones_cliente import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = b'00011sinithmeds'  # Ajustar el tamaño y el nombre del servicio
    print('sending {!r}'.format(message))
    sock.sendall(message)
    
    amount_received = 0
    amount_expected = int(sock.recv(5))
    print(amount_expected)
    while amount_received < amount_expected:
        data = sock.recv(amount_expected - amount_received)
        amount_received += len(data)
        print('received {!r}'.format(data))
    
    while True:
        print("Waiting for transaction")
        amount_received = 0
        amount_expected = int(sock.recv(5))
        data = b''
        while amount_received < amount_expected:
            data = sock.recv(amount_expected - amount_received)
            amount_received += len(data)
            print('received prueba {!r}'.format(data))
      
        accion = data.decode()[5:7]
        parametros = data.decode()[8:]
        print(accion)
        print(parametros)
        resp = b''
        print("Processing ...")
        
        if accion == 'vr':  # Ver historial médico
            result = verHistorialMedico(parametros)
            respuesta_historial = str(result)
            longitud_respuesta = len(respuesta_historial)
            mensaje_respuesta = f"{longitud_respuesta:05d}hmeds" + respuesta_historial
            resp = mensaje_respuesta.encode()
            
        if accion == 'el':  # Eliminar historial médico
            result = eliminarHistorialMedico(parametros)
            if result:
                resp = f'00014hmeds{result}'.encode()
            else:
                resp = f'00016hmeds{result}'.encode()

        if accion == 'ed':
            # Realizar acción para editar historial médico
            result = editarHistorialMedico(parametros)  # Manejar adecuadamente los parámetros
            
            if result:
                resp = f'00012hmeds{result}'.encode()
            else:
                resp = f'00014hmeds{result}'.encode() 
    
        
        print('sending {!r}'.format(resp))
        sock.sendall(resp)

finally:
    print('closing socket')
    sock.close()
