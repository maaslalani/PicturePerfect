from PIL import Image
from google.cloud import vision
from google.cloud.vision import types

import cv2
import numpy as np
from matplotlib import pyplot as plt


def detect_faces(face_file):
    client = vision.ImageAnnotatorClient()
    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations

def display_info(img, hue, sat, val):
    plt.imshow(img)
    plt.show()
    
    plt.figure(figsize=(10, 8))
    plt.subplot(311)                             #plot in the first cell
    plt.subplots_adjust(hspace=.5)
    plt.title("Hue")
    plt.hist(hue, bins=180)
    plt.subplot(312)                             #plot in the second cell
    plt.title("Saturation")
    plt.hist(sat, bins=128)
    plt.subplot(313)                             #plot in the third cell
    plt.title("Luminosity Value")
    plt.hist(val, bins=128)
    plt.show()

def get_average_hsv(input_file):
    img = cv2.imread(input_file) 
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hue, sat, val = hsv_image[:,:,0], hsv_image[:,:,1], hsv_image[:,:,2]
    flat_hue = np.ndarray.flatten(hue)
    flat_sat = np.ndarray.flatten(sat)
    flat_val = np.ndarray.flatten(val)

    avg_hue = np.mean(flat_hue)
    avg_sat = np.mean(flat_sat)
    avg_val = np.mean(flat_val)

    # display_info(hsv_image, flat_hue, flat_sat, flat_val)

    return avg_hue, avg_sat, avg_val

