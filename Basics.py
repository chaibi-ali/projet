import cv2
import numpy as np
from pyzbar.pyzbar import decode

with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines()

while True:
    image = cv2.imread('2.png')

    for barcode in decode(image):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput = True
            print('ce code existe')
        else:
            myOutput = False
            print('ce code existe pas')

    cv2.imshow('Result',image)
    cv2.waitKey(1)

