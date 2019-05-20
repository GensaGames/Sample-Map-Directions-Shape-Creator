import unittest

import cv2
import imutils
import jsonpickle

from app.BuilderMapImg import PolylinesImgBuilder
from app.other import LoggerFactory
import requests

from app.other.Helper import get_enc_polylines
from app.tests.Stubs import SDirct, SImg


class ImageBuilderTest(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = LoggerFactory.get_logger()

    def test_builder_vars(self):
        sample = SDirct.get_simple_direction_builder()
        self.logger.info('Working with Sample:\n{}'
                         .format(sample))

    def test_builder_direction(self):
        sample = SDirct.get_direction_with_path_builder().build()
        self.logger.info('Working with Direction Url:\n{}'
                         .format(sample))

        response = requests.get(sample)
        self.assertEqual(response.status_code, 200)
        self.logger.info('Working Response Code:\n{}'
                         .format(response.status_code))
        return response

    def test_directions_image_shape(self):
        response = self.test_builder_direction()
        enc = get_enc_polylines(response)
        self.assertIsNotNone(enc)

        image = imutils.url_to_image(
            SImg.get_sample_img_path_builder(enc).build())
        self.assertIsNotNone(image)

        cv2.imshow('Image', image)
        cv2.waitKey(delay=2000)


if __name__ == '__main__':
    unittest.main()






