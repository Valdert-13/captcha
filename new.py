import os
from config import *
import random
from PIL import Image

download_path = os.path.join(DATA_PATH, 'download/')
train = 'G:/data/captcha/Rosreestr/train/'
list_name = os.listdir(download_path)
for name in list_name:
    try:
        im = Image.open(download_path + name)
        rgb_im = im.convert('RGB')
        rgb_im.save(train + name[0:5] +'_' + str(random.randint(0, 10)) + '_.jpg')
    except:
        pass


