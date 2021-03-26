import os

list_captcha = ['python', 'rosreestr']

CAPTСHA = 'python' # captcha should be on the list_capcha
DATA_PATH = 'G:/data/captcha/'

if CAPTСHA == 'rosreestr':
    DATA_PATH = os.path.join(DATA_PATH, 'rosreestr/')
    download_path = os.path.join(DATA_PATH, 'download/')
    NUMBER = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ALPHABET = []
    IMG_SHAPE = (50, 180, 3)
    NUM_CODE_CHARACTERS = 5

elif CAPTСHA == 'python':
    DATA_PATH = os.path.join(DATA_PATH, 'PyCaptcha/')
    NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # , \
    # 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    IMG_SHAPE = (60, 160, 3)
    NUM_CODE_CHARACTERS = 5

DATA_PATH_TRAIN = os.path.join(DATA_PATH, 'train/')
DATASET_PATH_TEST = os.path.join(DATA_PATH, 'test/')

MODEL_TRAINING = False # start model training


ALL_CHARS = NUMBER + ALPHABET
ALL_CHARS_LEN = len(ALL_CHARS)

COUNT_IMG_TRAIN = 2_000 # number of images for tain
COUNT_IMG_TEST = int(COUNT_IMG_TRAIN * 0.1) # number of images for test


EPOCHS = 60
BATCH_SIZE = 64


