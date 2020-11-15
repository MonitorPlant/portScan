from socket import socket, AF_INET, SOCK_STREAM

HOST = 'localhost'
PORT = 51400
MAX_MESSAGE = 2048
NUM_THREAD = 1

CHR_CAN = '\18'
CHR_EOT = '\04'

def com_receiver():

    sock = socket( AF_INET, SOCK_STREAM )
    sock.bind( ( HOST, PORT ) )
    sock.listen( NUM_THREAD )
    print( 'receiver ready, NUM_THREAD = ' + str( NUM_THREAD ) )

    while True:
        try:
            conn, addr = sock.accept()
            mess       = conn.recv( MAX_MESSAGE ).decode( 'utf-8' )
            conn.close()

            if( mess == CHR_EOT ):
                break

            if( mess == CHR_CHAN ):
                print( 'cancel' )
                continue

            print( 'message:' + mess )

        except:
            print( 'Error:' + mess )

    sock.close()
    print( 'end of receiver' )

def proc():
    com_receiver()

proc()
