import urllib.parse

from app.other import LoggerFactory


class SimpleImgBuilder:
    ENDPOINT = 'https://maps.googleapis.com/maps/api/staticmap?'
    KEY = '<You-Key>'

    def __init__(self) -> None:
        self.vars = {}
        self.__set_key(self.KEY)

    def __set_key(self, val):
        self.vars.update(key=val)
        return self

    def set_center(self, lat, lon):
        self.vars.update(center='{},{}'.format(lat, lon))
        return self

    def set_zoom(self, val):
        self.vars.update(zoom=val)
        return self

    def set_size(self, w, h):
        self.vars.update(
            size='{}x{}'.format(w, h))
        return self

    def set_scale(self, val):
        self.vars.update(scale=val)
        return self

    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items()))

    def build(self):
        return self.ENDPOINT + urllib\
            .parse.urlencode(self.vars)


class PolylinesImgBuilder(SimpleImgBuilder):

    def __init__(self, weight, color, enc) -> None:
        super().__init__()

        str_path = 'weight:{}|color:{}|enc:{}'\
            .format(weight, color, enc)
        self.vars.update(path=str_path)



