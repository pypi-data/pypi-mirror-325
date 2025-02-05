import os
import time
import pickle
import mediapipe as mp
import cv2
from google.protobuf.json_format import MessageToDict


class HandDetector:
    def __init__(self):
        mpHands = mp.solutions.hands
        self.hand = mpHands.Hands()
        self.cap = cv2.VideoCapture(0)

    def capture(self):
        """
        captures the 10 frames and processes it
        :return: the position of all landmarks in the 10 frames in form of [[[x, y, z]<- each landmark, [x, y, z]...]<- each frame, [[x, y, z], [x, y, z]...] ...]
        """
        res = []
        for i in range(10):
            success, img = self.cap.read()
            res.append(img)
            time.sleep(0.1)
            # img = cv2.flip(img, 1)
            # for the detection
            # res[i] = cv2.flip(res[i], 1)
            res[i] = cv2.cvtColor(res[i], cv2.COLOR_BGR2RGB)
            res[i] = self.hand.process(res[i])
            no_hands = res[i]
            res[i] = res[i].multi_hand_landmarks
            if res[i] is None:
                raise RuntimeError("Hand either not detected or complete hand not on screen.")
            lr_hand = 0
            if len(no_hands.multi_handedness) == 2:
                lr_hand = 0
            else:
                for k in no_hands.multi_handedness:
                    label = MessageToDict(k)['classification'][0]['label']
                    if label == 'Left':
                        lr_hand = -1
                    if label == 'Right':
                        lr_hand = 1


            temp = []
            for j in res[i]:
                for k in j.landmark:
                    temp.append([k.x, k.y, k.z])
                    x,y,_ = img.shape
                    cv2.circle(img, (int(k.x*y), int(k.y*x)),  5, (255, 0, 255), 5)
            temp.append(lr_hand)
            res[i] = temp
            cv2.imshow("HandDetector", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # cv2.waitKey()
        return res

    def detect(self, res):
        """
        Takes in 10 images from direct openCV format and returns the formatted result
        :param res: list of 10 images from openCV
        :return: the position of all landmarks in the 10 frames in form of [[[x, y, z]<- each landmark, [x, y, z]...]<- each frame, [[x, y, z], [x, y, z]...] ...]
        """
        for i in range(len(res)):
            # res[i] = cv2.flip(res[i], 1)
            res[i] = cv2.cvtColor(res[i], cv2.COLOR_BGR2RGB)
            res[i] = self.hand.process(res[i])

            lr_hand = 0
            if len(res[i].multi_handedness) == 2:
                lr_hand = 0
            else:
                for i in res[i].multi_handedness:
                    label = MessageToDict(i)['classification'][0]['label']
                    if label == 'Left':
                        lr_hand = -1
                    if label == 'Right':
                        lr_hand = 1

            res[i] = res[i].multi_hand_landmarks
            temp = []
            for j in res[i]:
                for k in j.landmark:
                    temp.append([k.x, k.y, k.z])
            temp.append(lr_hand)
            res[i] = temp
            print(res[i])
        return res


    def distance(self, a, b):
        """
        Finds the cosec value between two set of landmark values given.
        :param a: the position of all landmarks in the 10 frames in form of [[[x, y, z]<- each landmark, [x, y, z]...]<- each frame, [[x, y, z], [x, y, z]...] ...]
        :param b: the position of all landmarks in the 10 frames in form of [[[x, y, z]<- each landmark, [x, y, z]...]<- each frame, [[x, y, z], [x, y, z]...] ...]
        :return: cosec distance between vector a and vector b
        """
        dot_prod = 0
        moda = 0
        modb = 0
        for i in range(min(len(b), len(a))):
            for j in range(min(len(b[i])-1, len(a[i])-1)):
                dot_prod += a[i][j][0]*b[i][j][0]
                dot_prod += a[i][j][1]*b[i][j][1]
                dot_prod += a[i][j][2]*b[i][j][2]
                moda += a[i][j][0]**2 + a[i][j][1]**2 + a[i][j][2]**2
                modb += b[i][j][0]**2 + b[i][j][1]**2 + b[i][j][2]**2
            dot_prod += a[i][-1]*b[i][-1]
            moda += a[i][-1] ** 2
            modb += b[i][-1] ** 2
        dot_prod /= (moda**(0.5))*(modb**(0.5))
        cosec = 1/((1-dot_prod**2)**(0.5))
        return cosec

    def store(self, res, label, path="./signData"):
        """
        Stores the landmark positions in a .dat file in given location.
        :param res: The position of all landmarks in the 10 frames in form of [[[x, y, z]<- each landmark, [x, y, z]...]<- each frame, [[x, y, z], [x, y, z]...] ...]
        :param label: Name of the sign
        :param path: Location of all the .dat file
        :return:
        """
        if not os.path.exists(path):
            os.makedirs(path)
        if ".dat" in label:
            f = open(path + "/" + label, "wb")
        else:
            f = open(path + "/" + label + ".dat", "wb")
        pickle.dump(res, f)
        f.close()

    def check(self, res, path="./signData"):
        """
        Checks which sign the current sign is closest to
        :param res: The position of all landmarks in the 10 frames in form of [[[x, y, z]<- each landmark, [x, y, z]...]<- each frame, [[x, y, z], [x, y, z]...] ...]
        :param path:
        :return: Location of all the .dat file
        """
        try:
            l = os.listdir(path)
        except FileNotFoundError:
            raise FileNotFoundError("Path not found")
        dats = [i for i in l if ".dat" in i]
        if len(dats) == 0:
            raise FileNotFoundError("No data found or wrong path")
        vals = dict()
        for i in dats:
            f = open(path + "/" + i, "rb")
            dat = pickle.load(f)
            vals[self.distance(res, dat)] = i
        m = max(vals.keys())
        ans = vals[m]
        return "".join(ans.split(".")[:-1])

    def livefeed(self):
        res = []
        words = []
        while True:
            success, img = self.cap.read()
            res.append(img)
            time.sleep(0.1)
            res[-1] = cv2.cvtColor(res[-1], cv2.COLOR_BGR2RGB)
            res[-1] = self.hand.process(res[-1])
            no_hands = res[-1]
            lr_hand = 0

            res[-1] = res[-1].multi_hand_landmarks
            if res[-1] is not None:
                temp = []
                for j in res[-1]:
                    for k in j.landmark:
                        temp.append([k.x, k.y, k.z])
                        x, y, _ = img.shape
                        cv2.circle(img, (int(k.x * y), int(k.y * x)), 5, (255, 0, 255), 5)
                temp.append(lr_hand)
                res[-1] = temp

                if len(no_hands.multi_handedness) == 2:
                    lr_hand = 0
                else:
                    for k in no_hands.multi_handedness:
                        label = MessageToDict(k)['classification'][0]['label']
                        if label == 'Left':
                            lr_hand = -1
                        if label == 'Right':
                            lr_hand = 1
                res[-1].append(lr_hand)
                if len(res) >= 10:
                    # print(res)
                    words.append(self.check(res[-10:]))
                    # print(words[-1])
            else:
                res.pop(-1)
            cv2.imshow("HandDetector", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # cv2.waitKey()

        return words
