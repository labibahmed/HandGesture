from socket import timeout
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import serial

if __name__ == '__main__':
    # assume you saved your recordings into a "data" folder
    A = pd.read_csv("testA.csv")
    V = pd.read_csv("testV.csv")
    Y = pd.read_csv("testY.csv")

    X = np.vstack([
        A.to_numpy(),
        V.to_numpy(),
        Y.to_numpy()
    ])

    def num2str(i):
        alpha = "AVY"
        return alpha[i]

    Label = np.concatenate([
        0*np.ones(len(A)),
        1*np.ones(len(V)),
        2*np.ones(len(Y)),
    ])

    clf = RandomForestClassifier().fit(X,Label)

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
            gesture = num2str(int(clf.predict([arr])))
            print(gesture)
        except:
            continue
    