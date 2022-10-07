import numpy as np
import cv2
from numpy.core.memmap import uint8
import random


img=cv2.imread(r'C:\Users\kc\Desktop\.venv\Perception\Q1\for_watson.png')
print(f'The shape of image is {img.shape}')
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def decryptImage(img):
    '''
    Input:
      Img: Numpy array image containing the hidden information
  
   Output:
      Decoded images: original and content based image. 
   '''
    # get dimensions of the image
    height=img.shape[0]
    width=img.shape[1]
    channels=img.shape[2]

    # create an empty numpy array representing two images
    newImage= np.zeros((height,width,channels),dtype='uint8')
    originalImage= np.zeros((height,width,channels),dtype='uint8')

    for i in range(height):
        for j in range(width):
            for l in range(channels):
                v1=format(img[i][j][l],'08b')
                v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4 # most significant bits
                v3=v1[4:] + chr(random.randint(0, 1)+48) * 4 # least significant bits
                originalImage[i][j][l]=int(v2,2)
                newImage[i][j][l]= int(v3, 2)
        
    cv2.imwrite("Original.jpg",originalImage)
    cv2.imwrite("NewPic.jpg",newImage)
    #new_image_trial = cv2.convertScaleAbs(newImage, alpha=5, beta=70)
    cv2.imshow('newImage',newImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# call the function
decryptImage(img)
