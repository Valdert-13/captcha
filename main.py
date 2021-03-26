from model.model import Model
from dataset.dataset import Dataset
from model.models_nn import *
from src.functions import chec_dir, count_img
from model.test_model import Test_model
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

        dict_models = {
            'model_1': model_1(),
            'model_2': model_2(),
            'model_3': model_3()
        }

        train = Dataset(DATA_PATH_TRAIN)
        test = Dataset(DATASET_PATH_TEST)
        model = Model(train.image, train.label, epochs=EPOCHS, models=dict_models)
        model.fit()
        result = Test_model(model.models,test.image, test.label)
        result.test_data()
        n = 0
        best_result = 0
        for i, model in enumerate(result.models):
            print(f'Accuracy of the model: {model["model_name"]} = {model["result"]}')

            if model["result"] > best_result:
                best_result = model["result"]
                n = i

        result.models[n].save(f'{CAPTСHA}_captcha_model.h5')


    else:
        model = tf.keras.models.load_model(f'{CAPTСHA}_captcha_model.h5')
        dict_models = {'model': model }
        test = Dataset(DATASET_PATH_TEST)
        model = Model(models=dict_models)
        result = Test_model(model.models, test.image, test.label)
        result.test_data()
        print(f'Accuracy of the model: {result.models[0]["model_name"]} = {result.models[0]["result"]}')


