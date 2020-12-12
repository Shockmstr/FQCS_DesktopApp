import unittest

from FQCS import detector, helper
import os
import shutil
import cv2

TEMP_PATH = "test\\tmp"
IMGPATH = "test\\data_test\\1.png"

class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.config = [detector.default_detector_config()] 
        os.mkdir(os.path.join(os.getcwd(), TEMP_PATH))
        return

    def tearDown(self):
        shutil.rmtree(os.path.join(os.getcwd(), TEMP_PATH), ignore_errors=True)

    def test_save_json_config(self):
        detector.save_json_cfg(self.config, os.path.join(os.getcwd(), TEMP_PATH))
        result = os.path.isdir(os.path.join(os.getcwd(), TEMP_PATH))
        self.assertEqual(result, True)

    def test_load_json_config(self):
        detector.save_json_cfg(self.config, os.path.join(os.getcwd(), TEMP_PATH))
        result = detector.load_json_cfg(os.path.join(os.getcwd(), TEMP_PATH))
        self.assertEqual(result[0]["name"], self.config[0]["name"])

    def test_calculate_length_per10px(self):
        result = helper.calculate_length_per10px(100, 2000)
        self.assertEqual(result, float(200))

    def test_calculate_length(self):
        result = helper.calculate_length(100, 1)
        self.assertEqual(result, float(10))

    def test_midpoint(self):
        result = helper.midpoint((1, 2), (3, 4))
        self.assertEqual(result, (2.0, 3.0))
    
    def test_find_contours_using_thresh(self):
        img = cv2.imread(os.path.join(os.getcwd(), IMGPATH))
        cnts, _, _ = detector.find_contours_using_thresh(img, self.config[0]["d_cfg"])
        self.assertGreater(len(cnts), 0)

    def test_find_contours_using_edge(self):
        img = cv2.imread(os.path.join(os.getcwd(), IMGPATH))
        cnts, _, _ = detector.find_contours_using_edge(img, self.config[0]["d_cfg"])
        self.assertGreater(len(cnts), 0)

    def test_find_contours_using_range(self):
        img = cv2.imread(os.path.join(os.getcwd(), IMGPATH))
        cnts, _, _ = detector.find_contours_using_range(img, self.config[0]["d_cfg"])
        self.assertGreater(len(cnts), 0)    
    
    def test_get_PSNR(self):
        img1 = cv2.imread(os.path.join(os.getcwd(), IMGPATH))
        img2 = img1.copy()
        result = helper.getPSNR(img1, img2)
        self.assertEqual(result, 0)

    def test_getMSSISM(self):
        img1 = cv2.imread(os.path.join(os.getcwd(), IMGPATH))
        img2 = img1.copy()
        result = helper.getMSSISM(img1, img2, 1 , 1)
        self.assertEqual(result, (1.0, 1.0, 1.0, 0.0))

    def test_diff_image(self):
        img1 = cv2.imread(os.path.join(os.getcwd(), IMGPATH))
        img2 = img1.copy()
        img2[img2 != 0] = 255
        result = helper.diff_image(img1, img2)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()