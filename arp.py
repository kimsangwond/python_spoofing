import struct

class Arp:

  def __init__( self, raw=None ):
    if raw != None:
      self._hard_type = raw[:2]
      self._proto_type = raw[2:4]
      self._hard_len = raw[4:5]
      self._proto_len = raw[5:6]
      self._opcode = raw[6:8]
      self._sender_mac = raw[8:14]
      self._sender_ip = raw[14:18]
      self._target_mac = raw[18:24]
      self._target_ip = raw[24:28]

  @property
  def header( self ):
    return self._hard_type + self._proto_type + self._hard_len + self._proto_len \
           + self._opcode + self._sender_mac + self._sender_ip + self._target_mac \
           + self._target_ip

  @property
  def hard_type( self ):
    (hard_type,) = struct.unpack('!H', self._hard_type)
    return hard_type

  @hard_type.setter
  def hard_type( self, type ):
    type = struct.pack('!H', type)
    self._hard_type = type

  @property
  def proto_type( self ):
    (proto_type,) = struct.unpack('!H', self._proto_type)

  @proto_type.setter
  def proto_type( self, type ):
    type = struct.pack('!H', type)
    self._proto_type = type

  @property
  def hard_len( self ):
    (hard_len,) = struct.unpack('!B', self._hard_len)
    return hard_len

  @hard_len.setter
  def hard_len( self, len ):
    len = struct.pack('!B', len )
    self._hard_len = len

  @property
  def proto_len( self ):
    (proto_len,) = struct.unpack('!B', self._proto_len)
    return proto_len

  @proto_len.setter
  def proto_len( self, len ):
    len = struct.pack('!B', len)
    self._proto_len = len

  @property
  def opcode( self ):
    (opcode,) = struct.unpack('!H', self._opcode)
    return self._opcode

  @opcode.setter
  def opcode( self, opcode ):
    opcode = struct.pack('!H', opcode)
    self._opcode = opcode

  @property
  def sender_mac( self ):
    sender_mac = struct.unpack('!6B', self._sender_mac)
    sender_mac = '%02x:%02x:%02x:%02x:%02x:%02x' % sender_mac
    return sender_mac

  @sender_mac.setter
  def sender_mac( self, mac ):
    mac = mac.split(':')
    for i in range( len(mac) ):
      mac[i] = int( mac[i], 16 )

    self._sender_mac = b''
    for i in range( len(mac) ):
      self._sender_mac += struct.pack('!B', mac[i])

  @property
  def sender_ip( self ):
    sender_ip = struct.unpack('!4B', self._sender_ip)
    sender_ip = '%d.%d.%d.%d' % sender_ip
    return sender_ip

  @sender_ip.setter
  def sender_ip( self, ip ):
    ip = ip.split('.')
    for i in range( len(ip) ):
      ip[i] = int( ip[i] )

    self._sender_ip = b''
    for i in range( len(ip) ):
      self._sender_ip += struct.pack('!B', ip[i])

  @property
  def target_mac( self ):
    target_mac = struct.unpack('!6B', self._target_mac)
    target_mac = '%02x:%02x:%02x:%02x:%02x:%02x' % target_mac
    return target_mac

  @target_mac.setter
  def target_mac( self, mac ):
    mac = mac.split(':')
    for i in range( len(mac) ):
      mac[i] = int( mac[i], 16 )

    self._target_mac =b''
    for i in range( len(mac) ):
      self._target_mac += struct.pack('!B', mac[i])

  @property
  def target_ip( self ):
    target_ip = struct.unpack('!4B', self._target_ip)
    target_ip = '%d.%d.%d.%d' % target_ip
    return target_ip

  @target_ip.setter
  def target_ip( self, ip):
    ip = ip.split('.')
    for i in range( len(ip) ):
      ip[i] = int( ip[i] )

    self._target_ip = b''
    for i in range( len(ip) ):
      self._target_ip += struct.pack('!B', ip[i])