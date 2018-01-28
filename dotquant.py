from math import sqrt
from skimage.feature import blob_log
from skimage.color import rgb2gray
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

def load_image (image_path):

    """

    """

    img = Image.open(image_path)
    img_np = np.array(img)
    img_np_gray = rgb2gray(img_np)

    return img_np_gray

def compute_radii (input_image, image_path):

    """

    """
    blobs_log = blob_log(input_image, max_sigma=0.2, num_sigma=10, threshold=0.2)
    blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

    print("Detected " + str(len(blobs_log)) + " punctae.")
    
    fig, ax = plt.subplots(1, 1, figsize=(15, 9), sharex=True, sharey=True, subplot_kw={'adjustable': 'box-forced'})
    ax.set_title(image_path)
    ax.imshow(input_image, interpolation='nearest')

    blob_radii = []

    for blob in blobs_log:
        y, x, r = blob
        blob_radii.append(r)
        c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
        ax.add_patch(c)

    #print(blob_radii)
    plt.show()


path = input("Enter image path: \n")
data = load_image(path)
compute_radii(data, path)