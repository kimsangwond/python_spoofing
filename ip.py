import struct

class Ip:

  def __init__( self, raw=None ):
    if raw != None:
      self._verlen = raw[:1]
      self._service = raw[1:2]
      self._total = raw[2:4]
      self._id = raw[4:6]
      self._flag_and_offset = raw[6:8]
      self._ttl = raw[8:9]
      self._type = raw[9:10]
      self._check_sum = raw[10:12]
      self._src = raw[12:16]
      self._dst = raw[16:20]

  @property
  def header( self ):
    return self._verlan + self._service + self._total + self._id + self._flag_and_offset + self._ttl + self._type + self._check_sum + self._src + self._dst

  @property
  def ver( self ):
    (ver,) = struct.unpack('!B', self._verlen)
    ver = verlen >> 4
    return ver

  @property
  def length( self ):
    (len,) = struct.unpack('!B', self._verlen)

  @property
  def service( self ):
    (service,) = struct.unpack('!B', self._service)
    return service

  @property
  def total( self ):
    (total,) = sturct.unpack('!H', self._total)
    return total

  @property
  def id( self ):
    (id,) = struct.unpack('!H', self._id)
    return id

  @property
  def flag( self ):
    (flag,) = struct.unpack('!H', self._flag_and_offset)
    flag = flag >> 13
    return flag

  @property
  def offset( self ):
    (offset,) = struct.unpack('!H', self._flag_and_offset)
    offset = (offset & 0x1FFF) << 2
    return offset

  @property
  def ttl( self ):
    (ttl,) = struct.unpack('!B', self._ttl)
    return ttl

  @property
  def type( self ):
    (type,) = struct.unpack('!B', self._type)

  @property
  def check_sum( self ):
    (check_sum,) = struct.unpack('!H', self._check_sum)

  @property
  def src( self ):
    src = struct.unpack('!4B', self._src)
    src = '%d.%d.%d.%d' % src
    return src

  @property
  def dst( self ):
    dst = struct.unpack('!4B', self._dst)
    dst = '%d.%d.%d.%d' % dst
    return dst