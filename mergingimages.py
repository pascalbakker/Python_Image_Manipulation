import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from scipy import misc
import glob


#Data

X_data = []

#Load images
for image_path in glob.glob("venv/images/*.jpg"):
    image = Image.open(image_path)
    image = image.resize((500, 500), Image.ANTIALIAS)
    image_array = np.array(image)
    X_data.append(image_array)


#If no user input, set default image size

images_proc = np.array(X_data)

average_array = images_proc.mean(axis=0)
img = Image.fromarray(average_array.astype('uint8'),mode="RGB")
img.save('my.png')
img.show()





