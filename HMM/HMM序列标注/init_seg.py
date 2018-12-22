# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: liuqm
# datetime:2018/12/22 15:23
# software: PyCharm

# 剔除处理语料的词性标注。
import codecs
import re
fin = codecs.open("处理语料.txt", "r", "utf-8")
strl = fin.readlines()
pattern = '/[a-zA-z]+'
l = []
for i in strl:
    i = re.sub(pattern, "", i.strip())
    l.append(i.strip())
with open("分词语料.txt", "w") as fout:
    fout.write('\n'.join(l))
fout.close()
fin.close()