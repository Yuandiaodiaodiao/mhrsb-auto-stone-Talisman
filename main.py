# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import numpy as np
import cv2
import matplotlib.pyplot as plt
from get_game import get_GAME
from keyboardsim import press_str, pressdownfor_str

from cnocr import CnOcr
from utils import castimg


def perpareimg(img,argmap,show=False):
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img720p = cv2.resize(img, (1280, 720))
    # img=cv2.cvtColor(img,cv2.COLOR_BGRA2RGB)
    imggray = img720p
    if show:
        plt.subplot(221)
        plt.imshow(imggray)

    h, w = imggray.shape[0:2]

    img_code_matrix = castimg(imggray, argmap, h, w)
    if show:
        plt.subplot(222)
        plt.imshow(img_code_matrix)
        plt.show()
    return img_code_matrix

ocr = CnOcr()





def lian1():
    press_str("f")
    press_str("f")

    press_str("f")

    press_str("d")

    press_str("f")

    press_str("w")

    press_str("f")

    press_str("a")

    press_str("f")
    time.sleep(0.1)
def lian10():
    press_str('w')
    for i in range(10):
        lian1()
    press_str('s')
    press_str('f')
from argsolver import blackList
def autoNext():
    for i in range(30):
        res,skillName = readStone()
        print(res,skillName)
        def checkInBlackList():
            for skill in blackList:
                if skill in "".join(skillName):
                    return True
            return False
        def saveRecord():
            try:
                with open('record.txt', 'a', encoding='utf-8')as f:
                    s = ""
                    for x in zip(skillName, res):
                        s += "".join(x) + " "
                    f.write(s)
                    f.write('\n')
            except:
                pass

        find=0
        try:

            if int(res[0])+int(res[1])>=5 and (not checkInBlackList()):
                press_str('f')
                saveRecord()
                time.sleep(0.2)
                find=1
                continue
        except:
            print('except')
            pass
        finally:
            if find==1:
                continue
            if i==29:
                continue
            press_str('d')
            time.sleep(0.1)
            if i%10==9:
                press_str('s')
                time.sleep(0.1)
    time.sleep(0.2)
    press_str('d')
    press_str('s')
    press_str('s')
    press_str('s')
    press_str('s')
    press_str('s')
    press_str('d')
    time.sleep(0.2)
    press_str('f')
    press_str('a')
    press_str('f')



def readStone():
    img = get_GAME("Monster Hunter Rise")
    imgcut= [ 0.38, 0.55,0.6,0.775]
    img = perpareimg(img,imgcut,False)
    img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retx,img2 = cv2.threshold(img2,150,255,cv2.THRESH_BINARY)
    res = ocr.ocr(img2)
    # print(res)
    resLv=[]
    resName=[]
    for i in res:
        s="".join(i).replace('l','1')
        x=s.split('Lv')
        if len(x)>1:
            resLv.append(x[1])
        else:
            resName.append(s)
    # print(resLv)
    return resLv,resName

def allx():
    lian10()
    time.sleep(0.5)
    autoNext()
def InfinityX():
    while True:
        lian10()
        time.sleep(1)
        autoNext()
        time.sleep(1)
if __name__ == '__main__':
    from keyboard_listener import KListener

    l = KListener()

    # 自动筛选30
    l.bindKeyAsync('f8', autoNext)

    # 自动10炉
    l.bindKeyAsync('f9', lian10)

    # 一轮自动炼丹
    l.bindKeyAsync('f7', allx)

    # 无限自动炼丹
    l.bindKeyAsync('f6', InfinityX)
    l.join()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
