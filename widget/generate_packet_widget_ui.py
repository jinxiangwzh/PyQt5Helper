# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\generate_packet_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_generate_packet_widget(object):
    def setupUi(self, generate_packet_widget):
        generate_packet_widget.setObjectName("generate_packet_widget")
        generate_packet_widget.resize(566, 470)
        self.verticalLayout = QtWidgets.QVBoxLayout(generate_packet_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.debug_gb = QtWidgets.QGroupBox(generate_packet_widget)
        self.debug_gb.setCheckable(True)
        self.debug_gb.setObjectName("debug_gb")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.debug_gb)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.debug_cb = QtWidgets.QComboBox(self.debug_gb)
        self.debug_cb.setObjectName("debug_cb")
        self.debug_cb.addItem("")
        self.debug_cb.addItem("")
        self.debug_cb.addItem("")
        self.debug_cb.addItem("")
        self.horizontalLayout_5.addWidget(self.debug_cb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addWidget(self.debug_gb)
        self.strip_gb = QtWidgets.QGroupBox(generate_packet_widget)
        self.strip_gb.setObjectName("strip_gb")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.strip_gb)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.strip_cb = QtWidgets.QCheckBox(self.strip_gb)
        self.strip_cb.setObjectName("strip_cb")
        self.horizontalLayout_7.addWidget(self.strip_cb)
        self.verticalLayout.addWidget(self.strip_gb)
        self.upx_gb = QtWidgets.QGroupBox(generate_packet_widget)
        self.upx_gb.setObjectName("upx_gb")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.upx_gb)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.no_upx_cb = QtWidgets.QCheckBox(self.upx_gb)
        self.no_upx_cb.setObjectName("no_upx_cb")
        self.horizontalLayout_6.addWidget(self.no_upx_cb)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.upx_exclude_file_cb = QtWidgets.QCheckBox(self.upx_gb)
        self.upx_exclude_file_cb.setObjectName("upx_exclude_file_cb")
        self.horizontalLayout_8.addWidget(self.upx_exclude_file_cb)
        self.upx_exclude_file_le = QtWidgets.QLineEdit(self.upx_gb)
        self.upx_exclude_file_le.setObjectName("upx_exclude_file_le")
        self.horizontalLayout_8.addWidget(self.upx_exclude_file_le)
        self.add_upx_exclude_file_pb = QtWidgets.QPushButton(self.upx_gb)
        self.add_upx_exclude_file_pb.setObjectName("add_upx_exclude_file_pb")
        self.horizontalLayout_8.addWidget(self.add_upx_exclude_file_pb)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.upx_gb)
        self.spec_file_path_gp = QtWidgets.QGroupBox(generate_packet_widget)
        self.spec_file_path_gp.setCheckable(True)
        self.spec_file_path_gp.setChecked(False)
        self.spec_file_path_gp.setObjectName("spec_file_path_gp")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.spec_file_path_gp)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.spec_file_path_str_lb = QtWidgets.QLabel(self.spec_file_path_gp)
        self.spec_file_path_str_lb.setObjectName("spec_file_path_str_lb")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.spec_file_path_str_lb)
        self.spec_file_path_le = QtWidgets.QLineEdit(self.spec_file_path_gp)
        self.spec_file_path_le.setObjectName("spec_file_path_le")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spec_file_path_le)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        self.select_spec_file_path_pb = QtWidgets.QPushButton(self.spec_file_path_gp)
        self.select_spec_file_path_pb.setObjectName("select_spec_file_path_pb")
        self.horizontalLayout_3.addWidget(self.select_spec_file_path_pb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.spec_file_path_gp)
        self.app_name_gp = QtWidgets.QGroupBox(generate_packet_widget)
        self.app_name_gp.setCheckable(True)
        self.app_name_gp.setChecked(False)
        self.app_name_gp.setObjectName("app_name_gp")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.app_name_gp)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.app_name_str_lb = QtWidgets.QLabel(self.app_name_gp)
        self.app_name_str_lb.setObjectName("app_name_str_lb")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.app_name_str_lb)
        self.app_name_le = QtWidgets.QLineEdit(self.app_name_gp)
        self.app_name_le.setObjectName("app_name_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.app_name_le)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.app_name_gp)
        self.packet_format_gp = QtWidgets.QGroupBox(generate_packet_widget)
        self.packet_format_gp.setObjectName("packet_format_gp")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.packet_format_gp)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.one_file_rb = QtWidgets.QRadioButton(self.packet_format_gp)
        self.one_file_rb.setObjectName("one_file_rb")
        self.horizontalLayout_2.addWidget(self.one_file_rb)
        self.one_dir_rb = QtWidgets.QRadioButton(self.packet_format_gp)
        self.one_dir_rb.setChecked(True)
        self.one_dir_rb.setObjectName("one_dir_rb")
        self.horizontalLayout_2.addWidget(self.one_dir_rb)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.packet_format_gp)
        self.groupBox_5 = QtWidgets.QGroupBox(generate_packet_widget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.select_py_path_str_lb = QtWidgets.QLabel(self.groupBox_5)
        self.select_py_path_str_lb.setObjectName("select_py_path_str_lb")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.select_py_path_str_lb)
        self.select_py_le = QtWidgets.QLineEdit(self.groupBox_5)
        self.select_py_le.setObjectName("select_py_le")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.select_py_le)
        self.horizontalLayout_4.addLayout(self.formLayout_3)
        self.select_py_pb = QtWidgets.QPushButton(self.groupBox_5)
        self.select_py_pb.setObjectName("select_py_pb")
        self.horizontalLayout_4.addWidget(self.select_py_pb)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.groupBox_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(generate_packet_widget)
        QtCore.QMetaObject.connectSlotsByName(generate_packet_widget)

    def retranslateUi(self, generate_packet_widget):
        _translate = QtCore.QCoreApplication.translate
        generate_packet_widget.setWindowTitle(_translate("generate_packet_widget", "Form"))
        self.debug_gb.setToolTip(_translate("generate_packet_widget", "<html><head/><body><p>Provide assistance with debugging a frozen application. This argument may be provided multiple times to select several of the following options. </p></body></html>"))
        self.debug_gb.setTitle(_translate("generate_packet_widget", "调试"))
        self.debug_cb.setItemText(0, _translate("generate_packet_widget", "all"))
        self.debug_cb.setItemText(1, _translate("generate_packet_widget", "imports"))
        self.debug_cb.setItemText(2, _translate("generate_packet_widget", "bootloader"))
        self.debug_cb.setItemText(3, _translate("generate_packet_widget", "noarchive"))
        self.strip_gb.setTitle(_translate("generate_packet_widget", "符号表带"))
        self.strip_cb.setToolTip(_translate("generate_packet_widget", "<html><head/><body><p>Apply a symbol-table strip to the executable and shared libs (<span style=\" color:#ff0000;\">not recommended</span></p><p><span style=\" color:#ff0000;\">for Windows</span>)</p></body></html>"))
        self.strip_cb.setText(_translate("generate_packet_widget", "应用符号表带"))
        self.upx_gb.setTitle(_translate("generate_packet_widget", "UPX"))
        self.no_upx_cb.setText(_translate("generate_packet_widget", "no_upx"))
        self.upx_exclude_file_cb.setToolTip(_translate("generate_packet_widget", "<html><head/><body><p>Prevent a binary from being compressed when using upx. This is typically used<br/>if upx corrupts certain binaries during compression. <span style=\" color:#ff0000;\">FILE is the filename of the<br/>binary without path</span>. This option can be used multiple times. </p></body></html>"))
        self.upx_exclude_file_cb.setText(_translate("generate_packet_widget", "排除文件"))
        self.upx_exclude_file_le.setPlaceholderText(_translate("generate_packet_widget", "输入文件名,多个文件之间分号隔开"))
        self.add_upx_exclude_file_pb.setText(_translate("generate_packet_widget", "添加文件"))
        self.spec_file_path_gp.setTitle(_translate("generate_packet_widget", "自定义.spec文件路径"))
        self.spec_file_path_str_lb.setText(_translate("generate_packet_widget", "路径:"))
        self.spec_file_path_le.setPlaceholderText(_translate("generate_packet_widget", "默认:当前目录"))
        self.select_spec_file_path_pb.setText(_translate("generate_packet_widget", "选择"))
        self.app_name_gp.setTitle(_translate("generate_packet_widget", "自定义生成文件名"))
        self.app_name_str_lb.setText(_translate("generate_packet_widget", "名字:"))
        self.packet_format_gp.setTitle(_translate("generate_packet_widget", "生成文件形式"))
        self.one_file_rb.setText(_translate("generate_packet_widget", "单个执行文件"))
        self.one_dir_rb.setText(_translate("generate_packet_widget", "文件夹"))
        self.groupBox_5.setTitle(_translate("generate_packet_widget", "输入文件"))
        self.select_py_path_str_lb.setText(_translate("generate_packet_widget", "路径:"))
        self.select_py_le.setPlaceholderText(_translate("generate_packet_widget", "必选"))
        self.select_py_pb.setText(_translate("generate_packet_widget", "选择"))
