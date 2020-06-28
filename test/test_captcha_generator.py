from config import *
import pytest
from captcha_generator import *


@pytest.mark.Captcha
def test_random_captcha():
    data_path = DATASET_PATH_TEST
    assert os.path.exists(data_path) == True,'the test failed, the DATASET_PATH_TEST does not exist'
    count_img = COUNT_IMG_TEST
    assert type(count_img) is int and count_img > 0, f'the test failed, "COUNT_IMG_TEST" not a type of int or <= 0'