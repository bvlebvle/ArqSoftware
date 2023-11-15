import socket
# Asegúrate de importar las funciones necesarias para manejar el historial de pacientes
from funciones_hpacs import *
from funciones_cliente import *

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el servidor está escuchando
server_address = ('localhost', 5001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Inscribir servicio en el bus, se hace para cada servicio
    # Los últimos 5 caracteres son el nombre del servicio
    message = b'00010sinithpcss'
    print('sending {!r}'.format(message))
    sock.sendall(message)
    amount_received = 0
    amount_expected = int(sock.recv(5))
    print(amount_expected)
    # Leer respuesta de bus cuando hace el snit
    while amount_received < amount_expected:
        data = sock.recv(amount_expected - amount_received)
        amount_received += len(data)
        print('received {!r}'.format(data))
    
    # Esperar mensaje para el servicio
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
        if accion == 'vr':
            result = verHistorialPaciente(parametros)
            respuesta_historial = str(result)
            # Formar el mensaje con longitud y contenido
            longitud_respuesta = len(respuesta_historial)
            mensaje_respuesta = f"{longitud_respuesta:05d}hpcss" + respuesta_historial
            # Codificar y enviar
            resp = mensaje_respuesta.encode() 
        if accion == 'el':
            result = eliminarHistorialPaciente(parametros)
            if result: 
                resp = b'00014hpcssEliminado'
            else: 
                resp = b'00016hpcssNoEliminado'
        if accion == 'ed':
            print("parametros: ", parametros)
            result = editarHistorialPaciente(parametros)
            if result: 
                resp = b'00012hpcssEditado'
            else: 
                resp = b'00014hpcssNoEditado'        

        print('sending {!r}'.format(resp))
        sock.sendall(resp)

finally:
    print('closing socket')
    sock.close()
