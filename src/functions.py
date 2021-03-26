from config import *
from src.rosreestr import download_cuptcha_rosreestr, rename_captcha
from src.captcha_generator import Captcha
import shutil


def chec_dir(path:str):
    'Проверка существоваяния директории'
    try:
        if not os.path.isdir(path):
            os.mkdir(path)
            print("Created the directory %s " % path)
    except OSError:
        print ("Creation of the directory %s failed" % path)


def count_img (path:str, count_img:int):
    'Подсчет разности требуемых и количества изображения в папке'
    count  = count_img - len(os.listdir(path))
    if count > 0:
        if CAPTСHA == 'python':
            Captcha(path, count)

        elif CAPTСHA == 'rosreestr':
            chec_dir(download_path)
            download_cuptcha_rosreestr(path, count)
            rename_captcha(path)
            for filename in os.listdir(download_path):
                file_path = os.path.join(download_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))






