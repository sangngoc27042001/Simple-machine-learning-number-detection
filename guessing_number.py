import pickle
import cv2
import numpy as np

__model1 = None
__model2 = None
__model3 = None
__model4 = None


def return_result(x):
    max = 0;
    for i in range(0, 4):
        count = 0;
        for j in range(0, 4):
            if (x[i] == x[j]):
                count = count + 1
        if count > max:
            max = count
            valuemax = x[i]
    return valuemax


def load_model():
    global __model1
    global __model2
    global __model3
    global __model4

    if __model1 is None:
        with open('predicting_number_file/model_for_predicting_number/model1_guessing_number.pickle', 'rb') as f:
            __model1 = pickle.load(f)

    if __model2 is None:
        with open('predicting_number_file/model_for_predicting_number/model2_guessing_number.pickle', 'rb') as f:
            __model2 = pickle.load(f)

    if __model3 is None:
        with open('predicting_number_file/model_for_predicting_number/model3_guessing_number.pickle', 'rb') as f:
            __model3 = pickle.load(f)

    if __model4 is None:
        with open('predicting_number_file/model_for_predicting_number/model4_guessing_number.pickle', 'rb') as f:
            __model4 = pickle.load(f)
load_model()

def predict_num(data_dir):
    im=cv2.imread(data_dir,cv2.IMREAD_GRAYSCALE)
    im=cv2.resize(im,(8,8))
    im=im/5
    im=im.flatten()
    x=[__model1.predict([im])[0],__model2.predict([im])[0],__model3.predict([im])[0],__model4.predict([im])[0]]
    return return_result(x)

import urllib.request

def download_image_ipg(url, file_path, file_name):
    fullpath=file_path+file_name+".png"
    urllib.request.urlretrieve(url,fullpath)

