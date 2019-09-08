#https://www.runoob.com/python/python-100-examples.html
#https://blog.csdn.net/github_39655029/article/details/82932848

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-9-8 13:37
# @Author  : JaocnHunt
# @Site    : 
# @File    : Python_100.py
# @Software: PyCharm

#1. 三位数
def main():
    n = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for m in range(1, 5):
                if(i != j) and(j != m)and (i != m):
                    print(i, j, m)
                    n = n+1
    print(n)

if __name__ == '__main__':
    main()
