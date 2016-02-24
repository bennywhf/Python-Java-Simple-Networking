import socket

def main():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 9876
    MESSAGE = "Watta Fook!"
        
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE
       
    sock = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    print("From Server: " + data)

main()
