import unittest

import cv2
import imutils
import numpy as np

from app.other import Navigation, LoggerFactory
from app.other.Navigation import get_image_changes_per_px
from app.tests.Stubs import SImg, get_random_shape_points


class NavigationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = LoggerFactory.get_logger()

    def test_image_bounds(self):
        bounds = Navigation.get_static_map_bounds(
            SImg.LOC[0], SImg.LOC[1], SImg.ZOOM,
            SImg.SIZE[0], SImg.SIZE[1])

        self.assertIsNotNone(bounds)
        self.assertEqual(len(bounds), 2)
        return bounds

    def test_changes_per_px(self):
        bounds = Navigation.get_static_map_bounds(
            SImg.LOC[0], SImg.LOC[1], SImg.ZOOM,
            SImg.SIZE[0], SImg.SIZE[1])

        dx, dy = get_image_changes_per_px(
            bounds, SImg.SIZE[0], SImg.SIZE[1])

        l_b = bounds[0]
        r_t = bounds[1]
        self.assertEqual((l_b[1] + (
                SImg.SIZE[0] * dx)), r_t[1])

        self.assertEqual((l_b[0] + (
                SImg.SIZE[1] * dy)), r_t[0])

    def test_image_bounds_in_middle(self):
        bounds = Navigation.get_static_map_bounds(
            SImg.LOC[0], SImg.LOC[1], SImg.ZOOM,
            SImg.SIZE[0], SImg.SIZE[1])
        self.logger.info('Working Image Bounds: {}'
                         .format(bounds))

        img_middle = int(SImg.SIZE[0] / 2)
        location = Navigation.get_image_points_location(
            bounds, SImg.SIZE[0], SImg.SIZE[1], [(img_middle, img_middle)])

        self.assertIsNotNone(location)
        self.logger.info(
            'Received Image Center Location: {} Should be close to: {}'
                .format(location, SImg.LOC))

        self.assertEqual(round(
            location[0][0], 5), round(float(SImg.LOC[0]), 5))
        self.assertEqual(round(
            location[0][1], 5), round(float(SImg.LOC[1]), 5))

    def test_image_bounds_locations(self):
        points = np.array([(320, 300), (320, 340)])
        self.logger.info("Generated Random Points:\n{}"
                         .format(points))

        bounds = Navigation.get_static_map_bounds(
            SImg.LOC[0], SImg.LOC[1], SImg.ZOOM,
            SImg.SIZE[0], SImg.SIZE[1])
        self.assertIsNotNone(bounds)
        self.logger.info("Current Img Loc Bounds:\n{}"
                         .format(str(bounds)))

        locations = Navigation.get_image_points_location(
            bounds, SImg.SIZE[0], SImg.SIZE[1], points)
        self.assertIsNotNone(locations)
        self.logger.info("Build Points Locations:\n{}"
                         .format(str(locations)))

        for loc in locations:
            l_b = bounds[0]
            r_t = bounds[1]
            self.assertTrue(r_t[0] >= loc[0] >= l_b[0])
            self.assertTrue(r_t[1] >= loc[1] >= l_b[1])

    def test_random_points_creation(self):
        img_builder = SImg.get_sample_img_builder()
        self.assertIsNotNone(img_builder)

        points = get_random_shape_points(
            SImg.SIZE[0], SImg.SIZE[1], edges=2)
        self.assertIsNotNone(points)
        self.assertEqual(len(points), 2)

        img_sample = imutils.url_to_image(img_builder.build())
        self.assertIsNotNone(img_sample)


if __name__ == '__main__':
    unittest.main()





