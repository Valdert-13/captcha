from config import *
import pytest
import os

@pytest.mark.config
def test_path_data():
    assert os.path.exists(DATA_PATH) == True,'the test failed, the path does not exist'

@pytest.mark.config
def test_var():
    list_variables = [COUNT_IMG_TRAIN, COUNT_IMG_TEST, NUM_CODE_CHARACTERS, EPOCHS, BATCH_SIZE]
    for var in list_variables:
        assert type(var) is int and var > 0,f'the test failed, {var} not a type of int or <= 0'

    assert len(IMG_SHAPE) == 3 and (i > 0 for i in IMG_SHAPE), 'the test failed, size "IMG_SHAPE" should be 3 positive values'

    assert len(ALL_CHARS) > 0,  'the test failed, "ALL_CHARS" must be greater than 0'

    assert type(MODEL_TRAINING) is bool