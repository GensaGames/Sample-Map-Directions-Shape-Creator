import cv2
import imutils
import numpy as np
import requests

from app import BuilderMapImg
from app.other import LoggerFactory, Navigation


# noinspection PyMethodMayBeStatic
from app.other.Helper import get_enc_polylines
from app.tests.Stubs import SImg, SDirct, get_random_shape_points


class SampleWorker:

    def __init__(self):
        self.logger = LoggerFactory.get_logger()

    def test_requested_location_with_points(self):
        points = get_random_shape_points(SImg.SIZE[0], SImg.SIZE[1], 5)
        self.logger.info("Generated Random Points:\n{}"
                         .format(points))

        bounds = Navigation.get_static_map_bounds(
            SImg.LOC[0], SImg.LOC[1], SImg.ZOOM,
            SImg.SIZE[0], SImg.SIZE[1])

        self.logger.info("Current Img Loc Bounds:\n{}"
                         .format(str(bounds)))

        locations = Navigation.get_image_points_location(
            bounds, SImg.SIZE[0], SImg.SIZE[1], points)

        self.logger.info("Build Points Locations:\n{}"
                         .format(str(locations)))

        new_builder = SDirct.get_simple_direction_builder()
        new_builder.set_origin(locations[0])
        new_builder.set_destination(locations[0])
        new_builder.set_waypoints(locations)
        self.logger.info('Working with Direction Url:\n{}'
                         .format(new_builder.build()))

        response = requests.get(new_builder.build())
        enc = get_enc_polylines(response)

        img_dirct = imutils.url_to_image(
            SImg.get_sample_img_path_builder(enc).build())
        self.show_built_images(points, img_dirct)

    @staticmethod
    def show_built_images(points, img_dirct):
        img_builder = SImg.get_sample_img_builder()
        img_sample = imutils.url_to_image(img_builder.build())

        cv2.polylines(
            img_sample, [points.reshape((-1, 1, 2))],
            True, (0, 0, 255), thickness=5)

        cv2.imshow("ImageSample", img_sample)
        cv2.imshow('ImageDirections', img_dirct)
        cv2.waitKey(delay=86000)


if __name__ == '__main__':
    SampleWorker()\
        .test_requested_location_with_points()


