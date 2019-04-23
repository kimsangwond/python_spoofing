import struct

class Eth:
  def __init__( self, raw=None ):
  if raw != None:
    self._dst = raw[:6]
    self._src = raw[6:12]
    self._type = raw[12:14]

  @property
  def header( self ):
    return self._dst + self._src + self._type

  @property
  def dst( self ):
    dst = struct.unpack('!6B', self._dst)
    dst = '%02x:%02x:%02x:%02x:%02x:%02x' % dst
    return dst

  @property
  def src( self ):
    src = struct.unpack('!6B', self._src)
    src = '%02x:%02x:%02x:%02x:%02x:%02x' % src
    return src

  @property
  def type( self ):
    (type,) = struct.unpack('!H', self._type)
    return type