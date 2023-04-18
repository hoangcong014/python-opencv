# please install some packages first
'''
pip install cvzone
pip install matplotlib
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation


def read_image(path):
    #image = cv2.imread(r"images/tieuvi_dress_1.jpg", 1)
    image = cv2.imread(path, 1)
    if image is not None:
        return image
    else:
        return None

def rm_background(image):
    segmentor = SelfiSegmentation()
    green = (0, 255, 0)
    #black = (0, 0, 0)
    imgNoBg = segmentor.removeBG(image, green, threshold=0.5)
    return imgNoBg

def resize_image(image, width=512, height=512):
    img_stretch_near = cv2.resize(image, (width, height), interpolation = cv2.INTER_LINEAR)
    return img_stretch_near

def some_resize_overview(image):
    half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
    bigger = cv2.resize(image, (1050, 1610))
    stretch_near = cv2.resize(image, (1024, 1024), interpolation = cv2.INTER_LINEAR)
    
    Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
    images =[image, half, bigger, stretch_near]
    count = 4 
    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])
        plt.show()

def save_image(image, path, filename):
    cv2.imwrite(path +"/"+filename, image)

def main():
    img_path ="images/woman_dress.jpg"
    img = read_image(img_path)
    print("Some resize overview:")
    #some_resize_overview(img)
    print("Custome resize default:")
    img_default_512 = resize_image(img)
    cv2.imshow('Resize Default 512', img_default_512)
    #img_default_512 = rm_background(img_default_512)
    save_image(img_default_512, "images", "woman_dress_512.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()