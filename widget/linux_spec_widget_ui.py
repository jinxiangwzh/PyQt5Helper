# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\linux_spec_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_linux_spec_widget(object):
    def setupUi(self, linux_spec_widget):
        linux_spec_widget.setObjectName("linux_spec_widget")
        linux_spec_widget.resize(400, 300)
        self.label = QtWidgets.QLabel(linux_spec_widget)
        self.label.setGeometry(QtCore.QRect(60, 90, 321, 111))
        self.label.setObjectName("label")

        self.retranslateUi(linux_spec_widget)
        QtCore.QMetaObject.connectSlotsByName(linux_spec_widget)

    def retranslateUi(self, linux_spec_widget):
        _translate = QtCore.QCoreApplication.translate
        linux_spec_widget.setWindowTitle(_translate("linux_spec_widget", "Form"))
        self.label.setText(_translate("linux_spec_widget", "<html><head/><body><p><span style=\" font-size:36pt; color:#0055ff;\">linux版本用</span></p></body></html>"))
