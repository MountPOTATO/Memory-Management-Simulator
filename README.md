# 同济大学软件学院操作系统课程项目——内存管理：请求分页分配方式

## 1.项目简介

假设每个页面可存放10条指令，分配给一个作业的内存块为4。模拟一个作业的执行过程，该作业有320条指令，即它的地址空间为32页，目前所有页还没有调入内存。给定条件下简单的模拟一个内存调度过程, 置换算法使用FIFO算法或LRU算法

## 2.开发环境与项目结构

- 操作系统: Win10 64位

- 开发工具:

  1.Visual Studio Code 2019

  2.PyCharm Community Edition 2020.1.3 x64 (Qt Designer,PyUIC5 as External Tools)

- 开发语言:  Python3

- 所使用的第三方库:

  PyQt5 (使用Qt为前端框架，PyQt5为支持python3的Qt版本框架)

- 项目文件结构:

  *widget.py*:包含该项目的可视化组件，由Qt Designer绘制并由pyuic5转码生成

  *operation.py*:包含执行顺序函数的声明，使用yield方法进行迭代，调用时使用next方法获取迭代返回结果

  *run.py*:包含该项目的主窗口，以及核心列表、按钮触发函数、调页算法等部分的部署

  *resources*:包含该项目所有的图片(.png)，可执行文件图标(.ico)

  

## 3.功能简介

### 3.1 界面说明与功能描述:

<img src="https://gitee.com/mount-potato/markdown-img-hosting/raw/master/pic/20210609184025.png" alt="img" style="zoom: 50%;" />

界面如上，该程序的实现有:

- 分配给该作业4个内存块, 每个页面可以存放10条指令,该作业有320条指令
- 随机生成320条指令的序列, 50%顺序执行, 25%均匀分布在前地址, 25%均匀分布在后地址
- 可选择LRU，FIFO两种置换算法
- 可选择顺序执行，跳步执行(即"50%顺序执行, 25%均匀分布在前地址, 25%均匀分布在后地址")，随机执行三种执行模式
- 按下单步执行按钮执行一条指令
- 按下连续执行按钮，持续执行指令直到停止
- 按下重置按钮进行重置
- 实时显示缺页数与缺页率



## 4.实现与算法详述:

### 4.1 调页算法实现

调页算法用于当新的页要调入已经满的内存时对新旧页替换的方案，如何选取所谓的旧页影响到缺页率，所以调页算法的机制也影响着这一过程的效率。

在实现时，我使用 `current_page` 列表记录4个内存块中存放的当前页数，同时使用一些其他的信息列表存储相应的信息，在进行页面替换时将以这些信息列表作为替换依据（时间以 `counter` 计数方式记录 ）

#### 4.1.1 FIFO算法

FIFO算法是最简单的页面替换算法之一，它在进行页面替换时，更换掉最早换入内存的页。

我用 `add_time` 列表记录4个内存块存储的页调入的时间，在调用FIFO算法时的代码如下:

```python
    def FIFO(self):
        return min(list(enumerate(self.add_time)),key=lambda x: x[1])[0]
```

即：获取 `add_time` 列表中所有的索引与换入时间值，找出最小的时间值（也就是最早），返回对应的索引（也就是对应的页号）

#### 4.1.2 LRU算法

FIFO算法只记录页面第一次进入内存的时间，因此如果第一次进入的页面是常用页面，那么就会发生多次没意义的缺页中断，降低性能。

LRU算法是另一种可行的方案，它基于局部性原理，认为过去一段时间里不曾被访问过的页面，在最近的将来可能也不会再被访问。它在进行页面替换时，更换掉最近一段时间内最久不适用的页面进行淘汰。

我用 `check_time` 列表记录4个内存块存储的页最近使用的时间。当页面新调入时，`add_time` 列表与 `check_time` 列表同步更新；而在发生命中时， 命中的对应内存块将更新 `check_time` 的对应值 。调用LRU算法时的代码如下：

```python
    def FIFO(self):
        return min(list(enumerate(self.check_time)),key=lambda x: x[1])[0]
```

即：获取 `check_time` 列表中所有的索引与换入时间值，找出最小的时间值（也就是最早），返回对应的索引（也就是对应的页号）

### 4.2 内存替换机制的实现

单步执行一条代码时的流程如下:

```
if 已执行指令条数==320
	return
根据指定顺序（顺序、随机、跳步）获取下一个指令逻辑地址
根据获取的逻辑地址确定页号，页内偏移
for循环遍历页表:
	if 出现命中:
		更新对应页的check_time值
		break

若都不命中:
	更新缺页数
	根据LRU()或FIFO()函数获取需要替换的内存块索引
	进行调换,对新换入的页面更新add_time与check_time值
	
更新缺页率
```

![img](https://gitee.com/mount-potato/markdown-img-hosting/raw/master/pic/20210609195513.png)



### 4.3 指令访问顺序（跳步）

本程序支持顺序（循环执行），跳步，随机顺序访问指令，其中跳步指令设定为"50%顺序执行, 25%均匀分布在前地址, 25%均匀分布在后地址"

本程序采用的方式如下：

1. 在0 - 319条指令中, 随机出一个起始指令, 记作m, 执行m
2. 选择m+1作为下一条顺序执行的指令
3. 用随机函数在0 - m-1中随机一个数作为前段指令, 将其记作m_1
4. 选择m_1+1作为下一条顺序执行的指令
5. 用随机函数在m_1+2 - 319中随机一个数作为前段指令, 将其记作m_2
6. 选择m_2+1作为下一条顺序执行的指令
7. 循环执行步骤3~6, 直至运行320次为止

算法实现上，采用Python的语言特性生成器调用，使得函数调用具有序列性（见*operation.py*中源码)

## 5.运行截图

<img src="https://gitee.com/mount-potato/markdown-img-hosting/raw/master/pic/20210609184212.png" alt="img" style="zoom: 34%;" /> <img src="https://gitee.com/mount-potato/markdown-img-hosting/raw/master/pic/20210609184452.png" alt="img" style="zoom:34%;" />

如图：

左——FIFO算法执行界面展示								右——LRU算法执行界面展示

说明：指令访问时，将同时更调页情况表与详细情况说明文本框，可以在调页情况表中查看简略的命中或调页情况，在文本框中查看详细说明，对四个内存块，有简略的可视化显示当前访问的指令地址。当指令访问无需换页时，文本框中的文段为绿色；当指令访问需要换页时，文本框中文段以及下方换入的新页的标签设为黄色。

## 6.项目总结

### 6.1个人认为的亮点

- 一定的可视化
- 设置了简要表与详细说明日志框
- 日志输出内容较为清晰明确
- 代码注释清晰

### 6.2 项目待改进之处

- 指令访问模拟机制：该模拟机制距离模拟出真实程序应有的工作集合还有较远的距离
- 代码编写：在部分模块出现一些代码赘余，需要对代码可读性继续进行改进

### 6.3 项目收获

- 通过模拟项目熟悉了内存管理中请求分页分配方式
- 对FIFO与LRU等算法通过代码实现的方式更加
- 熟悉了Python的生成器机制
