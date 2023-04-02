import tensorflow as tf
import cv2
import numpy as np
import os


def data_aug(img):
    data = []
    for i in range(5):
        img = tf.image.stateless_random_brightness(img, max_delta=0.02, seed=(1,2))
        img = tf.image.stateless_random_contrast(img, lower=0.6, upper=1, seed=(1,3))
        # img = tf.image.stateless_random_crop(img, size=(20,20,3), seed=(1,2))
        # img = tf.image.stateless_random_flip_left_right(img, seed=(np.random.randint(100),np.random.randint(100)))
        # img = tf.image.stateless_random_flip_left_right(img, seed=(1,1))
        img = tf.image.stateless_random_jpeg_quality(img, min_jpeg_quality=60, max_jpeg_quality=100, seed=(10,100))
        img = tf.image.stateless_random_saturation(img, lower=0.85,upper=1, seed=(np.random.randint(100),np.random.randint(100)))
            
        data.append(img)
    
    return data

def flip(img):
    img = tf.image.stateless_random_flip_left_right(img, seed=(1,1))
    return img

path = os.path.join(os.getcwd(), 'images')


for i in os.listdir(path):
    if i.endswith('.jpg'):
        y=1
        print(os.path.join(path, i))
        img = cv2.imread(os.path.join(path, i))
        aug_images = data_aug(img)
        inu = i.split('.')[0]
        print(len(aug_images))
        for im in aug_images:
            im= np.array(im)
            print(os.path.join(path, inu+f'_aug{y}.jpg'))
            cv2.imwrite(os.path.join(path, inu+f'_aug{y}.jpg') , im)
            # cv2.imshow('jj', im)
            # cv2.waitKey(0)
            y = y+1
        print('Done')