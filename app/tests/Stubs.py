from app import BuilderMapImg, BuilderDirection
import numpy as np


class SImg:
    LOC = (40.681660, -73.917258)
    ZOOM = 14
    SIZE = (640, 640)
    SCALE = 1

    @staticmethod
    def get_sample_img_builder():
        return BuilderMapImg.SimpleImgBuilder() \
            .set_center(SImg.LOC[0], SImg.LOC[1]) \
            .set_zoom(SImg.ZOOM) \
            .set_size(SImg.SIZE[0], SImg.SIZE[1]) \
            .set_scale(SImg.SCALE)

    @staticmethod
    def get_sample_img_path_builder(enc):
        return BuilderMapImg.PolylinesImgBuilder(
            weight=5, color='red', enc=enc) \
            .set_center(SImg.LOC[0], SImg.LOC[1]) \
            .set_zoom(SImg.ZOOM) \
            .set_size(SImg.SIZE[0], SImg.SIZE[1]) \
            .set_scale(SImg.SCALE)


class SDirct:
    ORIG = (40.681660, -73.917258)
    DEST = (40.681660, -73.917258)

    WAYP = [[40.70002, -73.89460],
            [40.68817, -73.91803],
            [40.69617, -73.90679],
            [40.68127, -73.90335],
            [40.68934, -73.91056]]

    @staticmethod
    def get_simple_direction_builder():
        return BuilderDirection.DirectionBuilder() \
            .set_origin(SDirct.ORIG) \
            .set_destination(SDirct.DEST) \
            .set_mode(BuilderDirection.DirectionBuilder
                      .Mode.walking)

    @staticmethod
    def get_direction_with_path_builder():
        return BuilderDirection.DirectionBuilder() \
            .set_origin(SDirct.ORIG) \
            .set_destination(SDirct.DEST) \
            .set_waypoints(SDirct.WAYP) \
            .set_mode(BuilderDirection.DirectionBuilder
                      .Mode.walking)


def get_random_shape_points(width, height, edges):

    def deviate_points(size):
        base = int((size / 100) * (100 / edges))
        points = np.linspace(
            base, size - base, edges)

        points = points + np.random.uniform(
            low=-base, high=base, size=(edges,))

        points = np.array(points, dtype=int)
        np.random.shuffle(points)
        return points

    x_p = deviate_points(width)
    y_p = deviate_points(height)
    a = np.array(list((zip(x_p, y_p))))
    return a







