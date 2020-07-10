import os
import numpy as np
from PIL import Image
from config import *

class Dataset():
    def __init__(self, data_path):
        'Создание датасета из изображений по выбраному пути'
        self.data_path = data_path


    def creat_dataset (self, data_path):
        img_list = os.listdir(data_path)
        len_img_list = len(img_list)

        X = np.zeros((len_img_list, *IMG_SHAPE))
        Y = np.zeros((len_img_list , NUM_CODE_CHARACTERS, ALL_CHARS_LEN))

        for i, img_name in enumerate(img_list):

            img = Image.open(os.path.join(data_path, img_name))
            img = np.array(img)
            img = img / 255.0
            img = np.reshape(img, IMG_SHAPE)
            one_hot_target = np.zeros((NUM_CODE_CHARACTERS, ALL_CHARS_LEN))

            for j, char in enumerate(img_name.split('_')[0]):
                index = ALL_CHARS.index(char)
                one_hot_target[j, index] = 1

            X[i] = img
            Y[i] = one_hot_target

        return X, Y

def get_train_data_loader():
    "Создание тренировочного датасета"
    ds = Dataset(DATA_PATH_TRAIN)
    image, label = ds.creat_dataset(DATA_PATH_TRAIN)
    return image, label

def get_test_data_loader():
    'Создание тестового датасета'
    ds = Dataset(DATASET_PATH_TEST)
    image, label = ds.creat_dataset(DATASET_PATH_TEST)
    return image, label


