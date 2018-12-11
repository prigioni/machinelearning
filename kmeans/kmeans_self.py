#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 15:05
# @Author  : Qasim
# @File    : kmeans_self.py
# @Software: PyCharm Community Edition

import numpy as np
import random
import matplotlib.pyplot as plt

# 样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xn = np.array([0, 1, 3, 8, 9, 10])
Yn = np.array([0, 2, 1, 8, 10, 7])

# 标识符号
sign_n = ['A', 'B', 'C', 'D', 'E', 'F']
sign_k = ['k1', 'k2']

print(Xn, Yn)
def start_class(Xk, Yk):
    # 数据点分类
    cls_dict = {}
    # 离哪个分类点最近，属于哪个分类
    for i in range(len(Xn)):
        # if Xn[i] in Xk:
        #     continue
        temp = []
        for j in range(len(Xk)):
            d1 = np.sqrt((Xn[i] - Xk[j]) * (Xn[i] - Xk[j]) + (Yn[i] - Yk[j]) * (Yn[i] - Yk[j]))
            temp.append(d1)
            # print('temp', temp)
        min_dis = np.min(temp)
        # print('min_dis', min_dis)
        min_inx = temp.index(min_dis)
        cls_dict[sign_n[i]] = sign_k[min_inx]
    # print(cls_dict)
    return cls_dict


# 重新计算分类的坐标点
def recal_class_point(Xk, Yk, cls_dict):
    num_k1 = 0  # 属于k1的数据点的个数
    num_k2 = 0  # 属于k2的数据点的个数
    x1 = 0  # 属于k1的x坐标和
    y1 = 0  # 属于k1的y坐标和
    x2 = 0  # 属于k2的x坐标和
    y2 = 0  # 属于k2的y坐标和

    # 循环读取已经分类的数据
    for d in cls_dict:
        # 读取d的类别
        kk = cls_dict[d]
        if kk == 'k1':
            # 读取d在数据集中的索引
            idx = sign_n.index(d)
            ##累加x值
            x1 += Xn[idx]
            ##累加y值
            y1 += Yn[idx]
            ##累加分类个数
            num_k1 += 1
        else:
            # 读取d在数据集中的索引
            idx = sign_n.index(d)
            ##累加x值
            x2 += Xn[idx]
            ##累加y值
            y2 += Yn[idx]
            ##累加分类个数
            num_k2 += 1
    ##求平均值获取新的分类坐标点
    k1_new_x = x1 / num_k1  # 新的k1的x坐标
    k1_new_y = y1 / num_k1  # 新的k1的y坐标

    k2_new_x = x2 / num_k2  # 新的k2的x坐标
    k2_new_y = y2 / num_k2  # 新的k2的y坐标

    ##新的分类数组
    Xk = np.array([k1_new_x, k2_new_x])
    Yk = np.array([k1_new_y, k2_new_y])
    return Xk, Yk


def draw_point(Xk, Yk, cls_dict):
    # 画样本点
    plt.figure(figsize=(5, 4))
    plt.scatter(Xn, Yn, color="green", label="数据", linewidth=1)
    plt.scatter(Xk, Yk, color="red", label="分类", linewidth=1)
    plt.xticks(range(0, 15))
    plt.xlim([1, 15])
    plt.ylim([1, 15])
    plt.legend()
    for i in range(len(Xn)):
        plt.text(Xn[i], Yn[i], sign_n[i] + ":" + cls_dict[sign_n[i]])
        for i in range(len(Xk)):
            plt.text(Xk[i], Yk[i], sign_k[i])
    plt.show()


if __name__ == '__main__':
    # 聚类个数
    k = 2
    # 随机种子
    base = 0  # 上限
    up = 4  # 下限
    resultList = random.sample(range(base, up + 1), 2)
    print(resultList)
    lx = []
    ly = []
    for i in resultList:
        lx.append(Xn[i])
        ly.append(Yn[i])
    lx = [0, 1]
    ly = [0, 2]
    Xk = np.array(lx)
    Yk = np.array(ly)
    print(Xk, Yk)
    # 聚类后的点与之前的点变化不大于0.5，退出
    threshold = 1
    while threshold > 0.5:
        cls_dict = start_class(Xk, Yk)
        print('cls_dict', cls_dict)
        Xk_new, Yk_new = recal_class_point(Xk, Yk, cls_dict)
        threshold = float((sum(abs(Xk_new - Xk)) + sum(abs(Yk_new - Yk))) / 2)
        # print(threshold)
        Xk = Xk_new
        Yk = Yk_new
        # draw_point(Xk, Yk, cls_dict)
