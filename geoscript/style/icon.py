from geoscript.util import toURL
from geoscript.style import util
from geoscript.style.symbolizer import Symbolizer
from org.geotools.styling import PointSymbolizer, PolygonSymbolizer

class Icon(Symbolizer):
  """
  Symbolizer for an external image or glyph. 

  An icon is composed is of a ``url`` that specifies the location of the source image
  and a ``format`` that specifies the format or the mime type of the image.

  >>> icon = Icon('tests/work/colorblocks.png', 'image/png')
  >>> icon = Icon('http://v2.suite.opengeo.org/geoserver/styles/smileyface.png', 'image/png')
  """
  def __init__(self, url, format):
    Symbolizer.__init__(self)
    self.url = toURL(url)
    self.format = format

  def _prepare(self, rule):
    syms = util.symbolizers(rule, PointSymbolizer)
    for sym in syms:
      self._apply(sym)
    
  def _apply(self, sym):
    eg = self.factory.createExternalGraphic(self.url, self.format)
    g = util.graphic(sym)
    if g:
      g.graphicalSymbols().add(eg)

  def __repr__(self):
    return self._repr('url', 'format')
