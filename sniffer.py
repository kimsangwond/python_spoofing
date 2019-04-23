import socket
import struct
from packet import *

class Packet:
	def __init__( self, raw ):

		self._eth = Eth( raw[:14] )

		if self._eth.type == 0x0800:
			self.analyze_ip( raw[14:] )

	def analyze_ip( self, raw ):
		
		self._ip = Ip( raw )

		if self._ip.type == 17:
			self.analyze_udp( raw[20:] )

	def analyze_udp( self, raw ):
		self._udp = Udp( raw )

	@property
	def eth( self ):
		return self._eth

	@property
	def ip( self ):
		return self._ip

	@property
	def udp( self ):
		return self._udp
	
sock = socket.socket(socket.PF_PACKET,socket.SOCK_RAW)
sock.bind(('enp0s5',socket.SOCK_RAW))

while True:

	data , addr = sock.recvfrom(65535)
	packet = Packet(data) 

	if packet.eth.type == 0x0800 and packet.eth.src == '192.168.6.41':
		print( "data : " , data )
		print( packet.ip.src + ' => ' + packet.ip.dst )
		print()
