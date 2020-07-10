# What is the capthca
Captcha is image  generated by chars randomly and proper voice to avoid the attack from the robot.   
![1STSD_4](https://github.com/Valdert-13/captcha/blob/master/picture/1STSD_4_.jpg)    
The picture above is a common captcha,including five capital letters of the alphabet and digital numbers.  
#How to recognize the captcha
There three main methods:
> * find the loopholes of the captcha
> * spilt the captcha into single char, and then recognize the chars
> * regard the captha as the whole, and recognzie it directly   

Tesseract OCR and OpenCV use the second method. But the captcha is more and more complex now. There is a common phenomenon that the chars in the captcha interlace with one another, so the second method gets a low accuracy. This program focuses on the third method. 

# Generate the captcha to train
Acquire massive capthca by hunman is unrealistic. Fortunately, we can easily generate the captcha by the python package **captcha**.See the [captcha_generator.py](https://github.com/Valdert-13/captcha/blob/master/captcha_generator.py) in details.

# Build the cnn model
I build the network with [TensorFlow](https://github.com/tensorflow/tensorflow).
```python
# 3 conv layer
    input_img = tf.keras.layers.Input(shape=IMG_SHAPE)
    output_code = []

    out = tf.keras.layers.Convolution2D(16, (3, 3), padding='same', activation='relu')(input_img)
    out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    out = tf.keras.layers.Convolution2D(32, (3, 3), padding='same', activation='relu')(out)
    out = tf.keras.layers.Convolution2D(32, (3, 3), padding='same', activation='relu')(out)
    out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    out = tf.keras.layers.Convolution2D(64, (3, 3), padding='same', activation='relu')(out)
    out = tf.keras.layers.Convolution2D(64, (3, 3), padding='same', activation='relu')(out)
    out = tf.keras.layers.BatchNormalization()(out)
    out = tf.keras.layers.MaxPooling2D(padding='same')(out)
    out = tf.keras.layers.Flatten()(out)


    for _ in range(NUM_CODE_CHARACTERS):
        dense = tf.keras.layers.Dense(64, activation='relu')(out)
        dropout = tf.keras.layers.Dropout(0.4)(dense)
        prediction = tf.keras.layers.Dense(ALL_CHARS_LEN, activation='sigmoid')(dropout)

        output_code.append(prediction)
```

# The training result    
I use 100 000 training samples and 5 000 test samples. After 150 epochs of training, the model obtains the correct rate of 75.62% on the test data.  


![1RF0L](https://github.com/Valdert-13/captcha/blob/master/picture/1RF0L_0_.jpg)    
![0F6KK](https://github.com/Valdert-13/captcha/blob/master/picture/0F6KK_8_.jpg)   



