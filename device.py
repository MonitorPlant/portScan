from socket import socket, AF_INET, SOCK_STREAM

HOST = 'localhost'
MASTER_PORT = 50001

CHR_EOT = '\04'

def com_send( mess ):
    
    while True:
        try:
            
            sock = socket( AF_INET, SOCK_STREAM )
            sock.connect( ( HOST, PORT ) )

            sock.send( mess.encode( 'utf-8' ) )

            sock.close()
            break

        except:
            print( 'retry: ' + mess )

def proc():
    com_send( 'message test' )

while input() != 'exit':
    com_send( 'message test' )

exit()
