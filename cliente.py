import socket
from funciones_gmeds import *
# Create a TCP/IP socket
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5001)
print ('connecting to {} port {}'.format (*server_address))
sock.connect (server_address)

try:
    message = b'00010sinitclien'
    print ('sending {!r}'.format (message))
    sock.sendall (message)
    amount_received = 0
    amount_expected = int(sock.recv (5))
    
    #leer repsuesta de bus cuando hace el snit
    while amount_received < amount_expected:
        data = sock.recv (amount_expected - amount_received)
        amount_received += len (data)
        print('received {!r}'.format(data))

    while True:
      print ("Waiting for transaction")
      #enviar cosas
      peticion = "00027gmedscr-paula-nunez-general"
      print ('sending {!r}'.format (peticion))
      peticion = str(peticion) 
      sock.sendall(bytes(peticion, 'utf-8'))
      
      amount_received = 0
      amount_expected = int(sock.recv (5))

      while amount_received < amount_expected:
          data = sock.recv (amount_expected - amount_received)
          amount_received += len (data)
          print('received {!r}'.format(data))
       
      print ("Processing ...")
      resp = '{:05d}'.format (len(data)) + data.decode ()
      print ("Send answer (if needed)")
      print ('sending {}'.format (resp))
      sock.sendall (bytes(resp, 'utf-8'))
    
    
    
finally:
    print ('closing socket')
    sock.close ()
