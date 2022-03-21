from socket import timeout
from telnetlib import XDISPLOC
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import serial

if __name__ == '__main__':
    # assume you saved your recordings into a "data" folder
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


    combinedCSV = np.vstack([
        A.to_numpy(),
        B.to_numpy(),
        C.to_numpy(),
        D.to_numpy(),
        E.to_numpy(),
        F.to_numpy(),
        G.to_numpy(),
        H.to_numpy(),
        I.to_numpy(),
        J.to_numpy(),
        K.to_numpy(),
        L.to_numpy(),
        M.to_numpy(),
        N.to_numpy(),
        O.to_numpy(),
        P.to_numpy(),
        Q.to_numpy(),
        R.to_numpy(),
        S.to_numpy(),
        T.to_numpy(),
        U.to_numpy(),
        V.to_numpy(),
        W.to_numpy(),
        X.to_numpy(),
        Y.to_numpy(),
        Z.to_numpy()
    ])

    def num2str(i):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return alpha[i]

    Label = np.concatenate([
        0*np.ones(len(A)),
        1*np.ones(len(B)),
        2*np.ones(len(C)),
        3*np.ones(len(D)),
        4*np.ones(len(E)),
        5*np.ones(len(F)),
        6*np.ones(len(G)),
        7*np.ones(len(H)),
        8*np.ones(len(I)),
        9*np.ones(len(J)),
        10*np.ones(len(K)),
        11*np.ones(len(L)),
        12*np.ones(len(M)),
        13*np.ones(len(N)),
        14*np.ones(len(O)),
        15*np.ones(len(P)),
        16*np.ones(len(Q)),
        17*np.ones(len(R)),
        18*np.ones(len(S)),
        19*np.ones(len(T)),
        20*np.ones(len(U)),
        21*np.ones(len(V)),
        22*np.ones(len(W)),
        23*np.ones(len(X)),
        24*np.ones(len(Y)),
        25*np.ones(len(Z))
    ])

    clf = RandomForestClassifier().fit(combinedCSV,Label)

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
    