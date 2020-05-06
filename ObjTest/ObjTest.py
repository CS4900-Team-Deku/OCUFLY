from cv2 import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

"""these images are run through the object recognition, its results are displayed
 for the user to see and the image is saved in the results folder with the 
same name as well a text file is also created with the names of the objects
 that it found"""

#  This image returns 6 people and a tie 
im = cv2.imread('111219.jpg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
cv2.imwrite('Results/111219.jpg', output_image)
new_file = open('Results/111219.txt', 'w')
listToStr = ' '.join([str(elem) for elem in label])    
new_file.write(listToStr)
print(listToStr)
new_file.close()


im2 = cv2.imread('985657.jpg')
bbox2, label2, conf2 = cv.detect_common_objects(im2)
output_image2 = draw_bbox(im2, bbox2, label2, conf2)
plt.imshow(output_image2)
plt.show()
cv2.imwrite('Results/985657.jpg', output_image2)
new_file2 = open('Results/985657.txt', 'w')
listToStr2 = ' '.join([str(elem2) for elem2 in label2])    
new_file2.write(listToStr2)
print(listToStr2)
new_file2.close()


im3 = cv2.imread('2888691.jpg')
bbox3, label3, conf3 = cv.detect_common_objects(im3)
output_image3 = draw_bbox(im3, bbox3, label3, conf3)
plt.imshow(output_image3)
plt.show()
cv2.imwrite('Results/2888691.jpg', output_image3)
new_file3 = open('Results/2888691.txt', 'w')
listToStr3 = ' '.join([str(elem3) for elem3 in label3])    
new_file3.write(listToStr3)
print(listToStr3)
new_file3.close()