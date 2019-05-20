import urllib.parse
from enum import Enum

from app.BuilderMapImg import SimpleImgBuilder
from app.other import LoggerFactory


class DirectionBuilder:
    ENDPOINT = 'https://maps.googleapis.com/maps/api/directions/json?'
    KEY = SimpleImgBuilder.KEY

    class Mode(Enum):
        walking = 1

    def __init__(self) -> None:
        self.vars = {}
        self.__set_key(self.KEY)
        self.__set_lang('en')

    def __set_key(self, val):
        self.vars.update(key=val)
        return self

    def __set_lang(self, val):
        self.vars.update(language=val)
        return self

    def set_origin(self, loc):
        self.vars.update(origin='{},{}'.format(loc[0], loc[1]))
        return self

    def set_destination(self, loc):
        self.vars.update(destination='{},{}'
                         .format(loc[0], loc[1]))
        return self

    def set_mode(self, val):
        self.vars.update(mode=val.name)
        return self

    def set_waypoints(self, points):
        str_points = ''
        for p in points:
            str_points += \
                'via:{},{}|'.format(p[0], p[1])

        self.vars.update(waypoints=str_points)
        return self

    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items()))

    def build(self):
        return self.ENDPOINT + urllib \
            .parse.urlencode(self.vars)




