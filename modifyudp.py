import socket 

s = socket.socket(socket.AF_INET, scoket.SOCK_DGRAM)

UDP_IP_ADDRESS = "192.168.0.132"
UDP_PORT_NO = 7777
Message = "Hello, server"

s.sendto(Message.endcode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
