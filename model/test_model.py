from config import *
import numpy as np


class Test_model():
    """
    Class builds container with predictive models based

    Parameters
    ----------

    train: tf.data.Datasets
        Тренировочный, предобработатнный датасет

    """

    def __init__(self,
                 models:list=[],
                 image=None,
                 label=None,):
        self.models = models
        self.image = image
        self.label = label



    def _tensor_to_chars(self, tensor):
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


    def test_data(self):
        'Тестирование моделей на тестовой выборке'
        for model in self.models:
            correct = 0
            total = 0
            predicted_code = np.array(model['model_class'].predict(self.image))
            predicted_code = np.transpose(predicted_code, (1, 0, 2))
            label_pred = self._tensor_to_chars(predicted_code)
            labels = self._tensor_to_chars (self.label)
            total += len(labels)
            correct += len([i for i, j in zip(labels, label_pred) if i == j])
            model['result'] = correct / total


        return self.models




