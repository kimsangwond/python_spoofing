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

  @property
  def proto_type( self ):
    (proto_type,) = struct.unpack('!H', self._proto_type)

  @property
  def hard_len( self ):
    (hard_len,) = struct.unpack('!B', self._hard_len)
    return hard_len

  @property
  def proto_len( self ):
    (proto_len,) = struct.unpack('!B', self._proto_len)
    return proto_len

  @property
  def opcode( self ):
    (opcode,) = struct.unpack('!H', self._opcode)
    return self._opcode

  @property
    sender_mac = struct.unpack('!6B', self._sender_mac)
    sender_mac = '%02x:%02x:%02x:%02x:%02x:%02x' % sender_mac
    return sender_mac

  @property
    sender_ip = struct.unpack('!4B', self._sender_ip)
    sender_ip = '%d.%d.%d.%d' % sender_ip
    return sender_ip

  @property
    target_mac = struct.unpack('!6B', self._target_mac)
    target_mac = '%02x:%02x:%02x:%02x:%02x:%02x' % target_mac
    return target_mac

  @property
    target_ip = struct.unpack('!4B', self._target_ip)
    target_ip = '%d.%d.%d.%d' % target_ip
    return target_ip