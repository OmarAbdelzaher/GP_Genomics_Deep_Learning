import numpy as np
import cv2
import os
from PIL import Image,ImageOps 
# from io import BytesIO
# from django.core.files.base import ContentFile


from tensorflow import keras

model_not_asian = keras.models.load_model("./not_asian")   # Loading the Deep Learning Model of Not Asian Data
model_asian = keras.models.load_model("./asian")           # Loading the Deep Learning Model of Asian Data

def down_syndrom_classification(imgs,nationality):
    first_img = imgs[0]
    im_pic = Image.open(first_img)
    cv_img = np.array(im_pic)
    img = cv_img
    # print(cv_img)
    cv2.imwrite("NewImage.png",cv_img)
    categories = ["Down", "Normal"]

    # Check for the used model before prediction : "Asian = Chinese" "Any other nationality = Not Asian"
    if(nationality == "Chinese"):
        new_img = cv2.resize(img,(224,224))
        new_img = new_img.reshape(1,new_img.shape[0],new_img.shape[1],new_img.shape[2])
        pred = model_asian.predict_generator(new_img, verbose = 1)
        pred = np.argmax(pred, axis = 1)
        pred_out = categories[pred[0]]
    else:
        new_img = cv2.resize(img,(32,32))
        new_img = new_img.reshape(1,new_img.shape[0],new_img.shape[1],new_img.shape[2])
        pred = model_not_asian.predict_generator(new_img, verbose = 1)
        pred = np.argmax(pred, axis = 1)
        pred_out = categories[pred[0]]
    return (pred_out)



       