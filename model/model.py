from tensorflow.keras.callbacks import TensorBoard
from config import *
import time
import datetime


class Model():
    """
    Class builds container with predictive models based

    Parameters
    ----------

    train: tf.data.Datasets
        Тренировочный, предобработатнный датасет
    valid: tf.data.Datasets
        Валидационный, предобработатнный датасет
    test: tf.data.Datasets
        Тестовый, предобработатнный датасет
    epochs: int
        число эпох
    models: dict
        словарь с можелями {'имя': модель}


    """

    def __init__(self,
                 image=None,
                 label=None,
                 epochs: int = 1,
                 models: dict = {}):

        # Vertion of model
        self.version = '1'

        self.image = image
        self.label = label
        self.epochs = epochs
        self.models = []

        for model in models.keys():
            self.models.append({'model_name': model,
                                'model_class': models[model],
                                'history': None,
                                'result':None
                                })

    # Models training
    def fit(self):

        """
        Обучение моделей

        """

        for model in self.models:
            now_str = lambda: datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Запуск обучение модели {model['model_name']}", now_str())

            tensorboard_callback = TensorBoard(
                log_dir='logs/' + model['model_name'],
                write_graph=False, update_freq=100, profile_batch=0)

            start_time = time.time()

            model['history'] = model['model_class'].fit(self.image,
                                                        [self.label[:, i] for i in range(NUM_CODE_CHARACTERS)],
                                                        epochs=self.epochs,
                                                        callbacks=[tensorboard_callback]
                                                        )

            model['time_fit'] = time.time() - start_time

        # Cleaning memory
        self.train = None
        self.valid = None




    # def model(self):
    #     'Создание модели'
    #     input_img = tf.keras.layers.Input(shape=IMG_SHAPE)
    #     output_code = []
    #
    #     out = tf.keras.layers.Convolution2D(16, (3, 3), padding='same', activation='relu')(input_img)
    #     out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    #     out = tf.keras.layers.Convolution2D(32, (3, 3), padding='same', activation='relu')(out)
    #     out = tf.keras.layers.Convolution2D(32, (3, 3), padding='same', activation='relu')(out)
    #     out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    #     out = tf.keras.layers.Convolution2D(64, (3, 3), padding='same', activation='relu')(out)
    #     out = tf.keras.layers.Convolution2D(64, (3, 3), padding='same', activation='relu')(out)
    #     out = tf.keras.layers.BatchNormalization()(out)
    #     out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    #     out = tf.keras.layers.Flatten()(out)
    #
    #
    #     for _ in range(NUM_CODE_CHARACTERS):
    #         dense = tf.keras.layers.Dense(64, activation='relu')(out)
    #         dropout = tf.keras.layers.Dropout(0.4)(dense)
    #         prediction = tf.keras.layers.Dense(ALL_CHARS_LEN, activation='sigmoid')(dropout)
    #
    #         output_code.append(prediction)
    #
    #     model = tf.keras.Model(input_img, output_code)
    #     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    #     return model

    # def fit (self):
    #     'Обучение модеои'
    #     model = create_model()
    #     image, label  = get_train_data_loader()
    #     model.fit(image, [label[:, i] for i in range(NUM_CODE_CHARACTERS)], epochs=self.epochs,
    #               batch_size=self.batch, verbose=1, validation_split=0.2)
    #     model.save(f'{CAPTСHA}_captcha_model.h5')
    #     return model

