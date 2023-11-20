import socket
# Asumiendo que tienes un módulo funciones_smeds con las funciones necesarias para gestionar los médicos
from funciones_smeds import *

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el servidor está escuchando
server_address = ('localhost', 5001)
print('Connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Inscribir servicio en el bus, se hace para cada servicio
    message = b'00010sinitsmeds'  # Asegúrate de cambiar 'gboxs' por 'smeds' si es necesario
    print('Sending {!r}'.format(message))
    sock.sendall(message)
    
    amount_received = 0
    amount_expected = int(sock.recv(5))
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
      
        # Aquí añadirías el manejo de acciones para 'smeds'
        if accion == 'ht': 
            id_medico = parametros
            horas_trabajadas = calcularHorasTrabajadasPorRut(id_medico)
            print (horas_trabajadas)    
            respuesta_historial = str(horas_trabajadas)
            # Formar el mensaje con longitud y contenido
            longitud_respuesta = len(respuesta_historial)
            mensaje_respuesta = f"{longitud_respuesta:05d}smeds" + respuesta_historial
            # Codificar y enviar
            resp = mensaje_respuesta.encode() 

        print('Sending {!r}'.format(resp))
        sock.sendall(resp)

finally:
    print('Closing socket')
    sock.close()
