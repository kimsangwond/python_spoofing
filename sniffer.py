import socket
import struct
#from packet import *
from packet import *
	
sock = socket.socket(socket.PF_PACKET,socket.SOCK_RAW)
sock.bind(('enp0s5',socket.SOCK_RAW))

while True:

	data , addr = sock.recvfrom(65535)
	packet = Packet(data) 

	if packet.eth.type == 0x0800 and packet.eth.src == '192.168.6.41':
		print( "data : " , data )
		print( packet.ip.src + ' => ' + packet.ip.dst )
		print()
