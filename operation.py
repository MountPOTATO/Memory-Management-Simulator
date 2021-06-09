'''
Author: mount_potaot
Date: 2021-06-07 22:46:45
LastEditTime: 2021-06-09 15:51:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \ostest\operation.py
'''
import random

#随机执行
def op_rand():
    while True:
        yield random.randint(0,319)

#顺序执行
def op_sequence():
    x=0
    while True:
        yield x
        x+=1
        x=0 if x>=320 else x

#跳步执行
def op_skip():
    x=random.randint(0,319)
    while True:
        yield x
        x+=1
        yield x
        x=random.randint(0,x-1)
        yield x
        x+=1
        yield x
        x=random.randint(x+1,319)
