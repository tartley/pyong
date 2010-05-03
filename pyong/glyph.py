from itertools import chain, repeat

from OpenGL import GL as gl

class Glyph(object):

    def __init__(self, verts, colors, indices):
        colors = tuple(colors)
        assert all(len(vert)==2 for vert in verts)
        assert len(colors[0]) in (3, 4)
        assert all(len(color)==len(colors[0]) for color in colors)
        self.glVerts = self.flatten(verts, gl.GLfloat)
        self.glColors = self.flatten(colors, gl.GLfloat)
        self.glIndices = self.flatten(indices, gl.GLubyte)

    @staticmethod
    def flatten(seq, gltype):
        '''
        Convert a sequence of the form ((a, b, c), (d, e, f)...) into a flat
        contiguous ctypes array (a, b, c, d, e, f...) of the given GLtype.
        '''
        assert all(len(seq[0]) == len(seq[i]) for i in xrange(1, len(seq)))
        return (gltype * (len(seq) * len(seq[0])))(*tuple(chain(*seq)))

    @staticmethod
    def from_item(item):
        return Glyph(
            item.geometry.verts,
            repeat(item.color, len(item.geometry.verts)),
            item.geometry.indices)

