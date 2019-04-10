#!/usr/bin/python
#-*- coding: utf-8 -*-

import subprocess
import sys
import re
import struct
from threading import *
from time import sleep
from socket import *
from uuid import getnode as get_mac
import argparse
import binascii
import ifaddr
from scapy.all import*
import netifaces

if __name__ == '__main__':
	adapters = ifaddr.get_adapters()
	for adapter in adapters:
		print ("IPs of network adapter " + adapter.nice_name)
		for ip in adapter.ips:
			print ("   %s/%s" % (ip.ip, ip.network_prefix))

	conf.iface= input('input nic: ')

	print(netifaces.gateways())

	attackerIP= socket.gethostbyname(socket.gethostname())
	gatewayIP= attackerIP[:-1]+str(1)
	victimIP= input('victim IP: ')
