import socket
from funciones_vmeds import *
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # inscribir servicio en el bus, se hace para cada servicio
    # los ultimos 5 caracteres son el nombre del servicio
    message = b'00010sinitvmeds'
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
        print("La accion es: ", accion)
        print("Parametros", parametros)
        resp = b''
        print("Processing ...")
        print("")
        print("")

        fecha = datetime.datetime.now()
        dia = fecha.day
        mes = fecha.month
        if accion == 'vd':
            result = visualizarAgendaDiaria(dia, mes, "")
            respuesta_agenda = str(result)
            longitud_respuesta = len(respuesta_agenda)
            mensaje_respuesta = f"{longitud_respuesta:05d}vmeds" + \
                respuesta_agenda
            resp = mensaje_respuesta.encode()
        if accion == 'vs':
            result = visualizarAgendaSemana(dia, mes, "")
            respuesta_agenda = str(result)
            longitud_respuesta = len(respuesta_agenda)
            mensaje_respuesta = f"{longitud_respuesta:05d}vmeds" + \
                respuesta_agenda
            resp = mensaje_respuesta.encode()
        if accion == 'dm':
            result = diaMedico(dia, mes, parametros)
            respuesta_agenda = str(result)
            longitud_respuesta = len(respuesta_agenda)
            mensaje_respuesta = f"{longitud_respuesta:05d}vmeds" + \
                respuesta_agenda
            resp = mensaje_respuesta.encode()
        if accion == 'sm':
            result = semanaMedico(dia, mes, parametros)
            respuesta_agenda = str(result)
            longitud_respuesta = len(respuesta_agenda)
            mensaje_respuesta = f"{longitud_respuesta:05d}vmeds" + \
                respuesta_agenda
            resp = mensaje_respuesta.encode()

        print("")
        print("")
        print('sending {!r}'.format(resp))
        sock.sendall(resp)

finally:
    print('closing socket')
    sock.close()
