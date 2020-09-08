from PIL import Image
import os
import numpy as np
import time

def _aHash(image):
    image_new = image
    average = np.mean(image_new)
    hash = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] > average:
                hash.append(1)
            else:
                hash.append(0)
    return hash

def _Hamming_distance(hash1, hash2):
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num

    # image1 = Image.open('./image1.png')
    # image2 = Image.open('./image2.jpg')
def getSimilarity(image1, image2):
    time0 = time.time()
    image1 = np.array(image1.resize((8, 8), Image.ANTIALIAS).convert('L'), 'f')
    image2 = np.array(image2.resize((8, 8), Image.ANTIALIAS).convert('L'), 'f')

    time1 = time.time()
    hash1 = _aHash(image1)
    hash2 = _aHash(image2)

    time2 = time.time()
    dist = _Hamming_distance(hash1, hash2)
    time3 = time.time()

    similarity = 1 - dist * 1.0 / 64

    print("read data: ", time1-time0)
    print("extraction", time2-time1)
    print("distance", time3-time2)
    return similarity

getSimilarity(Image.open("./image1.png"),Image.open("./image2.jpg"))