# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'os2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,QtWidgets


class Ui_QWidget(object):
    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget")
        QWidget.resize(819, 826)
        self.title = QtWidgets.QLabel(QWidget)
        self.title.setGeometry(QtCore.QRect(20, 10, 400, 41))
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setScaledContents(True)
        self.title.setObjectName("title")
        self.title.setStyleSheet("font-family:Microsoft YaHei;font-size: 24px;font-weight:bold;")
        self.ins_table = QtWidgets.QTableWidget(QWidget)
        self.ins_table.setGeometry(QtCore.QRect(20, 110, 781, 271))
        self.ins_table.setObjectName("ins_table")
        self.ins_table.setColumnCount(6)
        self.ins_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ins_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ins_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ins_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ins_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ins_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ins_table.setHorizontalHeaderItem(5, item)
        self.table_label = QtWidgets.QLabel(QWidget)
        self.table_label.setGeometry(QtCore.QRect(20, 60, 300, 31))
        self.table_label.setObjectName("table_label")
        self.table_label.setStyleSheet("font-family:Microsoft YaHei;font-size: 18px;")
        self.layoutWidget = QtWidgets.QWidget(QWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 70, 184, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_2 = QtWidgets.QLabel(self.layoutWidget)
        self.title_2.setTextFormat(QtCore.Qt.RichText)
        self.title_2.setScaledContents(True)
        self.title_2.setObjectName("title_2")
        self.horizontalLayout.addWidget(self.title_2)
        self.algorithm_combo = QtWidgets.QComboBox(self.layoutWidget)
        self.algorithm_combo.setObjectName("algorithm_combo")
        self.algorithm_combo.addItem("")
        self.algorithm_combo.addItem("")
        self.horizontalLayout.addWidget(self.algorithm_combo)
        self.layoutWidget1 = QtWidgets.QWidget(QWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(610, 70, 184, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.order_combo = QtWidgets.QComboBox(self.layoutWidget1)
        self.order_combo.setObjectName("order_combo")
        self.order_combo.addItem("")
        self.order_combo.addItem("")
        self.order_combo.addItem("")
        self.horizontalLayout_2.addWidget(self.order_combo)
        self.layoutWidget2 = QtWidgets.QWidget(QWidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 390, 781, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.op_one_button = QtWidgets.QPushButton(self.layoutWidget2)
        self.op_one_button.setObjectName("op_one_button")
        self.horizontalLayout_3.addWidget(self.op_one_button)
        self.op_cont_button = QtWidgets.QPushButton(self.layoutWidget2)
        self.op_cont_button.setObjectName("op_cont_button")
        self.horizontalLayout_3.addWidget(self.op_cont_button)
        self.reset_button = QtWidgets.QPushButton(self.layoutWidget2)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout_3.addWidget(self.reset_button)
        self.miss_times = QtWidgets.QLabel(QWidget)
        self.miss_times.setGeometry(QtCore.QRect(640, 700, 300, 32))
        self.miss_times.setObjectName("miss_times")
        self.miss_times.setStyleSheet("font-family:Microsoft YaHei;font-size: 18px;")
        self.miss_ratio = QtWidgets.QLabel(QWidget)
        self.miss_ratio.setGeometry(QtCore.QRect(640, 740, 300, 32))
        self.miss_ratio.setObjectName("miss_ratio")
        self.miss_ratio.setStyleSheet("font-family:Microsoft YaHei;font-size: 18px;")
        self.notification = QtWidgets.QTextBrowser(QWidget)
        self.notification.setGeometry(QtCore.QRect(20, 510, 781, 151))
        self.notification.setObjectName("notification")
        self.note = QtWidgets.QLabel(QWidget)
        self.note.setGeometry(QtCore.QRect(20, 460, 400, 31))
        self.note.setObjectName("note")
        self.note.setStyleSheet("font-family:Microsoft YaHei;font-size: 18px;")
        self.widget = QtWidgets.QWidget(QWidget)
        self.widget.setGeometry(QtCore.QRect(20, 680, 601, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.block_5 = QtWidgets.QLabel(self.widget)
        self.block_5.setObjectName("block_5")
        self.horizontalLayout_4.addWidget(self.block_5)
        self.page_text_1 = QtWidgets.QLabel(self.widget)
        self.page_text_1.setObjectName("page_text_1")
        self.horizontalLayout_4.addWidget(self.page_text_1)
        self.visual_1 = QtWidgets.QLabel(self.widget)
        self.visual_1.setObjectName("visual_1")
        self.horizontalLayout_4.addWidget(self.visual_1)
        self.widget1 = QtWidgets.QWidget(QWidget)
        self.widget1.setGeometry(QtCore.QRect(20, 710, 601, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.block_2 = QtWidgets.QLabel(self.widget1)
        self.block_2.setObjectName("block_2")
        self.horizontalLayout_5.addWidget(self.block_2)
        self.page_text_2 = QtWidgets.QLabel(self.widget1)
        self.page_text_2.setObjectName("page_text_2")
        self.horizontalLayout_5.addWidget(self.page_text_2)
        self.visual_2 = QtWidgets.QLabel(self.widget1)
        self.visual_2.setObjectName("visual_2")
        self.horizontalLayout_5.addWidget(self.visual_2)
        self.widget2 = QtWidgets.QWidget(QWidget)
        self.widget2.setGeometry(QtCore.QRect(20, 740, 601, 21))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.block_3 = QtWidgets.QLabel(self.widget2)
        self.block_3.setObjectName("block_3")
        self.horizontalLayout_6.addWidget(self.block_3)
        self.page_text_3 = QtWidgets.QLabel(self.widget2)
        self.page_text_3.setObjectName("page_text_3")
        self.horizontalLayout_6.addWidget(self.page_text_3)
        self.visual_3 = QtWidgets.QLabel(self.widget2)
        self.visual_3.setObjectName("visual_3")
        self.horizontalLayout_6.addWidget(self.visual_3)
        self.widget3 = QtWidgets.QWidget(QWidget)
        self.widget3.setGeometry(QtCore.QRect(20, 770, 601, 21))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.block_4 = QtWidgets.QLabel(self.widget3)
        self.block_4.setObjectName("block_4")
        self.horizontalLayout_7.addWidget(self.block_4)
        self.page_text_4 = QtWidgets.QLabel(self.widget3)
        self.page_text_4.setObjectName("page_text_4")
        self.horizontalLayout_7.addWidget(self.page_text_4)
        self.visual_4 = QtWidgets.QLabel(self.widget3)
        self.visual_4.setObjectName("visual_4")
        self.horizontalLayout_7.addWidget(self.visual_4)

        self.retranslateUi(QWidget)
        QtCore.QMetaObject.connectSlotsByName(QWidget)
        QWidget.setTabOrder(self.order_combo, self.algorithm_combo)
        QWidget.setTabOrder(self.algorithm_combo, self.ins_table)
        QWidget.setTabOrder(self.ins_table, self.op_one_button)
        QWidget.setTabOrder(self.op_one_button, self.op_cont_button)
        QWidget.setTabOrder(self.op_cont_button, self.reset_button)


    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        QWidget.setWindowTitle(_translate("QWidget", "Form"))
        self.title.setText(_translate("QWidget", "内存管理:请求调页存储方式模拟器"))
        item = self.ins_table.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "序号"))
        item = self.ins_table.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "地址"))
        item = self.ins_table.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "地址"))
        item = self.ins_table.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "所在页"))
        item = self.ins_table.horizontalHeaderItem(4)
        item.setText(_translate("QWidget", "缺页情况"))
        item = self.ins_table.horizontalHeaderItem(5)
        item.setText(_translate("QWidget", "换入页"))
        self.table_label.setText(_translate("QWidget", "调页情况表"))
        self.title_2.setText(_translate("QWidget", "请选择调页算法:"))
        self.algorithm_combo.setItemText(0, _translate("QWidget", "FIFO"))
        self.algorithm_combo.setItemText(1, _translate("QWidget", "LRU"))
        self.label.setText(_translate("QWidget", "请选择执行顺序:"))
        self.order_combo.setItemText(1, _translate("QWidget", "顺序"))
        self.order_combo.setItemText(0, _translate("QWidget", "跳步"))
        self.order_combo.setItemText(2, _translate("QWidget", "随机"))
        self.op_one_button.setText(_translate("QWidget", "单步执行"))
        self.op_cont_button.setText(_translate("QWidget", "连续执行"))
        self.reset_button.setText(_translate("QWidget", "重置"))
        self.miss_times.setText(_translate("QWidget", "缺页次数:"))
        self.miss_ratio.setText(_translate("QWidget", "缺页率:"))
        self.note.setText(_translate("QWidget", "调页情况详细说明"))
        self.block_5.setText(_translate("QWidget", "内存块1"))
        self.page_text_1.setText(_translate("QWidget", "Page 1"))
        self.visual_1.setText(_translate("QWidget", ""))
        self.block_2.setText(_translate("QWidget", "内存块2"))
        self.page_text_2.setText(_translate("QWidget", "Page 2"))
        self.visual_2.setText(_translate("QWidget", ""))
        self.block_3.setText(_translate("QWidget", "内存块3"))
        self.page_text_3.setText(_translate("QWidget", "Page 3"))
        self.visual_3.setText(_translate("QWidget", ""))
        self.block_4.setText(_translate("QWidget", "内存块4"))
        self.page_text_4.setText(_translate("QWidget", "Page 4"))
        self.visual_4.setText(_translate("QWidget", ""))

