'''
Author: mount_potato
Date: 2021-06-07 00:10:18
LastEditTime: 2021-06-08 18:59:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \ostest\run.py
'''

import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtGui import QIcon
from widget import Ui_QWidget
from operation import *


TOTAL_INS=320
NOPE=-1

class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super(MainWidget,self).__init__()
        #主界面设置
        self.ui=Ui_QWidget()
        self.ui.setupUi(self)
        self.setWindowTitle("OS assignment-2 :Demand Paging Memory Management Simulator")
        self.setWindowIcon(QIcon("./resources/window_icon.png"))
        
        #计数器
        self.counter = 0
        #缺页总数
        self.miss_page_sum = 0
        #内存管理可选项：执行顺序函数，执行算法
        self.order = op_sequence()
        self.algorithm = self.FIFO
        #组件列表：当前页号文本，当前页号可视化显示
        self.page_labels = (self.ui.page_text_1, self.ui.page_text_2, self.ui.page_text_3, self.ui.page_text_4)       
        self.page_visual=(self.ui.visual_1,self.ui.visual_2,self.ui.visual_3,self.ui.visual_4)
        #组件列表文本内容初设
        for i in range(0,len(self.page_labels)):
            self.page_visual[i].setText("")
            self.page_labels[i].setText("null")

        #4个内存块的当前页号
        self.current_page = [NOPE, NOPE, NOPE, NOPE]
        self.fresh_time = [NOPE, NOPE, NOPE, NOPE]
        self.access_time = [NOPE, NOPE, NOPE, NOPE]

        #日志显示:指令执行情况表格与指令详细情况文本框输出
        self.table=self.ui.ins_table
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['逻辑地址', '所在页', '是否缺页', '换出页', '换入页'])
        self.log=self.ui.notification
        
        #触发函数绑定
        #连续显示按钮计时器
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.ui.op_one_button.click)

        #按钮的触发函数绑定
        self.ui.op_one_button.clicked.connect(self.on_one_button_clicked)
        self.ui.op_cont_button.clicked.connect(self.on_cont_button_clicked)
        self.ui.reset_button.clicked.connect(self.on_reset_button_clicked)

        #下拉框选择器触发绑定
        self.ui.algorithm_combo.activated[str].connect(self.on_algorithm_changed)
        self.ui.order_combo.activated[str].connect(self.on_operation_order_changed)


        #触发一次重置按钮，整个界面预先重置
        self.ui.reset_button.click()

        #界面显示
        self.show()

#######################################################触发函数########################################################

    #算法选择下拉框触发
    def on_algorithm_changed(self):
        s=self.ui.algorithm_combo.currentText()
        if s=='FIFO':
            self.algorithm=self.FIFO
        else:
            self.algorithm=self.LRU

    #执行顺序下拉框触发
    def on_operation_order_changed(self):
        s=self.ui.order_combo.currentText()
        if s=='顺序':
            self.order=op_sequence()
        elif s=='跳步':
            self.order=op_skip()
        else:
            self.order=op_rand()

    #连续执行按钮触发
    def on_cont_button_clicked(self):
        #连续执行，每30ms点击一次单步执行按钮
        if self.counter<=TOTAL_INS:
            self.timer.start(30)
        else:
            self.timer.stop()
    
    #重置按钮触发
    def on_reset_button_clicked(self):
        #计时器停止
        self.timer.stop()
        #清空详细情况输出框
        self.ui.notification.clear()
        #重设计时器，缺页数，指令表格
        self.counter=0
        self.miss_page_sum=0
        self.ui.miss_times.setText("缺页次数:0")
        self.ui.miss_ratio.setText("缺页率:-")
        self.table.setRowCount(0)

        #重置页表，时间表
        for i in range(len(self.page_labels)):
            self.current_page[i]=NOPE
            self.fresh_time[i]=NOPE
            self.access_time[i]=NOPE

        #重设文本内容
        for i in range(0,len(self.page_labels)):
            self.page_visual[i].setText("")
            self.page_labels[i].setText("null")
        


    #单步按钮触发函数，核心操作
    def on_one_button_clicked(self):
        
        if self.counter==TOTAL_INS:
            return
        
        iter_ins=next(self.order)
        page=int(iter_ins/10)
        local_index=iter_ins%10
        
        #查找当前内存中的命中情况
        for i in range(len(self.current_page)):
            #命中时
            if self.current_page[i]==page:
                target_index=i
                self.access_time[i]=self.counter

                self.tableAddNew(str(iter_ins),str(page),"否","","")
                
                self.printMessage("第{}条指令,地址为第{}页首地址+{},命中,在内存块{}中找到该页面,\
                                    ".format(self.counter+1,page+1,local_index,i+1))
                
                self.page_visual_update(target_index,local_index)

                break    
        
        #未发生命中时,进行调页
        else:
            
            target_index=self.algorithm()
            old_page=self.current_page[target_index]
            old_page_string=str(old_page) if old_page != NOPE else ''
            
            self.miss_page_sum+=1

            self.page_swapping(target_index,page)

            self.tableAddNew(str(iter_ins),str(page),"是",old_page_string,str(page))

            self.printMessage("第{}条指令,地址为第{}页首地址+{},缺页,根据{}算法,{}将第{}页调入内存块{}\
                                ".format(   self.counter+1,
                                            page+1,
                                            local_index,
                                            "FIFO" if self.algorithm==self.FIFO else "LRU",
                                            "置换出内存块{}的第{}页,并".format(target_index+1,old_page+1) if old_page!=NOPE else "",
                                            page+1,target_index+1
                                    ))

            self.page_visual_update(target_index,local_index)

        #计数器+1
        self.counter += 1

        #实时更新缺页数，缺页率显示
        self.ui.miss_times.setText("缺页次数:{}".format(self.miss_page_sum))
        self.ui.miss_ratio.setText("缺页率:{}%".format(round((100*self.miss_page_sum/self.counter),3)))
        
#######################################################调页算法########################################################
    def FIFO(self):
        return min(list(enumerate(self.fresh_time)),key=lambda x: x[1])[0]
    
    def LRU(self):
        return min(list(enumerate(self.access_time)),key=lambda x: x[1])[0]

#######################################################换页方法########################################################
    def page_swapping(self,old_index,new):
        self.fresh_time[old_index]=self.counter
        self.access_time[old_index]=self.counter
        self.current_page[old_index]=new
        self.page_labels[old_index].setText("Page {}".format(new+1))
        self.page_labels[old_index].setVisible(True)


#######################################################显示更新方法####################################################
    def printMessage(self,string):
        self.log.append(string)
        self.cursor=self.log.textCursor()
        self.log.moveCursor(self.cursor.End)
        QtWidgets.QApplication.processEvents()

    def tableAddNew(self,c1,c2,c3,c4,c5):
        self.table.insertRow(self.counter)
        self.table.setItem(self.counter, 0, QtWidgets.QTableWidgetItem(c1))
        self.table.setItem(self.counter, 1, QtWidgets.QTableWidgetItem(c2))
        self.table.setItem(self.counter, 2, QtWidgets.QTableWidgetItem(c3))
        self.table.setItem(self.counter, 3, QtWidgets.QTableWidgetItem(c4))
        self.table.setItem(self.counter, 4, QtWidgets.QTableWidgetItem(c5))
    
    def page_visual_update(self,target_index,mark):
        visual=""
        for j in range(0,10):
            visual+=("×" if j==mark else "█")
        self.page_visual[target_index].setText(visual)        

#######################################################主函数####################################################
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget=MainWidget()
    sys.exit(app.exec())

        