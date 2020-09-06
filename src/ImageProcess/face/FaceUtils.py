import os
import dlib
import numpy as np
import cv2
from PIL import Image
import time

rootPath = os.path.abspath("D:/PySpace/PyUtils")
dataPath = os.path.join(rootPath, "DataResource/facedata")
modelDirPath = os.path.join(dataPath, "models")

# # 使用传统的HOG特征+级联分类的方法 进行人脸识别
detector = dlib.get_frontal_face_detector()

sp = dlib.shape_predictor(os.path.join(
    modelDirPath, "shape_predictor_68_face_landmarks.dat"))
face_rec = dlib.face_recognition_model_v1(os.path.join(
    modelDirPath, "dlib_face_recognition_resnet_model_v1.dat"))


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
    """
    识别出图片中所有的人脸并抽取出128维的特征数据
    """
    data = []
    if img.shape[0] * img.shape[1] > 500000:  # 图像太大，进行压缩
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    # 检测人脸，抽取特征数据
    dets = detector(img, 1)
    for k, d in enumerate(dets):
        rec = dlib.rectangle(d.left(), d.top(), d.right(), d.bottom())
        shape = sp(img, rec)  # 获取landmark
        # 使用resNet获取128维的人脸特征向量
        face_descriptor = face_rec.compute_face_descriptor(img, shape)
        data.append(face_descriptor)
    return np.array(data)


def compute_distance_of_features(features1: np.array, features2: np.array):
    if features1.shape[-1] != features2.shape[-1] or features1.shape[0] == 0:
        return None
    temp = features1 - features2
    e = np.linalg.norm(temp, axis=1)
    return e


def compute_face_similarity(req_array1, req_array2) -> []:
    """计算图片中的人脸相似度: 返回列表存储的(m,n)矩阵，m-req_file1的人脸数,n-req_file2的人脸数"""
    img1_array = req_array1
    img2_array = req_array2

    img1_faces = extract_faces_feature(img1_array)
    img2_faces = extract_faces_feature(img2_array)
    if len(img1_faces) == 0 or len(img2_faces) == 0:
        return []
    sim_list = []
    for f in img1_faces:
        distances1 = compute_distance_of_features(f, img2_faces)
        sims = 1 - distances1
        sim_list.append(sims.tolist())
    return sim_list


def is_face_in_photo(face_req_file, photo_req_file) -> bool:
    """判断<face_req_file>图片中的人脸是否在<photo_req_file>图片中:
        如果存在相似度大于0.5 的，则认为是同一个人脸
    """
    time0 = time.time()
    face_img_array = getImageFromFile(face_req_file)
    photo_img_array = getImageFromFile(photo_req_file)
    time1 = time.time()
    faces = extract_faces_feature(face_img_array)
    photo_faces = extract_faces_feature(photo_img_array)
    time2 = time.time()
    if len(faces) == 0 or len(photo_faces) == 0:
        return False
    distances = compute_distance_of_features(faces[:1], photo_faces)
    similarities = 1 - distances
    sim = max(similarities)
    time3 = time.time()

    print("load image: ", str(time1-time0))
    print("extraction: ", str(time2-time1))
    print("comparison: ", str(time3-time2))
    if sim > 0.5:
        return True
    else:
        return False

def getAllImageFiles(path):
    pathList = []
    for i in os.listdir(path):
        pathList.append(os.path.join(path, i))
    return pathList
