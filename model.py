import tensorflow as tf
from config import *
from dataset import get_train_data_loader



def create_model():
    'Создание модели'
    input_img = tf.keras.layers.Input(shape=IMG_SHAPE)
    output_code = []

    out = tf.keras.layers.Convolution2D(16, (3, 3), padding='same', activation='relu')(input_img)
    out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    out = tf.keras.layers.Convolution2D(32, (3, 3), padding='same', activation='relu')(out)
    out = tf.keras.layers.Convolution2D(32, (3, 3), padding='same', activation='relu')(out)
    out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    out = tf.keras.layers.Convolution2D(64, (3, 3), padding='same', activation='relu')(out)
    out = tf.keras.layers.Convolution2D(64, (3, 3), padding='same', activation='relu')(out)
    out = tf.keras.layers.BatchNormalization()(out)
    out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    out = tf.keras.layers.Flatten()(out)


    for _ in range(NUM_CODE_CHARACTERS):
        dense = tf.keras.layers.Dense(64, activation='relu')(out)
        dropout = tf.keras.layers.Dropout(0.4)(dense)
        prediction = tf.keras.layers.Dense(ALL_CHARS_LEN, activation='sigmoid')(dropout)

        output_code.append(prediction)

    model = tf.keras.Model(input_img, output_code)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def training_model (EPOCHS=EPOCHS, BATCH_SIZE=BATCH_SIZE ):
    'Обучение модеои'
    model = create_model()
    image, label  = get_train_data_loader()
    model.fit(image, [label[:, i] for i in range(NUM_CODE_CHARACTERS)], epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=1, validation_split=0.2)
    model.save('captcha_model.h5')
    return model

