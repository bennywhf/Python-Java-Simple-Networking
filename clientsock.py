import socket
import sys

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = ('localhost',9090)
    sock.connect(server_address)

    try:
        data = sock.recv(18)
        print(data)
    except Exception as e:
        print "Error "+ e
    finally:
        sock.close()

main()
