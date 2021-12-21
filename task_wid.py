# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\task_wid.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

"""виджет для создания задач"""
from configparser import ConfigParser
from PyQt5 import QtCore, QtGui, QtWidgets
"""В этом файле прописан только интерфейс, вся логика находится в main.py"""
config = ConfigParser()
config.read("settings.ini")


class Ui_Form_task(object):
    """функция обьявления всех обьектов в интерфейсе главного окна"""

    def setupUi(self, Form_task):
        """обьявление главного окна и его характеристик"""

        Form_task.setObjectName("Form_task")
        Form_task.resize(480, 640)
        Form_task.setMinimumSize(QtCore.QSize(480, 640))
        Form_task.setMaximumSize(QtCore.QSize(480, 640))
        """кнопка подтверждения создания задачи"""
        self.pushButton_create = QtWidgets.QPushButton(Form_task)
        self.pushButton_create.setGeometry(QtCore.QRect(-2, 541, 484, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        """horizontalLayoutWidget - виджет, созданный для баланса в расстоянии между обьектами по горизонтали"""
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form_task)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        """label_task в данном случае играет роль навигатора в программе, указывающий на строку ввода задачи, другие обьекты имеют аналогичные указатели"""
        self.label_task = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_task.setFont(font)
        self.label_task.setObjectName("label_task")
        self.horizontalLayout.addWidget(self.label_task)
        """lineEdit - виджет для ввода строки, lineEdit_task используется для ввода названия задачи"""
        self.lineEdit_task = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_task.setMaxLength(32)
        self.lineEdit_task.setObjectName("lineEdit_task")
        self.horizontalLayout.addWidget(self.lineEdit_task)
        self.formLayoutWidget = QtWidgets.QWidget(Form_task)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 110, 461, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_description = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_description.setFont(font)
        self.label_description.setObjectName("label_description")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_description)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.plainTextEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form_task)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(10, 360, 461, 32))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.horizontalLayoutWidget_2)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_2.addWidget(self.timeEdit)
        self.label_time = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout_2.addWidget(self.label_time)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form_task)
        self.horizontalLayoutWidget_3.setGeometry(
            QtCore.QRect(10, 390, 461, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_time = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_time.setFont(font)
        self.checkBox_time.setObjectName("checkBox_time")
        self.horizontalLayout_3.addWidget(self.checkBox_time)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form_task)
        self.horizontalLayoutWidget_4.setGeometry(
            QtCore.QRect(10, 450, 461, 32))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget_4)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.label_date = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.horizontalLayout_4.addWidget(self.label_date)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Form_task)
        self.horizontalLayoutWidget_5.setGeometry(
            QtCore.QRect(10, 480, 461, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_date = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_date.setFont(font)
        self.checkBox_date.setObjectName("checkBox_date")
        self.horizontalLayout_5.addWidget(self.checkBox_date)

        self.retranslateUi(Form_task)
        QtCore.QMetaObject.connectSlotsByName(Form_task)

    def retranslateUi(self, Form_task):
        """виджет для присваивания текста виджетам"""
        _translate = QtCore.QCoreApplication.translate
        Form_task.setWindowTitle(_translate("Form_task", "Form"))
        self.pushButton_create.setText(
            _translate("Form_task", "Создать задачу"))
        self.label_task.setText(_translate("Form_task", "Название задачи:"))
        self.label_description.setText(
            _translate("Form_task", "Описание задачи:"))
        self.label_time.setText(_translate("Form_task", "Время задачи"))
        self.checkBox_time.setText(_translate(
            "Form_task", "Без определенного времени"))
        self.label_date.setText(_translate("Form_task", "Дата задачи"))
        self.checkBox_date.setText(_translate(
            "Form_task", "Без определенной даты"))
