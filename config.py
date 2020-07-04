import os


DATA_PATH = 'G:/data/captcha/'
DATA_PATH_TRAIN = os.path.join(DATA_PATH, 'train/')
DATASET_PATH_TEST = os.path.join(DATA_PATH, 'test/')

MODEL_TRAINING = False # start model training



NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            #, \
            #'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

COUNT_IMG_TRAIN = 200000 # number of images for tain
COUNT_IMG_TEST = 5000 # number of images for test

ALL_CHARS = NUMBER + ALPHABET
ALL_CHARS_LEN = len(ALL_CHARS)

NUM_CODE_CHARACTERS = 5

EPOCHS = 200
BATCH_SIZE = 256

IMG_SHAPE = (60, 160, 3)
