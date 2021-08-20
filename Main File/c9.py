import argparse

import matplotlib.pyplot as plt

from lib.text_detection import TextDetection
from lib.utils import plt_show
from lib.config import Config


class OCR:

    def start_OCR(self, img_file):
        config = Config()
        OUTPUT_FILE = "out.png"
        td = TextDetection(img_file, config, direction='both+', use_tesseract=True, details=False)
        result_string = td.detect()
        return result_string
