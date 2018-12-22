# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liuqm
# datetime:2018/12/22 15:05
# software: PyCharm

# 在原始语料库中，存在多个连续空格以及空行等不便处理的字符。所以先用正则表达式对原始语料库进行处理。
# 删除每一行前面的19980101-01-001-001/m。
import codecs
import re

fin = codecs.open("词性标注%40人民日报199801.txt", "r", "utf-8")
lines = fin.readlines()
l = []
for strl in lines:
    if strl.strip() == '':
        continue
    strl = re.sub("\[", "", strl)
    strl = re.sub("]nt", "", strl)
    strl = re.sub("]ns", "", strl)
    strl = re.sub("]nz", "", strl)
    strl = re.sub("]l", "", strl)
    strl = re.sub("]i", "", strl)
    strl = re.sub("\n", "@", strl)
    strl = re.sub("\s+", " ", strl)
    strl = re.sub("@", "\n", strl)
    strl = re.sub(" \n", "\n", strl)
    strl = re.sub(" ", "@", strl)
    strl = re.sub("\s+", "\n", strl)
    strl = re.sub("@", " ", strl)
    strl = strl.split()
    l.append(' '.join(strl[1:]))
with open("处理语料.txt", "w") as fout:
    fout.write('\n'.join(l))
fout.close()
fin.close()
