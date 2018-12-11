# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liuqm
# datetime:2018/12/11 14:31
# software: PyCharm
# reference：https://www.cnblogs.com/ybjourney/p/4770559.html

from math import log


# 计算香农熵(为float类型）
def calShang(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}##创建字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt


def creatDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet,labels

#测试
# myData,labels = creatDataSet()
# print("原数据为：",myData)
# print("标签为：",labels)
# shang = calShang(myData)
# print("香农熵为：",shang)


# 划分数据集（以指定特征将数据进行划分）
def splitDataSet(dataSet, feature, value):
    # 传入待划分的数据集、划分数据集的特征以及需要返回的特征的值
    newDataSet = []
    for featVec in dataSet:
        # print(featVec)
        if featVec[feature] == value:
            reducedFeatVec = featVec[:feature]
            reducedFeatVec.extend(featVec[feature + 1:])
            newDataSet.append(reducedFeatVec)
    return newDataSet

# 测试
# myData, labels = creatDataSet()
# print("原数据为：", myData)
# print("标签为：", labels)
# split = splitDataSet(myData, 0, 1)
# print("划分后的结果为:", split)


# 选择最好的划分方式(选取每个特征划分数据集，从中选取信息增益最大的作为最优划分)在这里体现了信息增益的概念
def chooseBest(dataSet):
    featNum = len(dataSet[0]) - 1
    baseEntropy = calShang(dataSet)
    bestInforGain = 0.0
    bestFeat = -1  ##表示最好划分特征的下标

    for i in range(featNum):
        featList = [example[i] for example in dataSet]  # 列表
        # print(featList)
        # [1, 1, 1, 0, 0]
        # [1, 1, 0, 1, 1]
        uniqueFeat = set(featList)  ##得到每个特征中所含的不同元素
        newEntropy = 0.0
        for value in uniqueFeat:
            subDataSet = splitDataSet(dataSet, i, value)
            # print(subDataSet)
            prob = len(subDataSet) / len(dataSet)
            newEntropy += prob * calShang(subDataSet)
        # print(newEntropy)
        inforGain = baseEntropy - newEntropy
        if (inforGain > bestInforGain):
            bestInforGain = inforGain
            bestFeature = i  # 第i个特征是最有利于划分的特征
    return bestFeature

# 测试
# myData,labels = creatDataSet()
# best = chooseBest(myData)
# print(best)

# 递归构建决策树
import operator
# 返回出现次数最多的分类名称
def majorClass(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    #降序排序，可以指定reverse = true
    sortedClassCount = sorted(classcount.iteritems(),key = operator.itemgetter(1),reverse = true)
    # print(sortedClassCount)
    return sortedClassCount[0][0]


# 创建树
def creatTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    # print(classList[0])
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorClass(classList)
    bestFeat = chooseBest(dataSet)
    # print(bestFeat)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        # print(value)
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = creatTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

# 测试
myData, labels = creatDataSet()
mytree = creatTree(myData,labels)
print(mytree)