from captcha.image import ImageCaptcha
from PIL import Image
import random
import time
from config import *


class Captcha ():
    def __init__(self, data_path, count_img):
        'Создание изображений с капчей'
        self.path = data_path
        self.count_img = count_img

        def random_captcha():
            'Создание набора рандомных сиволов из "ALL_CHARS" и длинной "NUM_CODE_CHARACTERS"'
            captcha_text = []
            for i in range(NUM_CODE_CHARACTERS):
                c = random.choice(ALL_CHARS)
                captcha_text.append(c)
            return ''.join(captcha_text)

        def gen_captcha_text_and_image():
            'Создания излбражения на основани сгенирированых символов'
            image = ImageCaptcha()
            captcha_text = random_captcha()
            captcha_image = Image.open(image.generate(captcha_text))
            return captcha_text, captcha_image


        def creature_captcha_img (path):
            'Сохранение сгенерированых изображений с кодом в имени файла'
            star = time.time()
            if not os.path.exists(path):
                os.makedirs(path)

            for i in range(count_img):
                text, image = gen_captcha_text_and_image()
                filename = text + '_' + str(random.randint(0, 10)) +'_' +'.jpg'
                image.save(path + os.path.sep + filename)

            end = time.time()
            print('The generation time was', int(end-star), 'sec')

        creature_captcha_img(self.path)



