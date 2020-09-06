import os
import sys
import time
import ImageProcess.face.FaceUtils as FaceUtils

rootPath = os.path.abspath("D:/PySpace/PyUtils")
dataPath = os.path.join(rootPath, "DataResource/facedata")
modelDirPath = os.path.join(dataPath, "models")
tarFilePath = os.path.join(dataPath, "Albert_Costa_0001.jpg")
imageFilePathList = FaceUtils.getAllImageFiles(os.path.join(dataPath, "pure"))

def loadAlldata():
    imageNumpyArrList = []
    for file in imageFilePathList:
        imageNumpyArrList.append(FaceUtils.getImageFromFile(file))
    return  imageNumpyArrList

def main():
    time0 = time.time()
    loadAlldata()
    time1 = time.time()
    print(time1 - time0)

if __name__ == '__main__':
    main()