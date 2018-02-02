from math import sqrt
from skimage.feature import blob_log
from skimage.color import rgb2gray
from PIL import Image, ImageFont, ImageDraw

import matplotlib.pyplot as plt
import numpy as np

def load_image (image_path):

    """ Opens images (.tif, .png, .jpg)

        retruns: input image, input image converted to a numpy array
    """

    img = Image.open(image_path)
    img_np = np.array(img)
    img_np_gray = rgb2gray(img_np)

    return img, img_np_gray

def detect_blobs (input_image_original, input_image_np_gray, image_path):

    """ Detects blobs in converted image (image is converted to numpy array)

        Generates figure which can be saved and number of blobs identified

        returns: null
    """

    # Compute/detect blobs in image
    blobs_log = blob_log(input_image_np_gray, min_sigma=min_sigma_val, max_sigma=max_sigma_val, num_sigma=num_sigma_val, threshold=threshold_val)
    blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

    # Console results
    print("Detected " + str(len(blobs_log)) + " punctae.")

    # Label the image with the number of punctae identified
    # Note: Other operating systems (Windows and OSX) may not have the FreeSans font.  Change the font as necessary for the system.
    #image_draw = ImageDraw.Draw(input_image_original)
    #image_font = ImageFont.truetype("FreeSans.ttf", 60)
    #image_draw.text((0,0), str(len(blobs_log)) + " punctae", (255,255,255), font=image_font)

    fig, ax = plt.subplots(1, 1, figsize=(15, 9), sharex=True, sharey=True, subplot_kw={'adjustable': 'box-forced'})
    ax.set_title(image_path)
    ax.imshow(input_image_original, interpolation='nearest')
    ax.set_axis_off()

    blob_radii = []

    # Add circles to image
    for blob in blobs_log:
        y, x, r = blob
        blob_radii.append(r)
        c = plt.Circle((x, y), r, color='yellow', linewidth=2, fill=False)
        ax.add_patch(c)

    # Write radii results to file

    #output_radiii = open(image_path + "_blob_radii.txt", 'w')
    #for item in blob_radii:
    #    output_radiii.write("%s\n" % item)

    plt.tight_layout()
    plt.show()

def set_user_values ():

    """

    """

    print("Enter values.  Hit enter to select default values")

    # User set min_sigma value
    usr_min_sigma = input("min_sigma value (default = 0.63):")
    if usr_min_sigma is "":
        usr_min_sigma = float(0.63)
        print("min_sigma is set to default value 0.63")
    else:
        usr_min_sigma = float(usr_min_sigma)
        print("min_sigma value is set to: " +  str(usr_min_sigma)) 

    # User set max_sigma value
    usr_max_sigma = input("max_sigma value (default = 4.0):")
    if usr_max_sigma is "":
        usr_max_sigma = float(4.0)
        print("max_sigma is set to default value 4.0")
    else:
        usr_max_sigma = float(usr_max_sigma)
        print("max_sigma value is set to: " + str(usr_max_sigma))

    # User set num_sigma value
    usr_num_sigma = input("num_sigma value (default = 50.0):")
    if usr_num_sigma is "":
        usr_num_sigma = float(50.0)
        print("num_sigma is set to default vaule 50.0")
    else:
        usr_num_sigma = float(usr_num_sigma)
        print("num_sigma value is set to: " +  str(usr_num_sigma))

    # Usesr set threshold value
    usr_threshold = input("threshold value (default = 0.05):")
    if usr_threshold is "":
        usr_threshold = float(0.05)
        print("threshold is set to default value 0.05")
    else:
        usr_threshold = float(usr_threshold)
        print("threshold value is set to: " + str(usr_threshold))

    return usr_min_sigma, usr_max_sigma, usr_num_sigma, usr_threshold

path = input("Enter image path: \n")

min_sigma_val, max_sigma_val, num_sigma_val, threshold_val = set_user_values()
original_image, gray_image = load_image(path)
detect_blobs(original_image, gray_image, path)