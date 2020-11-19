import socket

target_host = 'localhost'

available_port = []

port = 49152

def portAvailable( port ):
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    return_code = sock.connect_ex( ( target_host, port ) )
    sock.close()
    return return_code

while len(available_port) < 127 and port < 65535:
    
    if portAvailable( port ) != 0:
        available_port.append( port )

    port = port + 1

print( "Complate!" )
print( available_port )
