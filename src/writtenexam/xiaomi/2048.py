#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def solution(input):
    res = ''
    for line in input:
        res = res + helper1(line) + '\n'
    return res


def helper1(line: str):
    nums = list(map(int, line.split()))
    # print(nums)
    i, j = 0, 0
    while i < len(nums):
        if nums[i]:
            j = i + 1
            while j < len(nums) and not nums[j]:
                j = j + 1
            if j < len(nums) and nums[i] == nums[j]:
                nums[i] = 2 * nums[i]
                nums[j] = 0
                i = j  
        i = i + 1
    str1 = ''
    for num in nums:
        if num:
            str1 += str(num) + ' '
    str1 = str1 + nums.count(0) * '0 '
    return str1

    # ******************************结束写代码******************************


_input_cnt = 0
_input_cnt = int(input())
_input_i = 0
_input = []
while _input_i < _input_cnt:
    try:
        _input_item = input()
    except:
        _input_item = None
    _input.append(_input_item)
    _input_i += 1

res = solution(_input)

print(res + "\n")
