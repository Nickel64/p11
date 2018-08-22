import cv2 as cv
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy

from util.classification import Classification

tfnet: TFNet


def start_ai():
    global tfnet
    options = {"model": "../cfg/tiny-yolo-voc-1c.cfg",
               "load": 150,
               "threshold": 0.1}
    tfnet = TFNet(options)


def classify(frame):
    # frame = cv.resize(frame, (1920, 1080))

    results = tfnet.return_predict(frame)
    out = []
    for res in results:
        clf = Classification(res)
        out.append(clf)
        print(clf)
    return out