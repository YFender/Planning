# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\timer_stand.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

"""интерфейс стандартного таймера"""
from configparser import ConfigParser
from PyQt5 import QtCore, QtGui, QtWidgets
"""В этом файле прописан только интерфейс, вся логика находится в main.py"""
config = ConfigParser()
config.read("settings.ini")


class Ui_Form_timer(object):
    """функция обьявления всех обьектов в интерфейсе главного окна"""

    def setupUi(self, Form_timer):
        """обьявление главного окна и его характеристик"""

        Form_timer.setObjectName("Form_timer")
        Form_timer.setWindowModality(QtCore.Qt.NonModal)
        Form_timer.resize(480, 640)
        Form_timer.setMinimumSize(QtCore.QSize(480, 640))
        Form_timer.setMaximumSize(QtCore.QSize(480, 640))
        """lcdNumber отображает время таймера"""
        self.lcdNumber = QtWidgets.QLCDNumber(Form_timer)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 160, 481, 141))
        self.lcdNumber.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setObjectName("lcdNumber")
        """label - строчка с коротким текстом, в данном контексте используется просто как указатель что есть что"""

        self.label = QtWidgets.QLabel(Form_timer)
        self.label.setGeometry(QtCore.QRect(0, 180, 480, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        """horizontalLayoutWidget - виджет, созданный для баланса в расстоянии между обьектами по горизонтали"""

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form_timer)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 240, 461, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        """spinBox - виджет с выбором числа, в данном случае три виджета отвечают за выбор времени"""
        self.spinBox_hour = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.spinBox_hour.setFont(font)
        self.spinBox_hour.setMaximum(23)
        self.spinBox_hour.setObjectName("spinBox_hour")
        self.horizontalLayout.addWidget(self.spinBox_hour)
        """label_hour - строка-информатор для spinBox_hour с подсказкой что есть что, аналогичные есть и у spinBox_min и spinBox_sec"""
        self.label_hour = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_hour.setFont(font)
        self.label_hour.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_hour.setObjectName("label_hour")
        self.horizontalLayout.addWidget(self.label_hour)
        self.spinBox_min = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.spinBox_min.setFont(font)
        self.spinBox_min.setMaximum(59)
        self.spinBox_min.setObjectName("spinBox_min")
        self.horizontalLayout.addWidget(self.spinBox_min)
        self.label_min = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_min.setFont(font)
        self.label_min.setObjectName("label_min")
        self.horizontalLayout.addWidget(self.label_min)
        self.spinBox_sec = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.spinBox_sec.setFont(font)
        self.spinBox_sec.setMaximum(59)
        self.spinBox_sec.setObjectName("spinBox_sec")
        self.horizontalLayout.addWidget(self.spinBox_sec)
        self.label_sec = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_sec.setFont(font)
        self.label_sec.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sec.setObjectName("label_sec")
        self.horizontalLayout.addWidget(self.label_sec)
        """stop_button - клавиша для остановки таймера"""
        self.stop_button = QtWidgets.QPushButton(Form_timer)
        self.stop_button.setGeometry(QtCore.QRect(-10, 517, 500, 130))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")
        """start_button - клавиша для запуска таймера"""
        self.start_button = QtWidgets.QPushButton(Form_timer)
        self.start_button.setGeometry(QtCore.QRect(-10, 517, 500, 130))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")

        self.retranslateUi(Form_timer)
        QtCore.QMetaObject.connectSlotsByName(Form_timer)

    def retranslateUi(self, Form_timer):
        """присваивание текста определенным обьектам"""
        _translate = QtCore.QCoreApplication.translate
        Form_timer.setWindowTitle(_translate(
                "Form_timer", "Стандартный таймер"))
        self.label.setText(_translate("Form_timer", "Задать таймер"))
        self.label_hour.setText(_translate("Form_timer", "часов"))
        self.label_min.setText(_translate("Form_timer", "минут"))
        self.label_sec.setText(_translate("Form_timer", "секунд"))
        self.stop_button.setText(_translate("Form_timer", "Стоп"))
        self.start_button.setText(_translate("Form_timer", "Старт"))
