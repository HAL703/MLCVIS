import matplotlib.pyplot as mpl
import numpy as np
import cv2 #this is a wrapper for OpenCV python bindings, main library
from skimage.filters import threshold_otsu as TOT #used for the bit masking algorithm

class Algorithms:
    def Kmeans(imgStr):
        imgToRead = cv2.imread(imgStr) #reads an image name from the given path (same directory) using cv2
    
        #---------------PREPROCESSING-------------------------

        imgToRead = cv2.cvtColor(imgToRead, cv2.COLOR_BGR2RGB) #converts image to an RGB "color space" pixel by pixel
        twoDVector = imgToRead.reshape((-1,3)) #images are 3D with a width, height, and depth of 3 color channels
        #"reshaping" along the image's first axis to convert into a 2D vector with 3 rgb color channels
        #if image was (2,2,3), width, height, channels respectively, then it would be shaped into (4,3)
        twoDVector = np.float32(twoDVector) #converts vector into a float, required for kmeans algorithm in cv2

        #---------------CRITERIA------------------------------
        #defining criteria for how the K-means algo clusters pixels together
        crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2) 
        K=8 #K value represents the number of groups a pixel can belong to, higher K = higher segmentation
        attempts=10 #helps stop the algorithm from going too long

        #---------------APPLICATION---------------------------

        _,labels,centers = cv2.kmeans(twoDVector,K,None,crit,attempts,cv2.KMEANS_PP_CENTERS) #unpacking into 3 variables, _ doesn't matter here
        center = np.uint8(centers) #converting back to 8-bit pixel values
        res = center[labels.flatten()] #this constructs the segmented image by converting all pixels to the colors of the centroids (centers) after flattening the labels array
        res_image = res.reshape((imgToRead.shape))
        mpl.imshow(res_image)
        mpl.show()

    def Cdetect(imgStr):
        imgToRead = cv2.imread(imgStr)

        #---------------PREPROCESSING-------------------------

        rgb = cv2.cvtColor(imgToRead, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)

        #---------------CRITERIA------------------------------

        lightGreen = (40,40,40)
        darkGreen = (70,255,255)
        colorMask = cv2.inRange(hsv, lightGreen, darkGreen)

        #---------------APPLICATION---------------------------

        res_image = cv2.bitwise_and(imgToRead, imgToRead, mask=colorMask)
        mpl.imshow(res_image)
        mpl.show()
    def Bmask(imgStr): #this will have to use thresholding to apply the imgFilter function
        imgToRead = cv2.imread(imgStr)

        #---------------PREPROCESSING-------------------------
        #converting image from BGR to RGB in order to get it to grayscale
        rgb = cv2.cvtColor(imgToRead, cv2.COLOR_BGR2RGB)
        grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

        #---------------APPLICATION---------------------------

        def imgFilter(img, mask): #this REQUIRES a binary image, not a grayscale image
            r = img[:,:,0] * mask #multiplying each color channel by the mask
            g = img[:,:,1] * mask
            b = img[:,:,2] * mask
            return np.dstack([r,g,b])
        threshold = TOT(grayscale) #thresholding means to create a binary image from a grayscaled image, TOT is just one of many algorithms
        thresholdedImg = grayscale < threshold
        filteredImg = imgFilter(imgToRead, thresholdedImg) #using the base image's channels and multiplying by the thresholded masks
        mpl.imshow(filteredImg)
        mpl.show()
