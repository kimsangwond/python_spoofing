class Udp:

  def __init__( self, raw=None ):
    if raw != None:
      self._src = raw[:2]
      self._dst = raw[2:4]
      self._length = raw[4:6]
      self._check_sum = raw[6:8]
      self._data = raw[8:]

  @property
  def header( self ):
    return self._src + self._dst + self._length + self._check_sum + self._data

  @property
  def src( self ):
    (src,) = struct.unpack('!H', self._src)
    return src

  @property
  def dst( self ):
    (dst,) = struct.unpack('!H', self._dst)
    return dst

  @property
  def length( self ):
    (length,) = struct.unpack('!H', self._length)
    return length