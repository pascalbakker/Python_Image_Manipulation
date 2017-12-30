import numpy as np
from PIL import Image
import glob
import math

"""
    Pascal Bakker
    12/29/17
    Image Manipulation and Linear Algebra
    This project is made to show how to manipulate images using linear algebra and numpy. 
"""

#Rotate image given degree
def rotate_image(arg):
    #Ask for user input
    degrees = int(input("Degrees to rotate: "))
    degrees %= 360

    #number of rows
    n = arg.shape[0]
    #matrix M
    M = math.sqrt(2)*np.array([[math.cos(degrees),-1*math.sin(degrees)],
                               [math.sin(degrees),math.cos(degrees)]])
    arg_new = np.zeros(shape=(3*arg.shape[0], 3*arg.shape[1], 3))
    for z in range(arg.shape[2]):
        for x in range(arg.shape[0]):
            for y in range(arg.shape[1]):
                coord = np.array([[x],
                                  [y]])
                new_coord = np.zeros(shape=(2,1))
                new_coord = np.dot(M,coord)
                new_coord = new_coord.astype(int)
                #print(str(new_coord[0])+" "+str(new_coord[1]))
                """
                if new_coord[0]<0 or new_coord[1] < 0:
                    print(str(new_coord[0]) + " " + str(new_coord[1]))
                """

                arg_new[arg.shape[0]+new_coord[0], arg.shape[1]+new_coord[1], z] = arg[x][y][z]

    return arg_new

#Change color of the images depending on the RGB percentage
def change_color(arg):
    #Get user input
    R,G,B=-1.0
    while R<0.0 or G<0.0 or B<0.0 or R>1.0 or G>1.0 or B>1.0:
        print("Enter values between 0 and 1")
        R = float(input("R: "))
        G = float(input("G: "))
        B = float(input("B: "))
        arg = arg.astype(float)

    #Manipulate image
    arg[:, :, : 0] *= R
    arg[:, :, : 1] *= G
    arg[:, :, : 2] *= B

    return arg


def main():
    #Modes
    modes ={
        1: rotate_image,
        2: change_color,
        #3: blur_image,
        #4: filter_image,
    }

    #Images
    X_data = []
    # Load images
    for image_path in glob.glob("venv/images/*.jpg"):
        image = Image.open(image_path)
        image = image.resize((500, 500), Image.ANTIALIAS)
        image_array = np.array(image)
        X_data.append(image_array)

    #Choose image
    index=-1
    while index<0 or index>len(X_data):
        index = int(input("Choose picture between 0 and "+str(len(X_data))+": "))
    chosen_image = X_data[index]

    index=-1

    #Choose mode
    print("1:rotate image\n2:change color\n3:blur\nfilter")
    while index<0 or index >8:
        index = int(input("Choose mode between 0 and "+str(len(X_data))+": "))

    #Execute mode

    chosen_image= modes[index](chosen_image)

    img = Image.fromarray(chosen_image.astype('uint8'),mode="RGB")
    img.show()


if __name__ == "__main__": main()


""""
def blur_image(arg):

def filter_image(arg):
"""


