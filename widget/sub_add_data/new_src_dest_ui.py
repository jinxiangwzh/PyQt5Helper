# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\new_src_dest.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_new_src_dest(object):
    def setupUi(self, new_src_dest):
        new_src_dest.setObjectName("new_src_dest")
        new_src_dest.resize(400, 135)
        new_src_dest.setMaximumSize(QtCore.QSize(400, 135))
        self.verticalLayout = QtWidgets.QVBoxLayout(new_src_dest)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.src_lb = QtWidgets.QLabel(new_src_dest)
        self.src_lb.setObjectName("src_lb")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.src_lb)
        self.dest_lb = QtWidgets.QLabel(new_src_dest)
        self.dest_lb.setObjectName("dest_lb")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dest_lb)
        self.src_le = QtWidgets.QLineEdit(new_src_dest)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.src_le.sizePolicy().hasHeightForWidth())
        self.src_le.setSizePolicy(sizePolicy)
        self.src_le.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.src_le.setReadOnly(True)
        self.src_le.setClearButtonEnabled(False)
        self.src_le.setObjectName("src_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.src_le)
        self.dest_le = QtWidgets.QLineEdit(new_src_dest)
        self.dest_le.setObjectName("dest_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dest_le)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_all_common_fmt_cb = QtWidgets.QCheckBox(new_src_dest)
        self.select_all_common_fmt_cb.setObjectName("select_all_common_fmt_cb")
        self.horizontalLayout.addWidget(self.select_all_common_fmt_cb)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ok_pb = QtWidgets.QPushButton(new_src_dest)
        self.ok_pb.setObjectName("ok_pb")
        self.horizontalLayout.addWidget(self.ok_pb)
        self.cancel_pb = QtWidgets.QPushButton(new_src_dest)
        self.cancel_pb.setObjectName("cancel_pb")
        self.horizontalLayout.addWidget(self.cancel_pb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(new_src_dest)
        QtCore.QMetaObject.connectSlotsByName(new_src_dest)

    def retranslateUi(self, new_src_dest):
        _translate = QtCore.QCoreApplication.translate
        new_src_dest.setWindowTitle(_translate("new_src_dest", "设置源和目标目录"))
        self.src_lb.setText(_translate("new_src_dest", "SRC："))
        self.dest_lb.setText(_translate("new_src_dest", "DEST："))
        self.dest_le.setText(_translate("new_src_dest", "."))
        self.dest_le.setPlaceholderText(_translate("new_src_dest", "请输入文件夹名字,用于存放在run-time时候的文件"))
        self.select_all_common_fmt_cb.setText(_translate("new_src_dest", "选择所有相同格式"))
        self.ok_pb.setText(_translate("new_src_dest", "确定"))
        self.cancel_pb.setText(_translate("new_src_dest", "取消"))
