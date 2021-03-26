import tensorflow as tf
from config import *

def model_1():
    'Иницилизация структуры модели'
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


def model_2():
    'Иницилизация структуры модели'
    input_img = tf.keras.layers.Input(shape=IMG_SHAPE)
    output_code = []

    out = tf.keras.layers.Convolution2D(16, (3, 3), padding='same', activation='relu')(input_img)
    out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    out = tf.keras.layers.Convolution2D(32, (3, 3), padding='same', activation='relu')(out)
    out = tf.keras.layers.Convolution2D(32, (3, 3), padding='same', activation='relu')(out)
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


def model_3():
    'Иницилизация структуры модели'
    input_img = tf.keras.layers.Input(shape=IMG_SHAPE)
    output_code = []

    out = tf.keras.layers.Convolution2D(16, (3, 3), padding='same', activation='relu')(input_img)
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