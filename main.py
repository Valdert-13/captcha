from config import *
from captcha_generator import  Captcha
from model import training_model
from  test import test_data
import tensorflow as tf
import os


def chec_dir(path):
    'Проверка существоваяния директории'
    try:
        if not os.path.isdir(path):
            os.mkdir(path)
            print("Created the directory %s " % path)
    except OSError:
        print ("Creation of the directory %s failed" % path)


def count_img (path, count_img):
    'Подсчет разности требуемых и количества изображения в папке'
    count  = count_img - len(os.listdir(path))
    if count > 0:
        Captcha(path, count)



if __name__ == "__main__":
    if not os.path.isdir(DATA_PATH):
        print ('Пожалуйста укажите сущетсвующий путь. Config.py DATA_PATH = ')
        exit()

    chec_dir(DATASET_PATH_TEST)
    count_img(DATASET_PATH_TEST, COUNT_IMG_TEST)


    if not os.path.isfile('captcha_model.h5') or MODEL_TRAINING:
        if os.path.isfile('captcha_model.h5'):os.remove('captcha_model.h5')
        chec_dir(DATA_PATH_TRAIN)
        count_img(DATA_PATH_TRAIN, COUNT_IMG_TRAIN)
        model = training_model(EPOCHS, BATCH_SIZE)
    else:
        model = tf.keras.models.load_model('captcha_model.h5')

    correct, total = test_data(model)
    print('Test Accuracy of the model on the %d test images: %f %%' % (total, 100 * correct / total))


