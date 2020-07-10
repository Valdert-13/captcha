from config import *
from captcha_generator import Captcha
from model import training_model
from test_model import test_data
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
        if CAPTСHA == 'python':
            Captcha(path, count)

        elif CAPTСHA == 'rosreestr':
            print('Запустите модуль rosreestr.py переименуте капxу (пример: 12345_09_.jpg) согласно изображению на картике или скачайте по ссылке')
            exit()




if __name__ == "__main__":
    if not os.path.isdir(DATA_PATH):
        print ('Пожалуйста укажите сущетсвующий путь. Config.py DATA_PATH = ')
        exit()

    assert CAPTСHA in list_captcha, 'Пожалуйста укажите наименование капчи принадлежащего списку list_captcha в config.py'


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


