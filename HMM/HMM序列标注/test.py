# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liuqm
# datetime:2018/12/22 16:22
# software: PyCharm

import pprint, pickle


# 读取保存的中间结果
pkl_pos = open('pos.pkl', 'rb')
pos = pickle.load(pkl_pos)
pkl_pi = open('pi.pkl', 'rb')
pi = pickle.load(pkl_pi)
pkl_A = open('A.pkl', 'rb')
A = pickle.load(pkl_A)
pkl_B = open('B.pkl', 'rb')
B = pickle.load(pkl_B)

while True:
    tmp = input("请输入需要词性标注的句子，以空格分割: ")
    if tmp == "-1":
        break
    text = tmp.split(" ")

    num = len(text)
    for i in range(0, num):
        text[i] = text[i]
    dp = [{} for i in range(0, num)]
    pre = [{} for i in range(0, num)]
    # 初始化概率
    for k in pos:
        for j in range(0, num):
            dp[j][k] = 0
            pre[j][k] = ""
    n = len(pos)
    for c in pos:
        if text[0] in B[c]:
            dp[0][c] = pi[c]*B[c][text[0]]*1000
        else:
            dp[0][c] = pi[c]*0.5*1000/(cy[c]+fre[c])
    for i in range(1, num):
        for j in pos:
            for k in pos:
                tt = 0
                if text[i] in B[j]:
                    tt = B[j][text[i]]*1000
                else:
                    tt = 0.5*1000/(cy[j]+fre[j])
                if dp[i][j] < dp[i-1][k]*A[k][j]*tt:
                    dp[i][j] = dp[i-1][k]*A[k][j]*tt
                    pre[i][j] = k
    res = {}
    MAX = ""
    for j in pos:
        if MAX == "" or dp[num-1][j] > dp[num-1][MAX]:
            MAX = j
    if dp[num-1][MAX] == 0:
        print("您的句子超出我们的能力范围了")
        continue
    i = num-1
    while i >= 0:
        res[i] = MAX
        MAX = pre[i][MAX]
        i -= 1
    result = []
    for i in range(0, num):
        # print(text[i]+"\\"+res[i],)
        result.append(text[i]+"\\"+res[i])
    print(' '.join(result))