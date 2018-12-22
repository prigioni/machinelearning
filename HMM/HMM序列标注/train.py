# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liuqm
# datetime:2018/12/22 15:11
# software: PyCharm

import codecs
import pickle


def get_pos():
    # 所有的词性
    pos = []
    fin = codecs.open("处理语料.txt", "r", "utf-8")
    while True:
        text = fin.readline()
        if text == "":
            break
        tmp = text.split(" ")
        n = len(tmp)
        for i in range(0, n - 1):
            word = tmp[i].split('/')
            if word[1] not in pos:
                pos.append(word[1])
    return pos


def get_wwAB():
    # 状态转移概率矩阵
    A = {}
    # 观测概率矩阵
    B = {}
    # 先验概率矩阵
    pi = {}
    # 每个词性出现的频率
    fre = {}
    pos = get_pos()
    fin = codecs.open("分词语料.txt", "r", "utf-8")
    text = fin.read()
    # 对词表去重
    text = text.replace('\n', ' ')
    ww = list(set(text.split()))
    # 初始化概率矩阵
    for i in pos:
        pi[i] = 0
        fre[i] = 0
        A[i] = {}
        B[i] = {}
        for j in pos:
            A[i][j] = 0
        for j in ww:
            B[i][j] = 0
    return ww, A, B, pos, fre, pi


def cal():
    # 所有词语
    ww = []
    # dp概率
    dp = []
    # 路径记录
    pre = []
    zz = {}
    ww, A, B, pos, fre, pi = get_wwAB()
    # 计算概率矩阵
    line = 0  # 总行数
    fin = codecs.open("处理语料.txt", "r", "utf-8")

    while True:
        text = fin.readline()
        if text == "\n":
            continue
        if text == "":
            break
        tmp = text.split(" ")
        n = len(tmp)
        line += 1
        for i in range(0, n - 1):
            word = tmp[i].split('/')
            pre = tmp[i-1].split('/')
            fre[word[1]] += 1
            if i == 0:
                pi[word[1]] += 1
            elif i > 0:
                A[pre[1]][word[1]] += 1
            B[word[1]][word[0]] += 1

    cx = {}
    cy = {}
    for i in pos:
        cx[i] = 0
        cy[i] = 0
        pi[i] = pi[i] * 1.0 / line
        for j in pos:
            if A[i][j] == 0:
                cx[i] += 1
                A[i][j] = 0.5
        for j in ww:
            if B[i][j] == 0:
                cy[i] += 1
                B[i][j] = 0.5

    for i in pos:
        pi[i] = pi[i] * 1.0 / line
        for j in pos:
            A[i][j] = A[i][j] * 1.0 / (fre[i] + cx[i])
        for j in ww:
            B[i][j] = B[i][j] * 1.0 / (fre[i] + cy[i])

    return pos, pi, A, B


if __name__ == "__main__":
    # 训练并保存中间结果
    pos, pi, A, B = cal()
    output1 = open('pos.pkl', 'wb')
    pickle.dump(pos, output1)
    output1.close()
    output2 = open('pi.pkl', 'wb')
    pickle.dump(pi, output2)
    output2.close()
    output3 = open('A.pkl', 'wb')
    pickle.dump(A, output3)
    output3.close()
    output4 = open('B.pkl', 'wb')
    pickle.dump(B, output4)
    output4.close()
    print("训练结束")