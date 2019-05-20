import unittest

import cv2
import imutils

from app import BuilderMapImg
from app.tests.Stubs import SImg


class ImageBuilderTest(unittest.TestCase):

    def test_builder_vars(self):
        sample = SImg.get_sample_img_builder()

        self.assertEqual(float(
            sample.vars.get('center')
                .split(",")[0]), SImg.LOC[0])

        self.assertEqual(float(
            sample.vars.get('zoom')), SImg.ZOOM)

        self.assertEqual(int(
            sample.vars.get('size')
                .split("x")[0]), SImg.SIZE[0])

        self.assertEqual(int(
            sample.vars.get('scale')), SImg.SCALE)

    def test_builder_image(self):
        image = imutils.url_to_image(
            SImg.get_sample_img_builder().build())
        self.assertIsNotNone(image)

        cv2.imshow('Image', image)
        cv2.waitKey(delay=2000)


if __name__ == '__main__':
    unittest.main()



