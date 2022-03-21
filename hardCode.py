from socket import timeout
from telnetlib import XDISPLOC
#rom cv2 import threshold
import numpy as np
import pandas as pd
import serial

if __name__ == '__main__':
    # assume you saved your recordings into a "data" folder
    # read each csv
    A = pd.read_csv("testA.csv")
    B = pd.read_csv("testB.csv")
    C = pd.read_csv("testC.csv")
    D = pd.read_csv("testD.csv")
    E = pd.read_csv("testE.csv")
    F = pd.read_csv("testF.csv")
    G = pd.read_csv("testG.csv")
    H = pd.read_csv("testH.csv")
    I = pd.read_csv("testI.csv")
    J = pd.read_csv("testJ.csv")
    K = pd.read_csv("testK.csv")
    L = pd.read_csv("testL.csv")
    M = pd.read_csv("testM.csv")
    N = pd.read_csv("testN.csv")
    O = pd.read_csv("testO.csv")
    P = pd.read_csv("testP.csv")
    Q = pd.read_csv("testQ.csv")
    R = pd.read_csv("testR.csv")
    S = pd.read_csv("testS.csv")
    T = pd.read_csv("testT.csv")
    U = pd.read_csv("testU.csv")
    V = pd.read_csv("testV.csv")
    W = pd.read_csv("testW.csv")
    X = pd.read_csv("testX.csv")
    Y = pd.read_csv("testY.csv")
    Z = pd.read_csv("testZ.csv")

    thres = 250 # upper and lower boundry
    # create an array of all the averages
    combinedCSV = np.vstack([
        A.to_numpy().mean(axis=0),
        B.to_numpy().mean(axis=0),
        C.to_numpy().mean(axis=0),
        D.to_numpy().mean(axis=0),
        E.to_numpy().mean(axis=0),
        F.to_numpy().mean(axis=0),
        G.to_numpy().mean(axis=0),
        H.to_numpy().mean(axis=0),
        I.to_numpy().mean(axis=0),
        J.to_numpy().mean(axis=0),
        K.to_numpy().mean(axis=0),
        L.to_numpy().mean(axis=0),
        M.to_numpy().mean(axis=0),
        N.to_numpy().mean(axis=0),
        O.to_numpy().mean(axis=0),
        P.to_numpy().mean(axis=0),
        Q.to_numpy().mean(axis=0),
        R.to_numpy().mean(axis=0),
        S.to_numpy().mean(axis=0),
        T.to_numpy().mean(axis=0),
        U.to_numpy().mean(axis=0),
        V.to_numpy().mean(axis=0),
        W.to_numpy().mean(axis=0),
        X.to_numpy().mean(axis=0),
        Y.to_numpy().mean(axis=0),
        Z.to_numpy().mean(axis=0)
    ])

    # convert number to letter
    def num2str(i):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return alpha[i]

    # go through the loop checking if the arr input fit's within the boundry for any of the letters
    # then it prints the letter based on the index
    def predict2(arr):
        i = 0
        while(not(all(np.greater(arr,combinedCSV[i]-thres)) and all(np.less(arr,combinedCSV[i]+thres)))):
            i = i+1
            if i > 25: break
        if i > 25: print("undefined") 
        else: print(num2str(i))


    try:
        arduino = serial.Serial("COM3", timeout= 1.1)
    except:
        print("Error")
    
    rawdata = []
    while True:
        rawdata = str(arduino.readline())
        cleandata = rawdata[2:-5]
        try:
            arr = list(map(float,cleandata.split(',')))
            predict2(arr)
        except:
            print('Error')
            continue
    