# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\build_process_info.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_build_process_widget(object):
    def setupUi(self, build_process_widget):
        build_process_widget.setObjectName("build_process_widget")
        build_process_widget.resize(550, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/left_menu/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        build_process_widget.setWindowIcon(icon)
        build_process_widget.setWindowOpacity(1.0)
        self.verticalLayout = QtWidgets.QVBoxLayout(build_process_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.build_process_te = QtWidgets.QTextEdit(build_process_widget)
        self.build_process_te.setStyleSheet("background-color: black;\n"
"color:white;")
        self.build_process_te.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.build_process_te.setPlaceholderText("")
        self.build_process_te.setObjectName("build_process_te")
        self.verticalLayout.addWidget(self.build_process_te)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(build_process_widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(build_process_widget)
        QtCore.QMetaObject.connectSlotsByName(build_process_widget)

    def retranslateUi(self, build_process_widget):
        _translate = QtCore.QCoreApplication.translate
        build_process_widget.setWindowTitle(_translate("build_process_widget", "build信息"))
        self.pushButton.setText(_translate("build_process_widget", "强制取消"))
import resource.resource_rc
