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
    x=random.randint(0,159)
    while True:
        yield x
        x+=1
        yield x
        x=random.randint(161,318)
        yield x
        x+=1
        yield x
        x=random.randint(0,159)
