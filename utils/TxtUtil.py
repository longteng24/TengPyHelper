# -*- coding: utf-8 -*

"""
txt 文件操作 工具类
"""


# 读取文件，返回列表
def getLines(filename):
    with open(filename, 'r', encoding='utf-8') as rfile:
        parSet = set()
        lst = rfile.readlines()
        for item in lst:
            item = item.replace('\n', '')
            if item is not None and item != '':
                # 获取每一行，第一行默认为uuid
                parSet.add(item)
        print("读取:", len(parSet), "行数据")
        l = list(parSet)
        l.sort()
        return l


