from config import *
import numpy as np
from dataset import get_test_data_loader



def tensor_to_chars(tensor):
    'Преоброзование тензора в символьную строку'
    label_pred = []
    for i in  tensor:
        indexes = []
        for char_vector in i:
            indexes.append(np.argmax(char_vector))
        label_pred.append(indexes)

    for j, indexes in enumerate(label_pred):
        code = ''
        for i in indexes:
            code += ALL_CHARS[i]

        label_pred[j] = code

    return label_pred


def test_data(model):
    'Тестирование модели на тестовой выборке'
    correct = 0
    total = 0
    image, label_tensor = get_test_data_loader()
    predicted_code = np.array(model.predict(image))
    predicted_code = np.transpose(predicted_code, (1, 0, 2))
    label_pred = tensor_to_chars(predicted_code)
    labels = tensor_to_chars (label_tensor)
    total += len(labels)
    correct += len([i for i, j in zip(labels, label_pred) if i == j])


    return correct, total




