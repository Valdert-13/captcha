from config import *
from model import training_model
from functions import chec_dir, count_img
from test_model import test_data
import tensorflow as tf
import os

if __name__ == "__main__":
    if not os.path.isdir(DATA_PATH):
        print ('Пожалуйста укажите сущетсвующий путь. Config.py DATA_PATH = ')
        exit()

    assert CAPTСHA in list_captcha, 'Пожалуйста укажите наименование каптчи принадлежащего списку list_captcha в config.py'


    chec_dir(DATASET_PATH_TEST)
    count_img(DATASET_PATH_TEST, COUNT_IMG_TEST)


    if not os.path.isfile(f'{CAPTСHA}_captcha_model.h5') or MODEL_TRAINING:
        if os.path.isfile(f'{CAPTСHA}_captcha_model.h5'):os.remove(f'{CAPTСHA}_captcha_model.h5')
        chec_dir(DATA_PATH_TRAIN)
        count_img(DATA_PATH_TRAIN, COUNT_IMG_TRAIN)
        model = training_model(EPOCHS, BATCH_SIZE)
    else:
        model = tf.keras.models.load_model(f'{CAPTСHA}_captcha_model.h5')

    correct, total = test_data(model)
    print('Test Accuracy of the model on the %d test images: %f %%' % (total, 100 * correct / total))


