import os
import numpy as np
import time
import ImageProcess.face.FaceUtils as FaceUtils

rootPath = os.path.abspath("D:/PySpace/PyUtils")
dataPath = os.path.join(rootPath, "DataResource/facedata")
modelDirPath = os.path.join(dataPath, "models")
tarFilePath = os.path.join(dataPath, "Albert_Costa_0001.jpg")
imageFilePathList = FaceUtils.getAllImageFiles(os.path.join(dataPath, "pure"))

def loadAlldata():
    imageNumpyArrDict = {}
    for file in imageFilePathList:
        imageNumpyArrDict[file] = FaceUtils.getImageFromFile(file)
    return  imageNumpyArrDict

def extractAllFeatures(imageNumpuArrDict):
    faceFeaturesDict = {}
    for (file, imageArr) in imageNumpuArrDict.items():
        faceFeaturesDict[file] = FaceUtils.extract_faces_feature(imageArr)
    return faceFeaturesDict

def findMostSimilar(targetFeature, faceFeaturesDict):
    _max = 0
    result = ""
    for (file, feature) in faceFeaturesDict.items():
        distances = FaceUtils.compute_distance_of_features(targetFeature[:1], feature)
        if distances is not None:
            sim = 1 - distances.min()
            if sim > _max:
                _max = sim
                result = file
    return result




def main():
    time0 = time.time()
    imageNumpyArrayDict = loadAlldata()
    time1 = time.time()
    faceFeaturesDict = extractAllFeatures(imageNumpyArrayDict)
    # np.save("./feature.npy", faceFeaturesDict)
    # faceFeaturesDict = np.load("./feature.npy").item()
    time2 = time.time()
    targetFeature = FaceUtils.extract_faces_feature(FaceUtils.getImageFromFile(tarFilePath))
    time3 = time.time()
    result = findMostSimilar(targetFeature, faceFeaturesDict)
    time4= time.time()
    print(result)
    print("load data: ", str(time1 - time0))
    print("extraction: ", str(time2 - time1))
    print("extract target: ", str(time3-time2))
    print("find most similar: ", str(time4 - time3))
    print("total: ", str(time4 - time0))


if __name__ == '__main__':
    main()