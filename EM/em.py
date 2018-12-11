# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liuqm
# datetime:2018/12/10 19:23
# software: PyCharm
# https://blog.csdn.net/castle_cc/article/details/78835581
import numpy as np
import math

input = np.array([[1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                  [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                  [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
                  [1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                  [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]])

thetaA = 0.8
thetaB = 0.45
m, n = input.shape
headNums = input.sum(axis=1)
tailNums = n - headNums
# print(headNums)
# print(tailNums)
for i in range(10):
    pAHNum = 0
    pATNum = 0
    pBHNum = 0
    pBTNum = 0
    for headNum in headNums:
        pA = math.pow(thetaA, headNum) * math.pow((1 - thetaA), (n - headNum))
        pB = math.pow(thetaB, headNum) * math.pow((1 - thetaB), (n - headNum))
        pSum = pA + pB
        pA = pA / pSum
        pB = pB / pSum
        pAHNum += headNum * pA
        pATNum += (n - headNum) * pA
        pBHNum += headNum * pB
        pBTNum += (n - headNum) * pB

    thetaA = pAHNum / (pAHNum + pATNum)
    thetaB = pBHNum / (pBHNum + pBTNum)

print(thetaA)
print(thetaB)

