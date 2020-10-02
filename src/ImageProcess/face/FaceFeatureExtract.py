import os
import dlib
from PIL import Image
import numpy as np
import cv2

confFilePath = "./conf.conf"
confDict = {}

def init(confDict):
    with open(confFilePath, "r", encoding='utf-8') as conf:
        for line in conf:
            (key, value) = line.replace(" ", "").replace("\n", "").split("=")
            confDict[key] = value


def getImageFromFile(filePath, mode="RGB")->"numpy.array or None":
    try:
        im = Image.open(filePath)
        if mode:
            im = im.convert(mode)
        return np.array(im)
    except Exception as err:
        print(err)

    return None

def extract_faces_feature(img: np.array) -> np.array:

    data = []
    if img.shape[0] * img.shape[1] > 500000:
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    dets = detector(img, 1)
    for k, d in enumerate(dets):
        rec = dlib.rectangle(d.left(), d.top(), d.right(), d.bottom())
        shape = sp(img, rec)
        face_descriptor = face_rec.compute_face_descriptor(img, shape)
        data.append(face_descriptor)
    return np.array(data)

if __name__ == '__main__':
    init(confDict)
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(os.path.join(
        confDict['modelDirPath'], "shape_predictor_68_face_landmarks.dat"))
    face_rec = dlib.face_recognition_model_v1(os.path.join(
        confDict['modelDirPath'], "dlib_face_recognition_resnet_model_v1.dat"))

