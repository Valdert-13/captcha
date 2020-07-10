import os
from config import *
import random
import numpy as np

train = 'G:/data/captcha/Rosreestr/train/'
test = 'G:/data/captcha/Rosreestr/test/'
list_name = os.listdir(train)
arr = np.array(list_name)
ls = np.random.choice(list_name,size=int(COUNT_IMG_TEST), replace=False)
for name in ls:
    os.rename(train+ name, test + name)

