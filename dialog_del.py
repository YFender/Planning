# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog_del.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_dialog_del(object):
    def setupUi(self, Form_dialog_del):
        Form_dialog_del.setObjectName("Form_dialog_del")
        Form_dialog_del.resize(400, 100)
        Form_dialog_del.setMinimumSize(QtCore.QSize(400, 100))
        Form_dialog_del.setMaximumSize(QtCore.QSize(400, 100))
        self.gridLayout = QtWidgets.QGridLayout(Form_dialog_del)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(Form_dialog_del)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.dialogButtonBox.setCenterButtons(True)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.gridLayout.addWidget(self.dialogButtonBox, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form_dialog_del)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.retranslateUi(Form_dialog_del)
        QtCore.QMetaObject.connectSlotsByName(Form_dialog_del)

    def retranslateUi(self, Form_dialog_del):
        _translate = QtCore.QCoreApplication.translate
        Form_dialog_del.setWindowTitle(_translate("Form_dialog_del", "Form"))
        self.label.setText(_translate("Form_dialog_del", "Вы действительно хотите удалить задачу?"))
