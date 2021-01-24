# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\edit_src_dest.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_src_dest(object):
    def setupUi(self, edit_src_dest):
        edit_src_dest.setObjectName("edit_src_dest")
        edit_src_dest.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(edit_src_dest)
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.detail_tb = QtWidgets.QTableWidget(edit_src_dest)
        self.detail_tb.setObjectName("detail_tb")
        self.detail_tb.setColumnCount(2)
        self.detail_tb.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.detail_tb.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail_tb.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_2.addWidget(self.detail_tb)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.delete_pb = QtWidgets.QPushButton(edit_src_dest)
        self.delete_pb.setObjectName("delete_pb")
        self.verticalLayout.addWidget(self.delete_pb)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_pb = QtWidgets.QPushButton(edit_src_dest)
        self.ok_pb.setObjectName("ok_pb")
        self.horizontalLayout.addWidget(self.ok_pb)
        self.cancel_pb = QtWidgets.QPushButton(edit_src_dest)
        self.cancel_pb.setObjectName("cancel_pb")
        self.horizontalLayout.addWidget(self.cancel_pb)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(edit_src_dest)
        QtCore.QMetaObject.connectSlotsByName(edit_src_dest)

    def retranslateUi(self, edit_src_dest):
        _translate = QtCore.QCoreApplication.translate
        edit_src_dest.setWindowTitle(_translate("edit_src_dest", "编辑SRC和DEST[*]"))
        item = self.detail_tb.horizontalHeaderItem(0)
        item.setText(_translate("edit_src_dest", "SRC"))
        item.setToolTip(_translate("edit_src_dest", "现在的目录/文件"))
        item = self.detail_tb.horizontalHeaderItem(1)
        item.setText(_translate("edit_src_dest", "DEST"))
        item.setToolTip(_translate("edit_src_dest", "打包后要访问的位置"))
        self.delete_pb.setText(_translate("edit_src_dest", "删除"))
        self.ok_pb.setText(_translate("edit_src_dest", "确定"))
        self.cancel_pb.setText(_translate("edit_src_dest", "取消"))
