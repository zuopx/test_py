#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def solution(arr):
    if len(arr) == 0:
        return 0
    ret = 0
    for i in range(len(arr) - 1):
        ret = ret + helper1(arr, i)
    return ret


def helper1(arr, i):
    ind = i
    mi = arr[i]
    for j in range(i + 1, len(arr)):
        if arr[j] < mi:
            mi = arr[j]
            ind = j
    if ind == i:
        return 0
    else:
        tmp = arr[ind]
        for k in range(ind, i):
            arr[k + 1] = arr[k]
        arr[i] = tmp
        return 1

    # ******************************结束写代码******************************


# _arr_cnt = 0
# _arr_cnt = int(input())
# _arr_i = 0
# _arr = []
# while _arr_i < _arr_cnt:
#     _arr_item = int(input())
#     _arr.append(_arr_item)
#     _arr_i += 1
_arr = [1, 9, 7, 5, 3]

res = solution(_arr)

print(str(res) + "\n")
