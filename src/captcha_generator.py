from captcha.image import ImageCaptcha
from PIL import Image
import random
import time
from config import *


class Captcha ():
    """
    Класс создания изображений python captcha в указанной директории

    Parameters
    ----------
    data_path: str
        путь директории

    count_img: int
        Количиство образцов изображений
    """

    def __init__(self, data_path:str, count_img:int):
        self.path = data_path
        self.count_img = count_img
        self._creature_captcha_img()


    def _random_captcha(self):
        'Создание набора рандомных сиволов из "ALL_CHARS" и длинной "NUM_CODE_CHARACTERS"'
        captcha_text = []
        for i in range(NUM_CODE_CHARACTERS):
            c = random.choice(ALL_CHARS)
            captcha_text.append(c)
        return ''.join(captcha_text)


    def _gen_captcha_text_and_image(self):
        'Создания излбражения на основани сгенирированых символов'
        image = ImageCaptcha()
        captcha_text = self._random_captcha()
        captcha_image = Image.open(image.generate(captcha_text))
        return captcha_text, captcha_image


    def _creature_captcha_img (self):
        'Сохранение сгенерированых изображений с кодом в имени файла'
        star = time.time()
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        for i in range(self.count_img):
            text, image = self._gen_captcha_text_and_image()
            filename = text + '_' + str(random.randint(0, 10)) +'_' +'.jpg'
            image.save(self.path + os.path.sep + filename)

        end = time.time()
        print('The generation time was', int(end-star), 'sec')





