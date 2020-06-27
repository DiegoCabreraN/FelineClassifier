import os
import re
import numpy as np

import tensorflow as tf
import tensorflow.keras as K
import tensorflow.keras.preprocessing as Kproc
import tensorflow.keras.applications as Kmodels

tf.config.set_visible_devices([], 'GPU')
visible_devices = tf.config.get_visible_devices()
for device in visible_devices:
    assert device.device_type != 'GPU'

def Model(filepath):

    cat_labels = [
        "tabby", 
        "tiger_cat", 
        "Persian_cat", 
        "Siamese_cat", 
        "Egyptian_cat",
    ]

    feline_labels = [
        "cougar", 
        "lynx", 
        "leopard", 
        "snow_leopard", 
        "jaguar",
        "tiger", 
        "cheetah"
    ]

    model = tf.keras.applications.VGG19()
    image = Kproc.image.load_img(filepath, target_size=(224,224))
    image = Kproc.image.img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = Kmodels.vgg19.preprocess_input(image)
    prediction = model.predict(image)
    label = Kmodels.vgg19.decode_predictions(prediction, top=3)
    detected_object = label[0][0][1]

    if detected_object in cat_labels:
        elem = re.findall(r"\S+(?=_)|\S+",detected_object)
        return elem[0]
    elif detected_object in feline_labels:
        return (detected_object, None)
    return None