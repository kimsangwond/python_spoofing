from header.ip import *
from header.udp import *
from header.arp import *

class Packet:

  def __init__( self, raw ):
    self._eth = Eth( raw[:14] )
    if self._eth.type == 0x0800:
      self.analyze_ip( raw[14:] )
 
  if self._eth.type == 0x0806:
    self.analyze_arp( raw[14:] )
  

  def analyze_ip( self, raw ):
    self._ip = Ip( raw )
    if self._ip.type == 17:
      self.analyze_udp( raw[20:] )

  def analyze_udp( self, raw ):
    self._udp = Udp( raw )

  def analyze_arp( self, raw ):
    self._arp = Arp( raw )  
 
  @property
  def eth( self ):
    return self._eth

  @property
  def ip( self ):
    return self._ip

  @property
  def arp( self ):
    return self._arp