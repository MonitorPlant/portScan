from socket import socket, AF_INET, SOCK_STREAM

HOST = 'localhost'
MASTER_PORT = 50000
MAX_MESSAGE = 2048
NUM_THREAD = 1

CHR_EOT   = '\04'
CHR_ADD   = '\05'
CHR_DEL   = '\06'
CHR_STATE = '\07'
ENABLE    = '\12'
DISABLE   = '\14'

received_port = []
device_name = []

def availablePort( device_name ):
    port = 50001
    while True:
        if port == 56130:
            continue
        if port 
    
        test_sock = socket( AF_INET, SOCK_STREAM )
        return_code = sock.connect_ex( ( HOST, currnent_port ) )

receive_socket = socket( AF_INET, SOCK_STREAM )
receive_socket.bind( ( HOST, PORT ) )
receive_socket.listen( NUM_THREAD )

print( 'receiver ready, NUM_THREAD = ' + str( NUM_THREAD ) )

while True:
    try:
        connect = receive_socket.accept()
        name    = connect.recv( MAX_MESSAGE ).decode( 'utf-8' )
        message = connect.recv( MAX_MESSAGE ).decode( 'utf-8' )
        connect.close()

    if( message == CHR_EOT ):
        break

    availablePort( message )

        print( 'message:' + mess )
    except:
        print( 'Error:' + mess )

sock.close()
print( 'end of receiver' )
