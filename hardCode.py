from socket import timeout
from telnetlib import XDISPLOC
#rom cv2 import threshold
import numpy as np
import pandas as pd
import serial

if __name__ == '__main__':
    # assume you saved your recordings into a "data" folder
    A = pd.read_csv("testA.csv")    
    B = pd.read_csv("testB.csv")
    #C = pd.read_csv("testC.csv")
    #D = pd.read_csv("testD.csv")

    thres = 10
    aArr = (A.to_numpy()).mean(axis=0)
    bArr = (B.to_numpy()).mean(axis=0)
    #C.to_numpy()
    #D.to_numpy()

    def predict(arr):
        if (arr > aArr-thres and arr < aArr+thres):
            print('A')
        elif (arr> bArr-thres and arr < bArr+thres):
            print('B')
        else:
            print("undefined")

    try:
        arduino = serial.Serial("COM4", timeout= 1.1)
    except:
        print("Error")
    
    rawdata = []
    while True:
        rawdata = str(arduino.readline())
        cleandata = rawdata[2:-5]
        try:
            arr = list(map(float,cleandata.split(',')))
            predict(arr)
        except:
            continue
    