import matplotlib.pyplot as mpl
import numpy as np
import cv2 #this is a wrapper for OpenCV python bindings

path = 'imagePlaceholder.jpg'
imgToRead = cv2.imread(path) #reads an image name from the given path (same directory) using cv2

#---------------PREPROCESSING-------------------------

imgToRead = cv2.cvtColor(imgToRead, cv2.COLOR_BGR2RGB) #converts image to an RGB "color space" pixel by pixel
twoDVector = imgToRead.reshape((-1,3))
#"reshaping" along the image's first axis to convert into a 2D vector
#if image was (2,2,6), width, height, channels respectively, then it would be shaped into (4,6)
twoDVector = np.float32(twoDVector) #converts vector into a float

#---------------CRITERIA------------------------------
#defining criteria for how the K-means algo clusters pixels together
crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
K=4
attempts=10

#---------------APPLICATION---------------------------

ret,label,center = cv2.kmeans(twoDVector,K,None,crit,attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
res_image = res.reshape((imgToRead.shape))
mpl.imshow(res_image)
mpl.show()


