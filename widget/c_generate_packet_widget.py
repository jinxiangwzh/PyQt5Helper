#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         c_add_data_item_widget
# Description:
# Author:       Great Master
# Date:         2020/4/26
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import logging

from PyQt5.QtWidgets import QFrame, QFileDialog

from app_global import *
from widget.generate_packet_widget_ui import Ui_generate_packet_widget


class GeneratePacketWidget(QFrame):
    def __init__(self):
        super(GeneratePacketWidget, self).__init__()
        self.ui = Ui_generate_packet_widget()
        self.ui.setupUi(self)
        self.load_config_information()
        self._signal_init()

    def _signal_init(self):
        # debug
        self.ui.debug_cb.currentTextChanged.connect(self.on_debug_level_text_changed)
        self.ui.debug_gb.toggled.connect(self.on_debug_state_toggle)

        # strip
        self.ui.strip_cb.stateChanged.connect(self.on_strip_table_state_changed)
        # upx
        self.ui.no_upx_cb.stateChanged.connect(self.on_no_upx_state_changed)
        self.ui.upx_exclude_file_cb.stateChanged.connect(self.on_upx_exclude_state_changed)
        self.ui.upx_exclude_file_le.editingFinished.connect(self.on_upx_exclude_file_edit_finished)
        self.ui.add_upx_exclude_file_pb.clicked.connect(self.on_add_upx_exclude_file_button_clicked)
        self.ui.upx_exclude_file_le.textChanged.connect(self.on_upx_exclude_file_changed)
        # 选择文件
        self.ui.select_py_le.textChanged.connect(self.on_select_py_path_changed)
        self.ui.select_py_pb.clicked.connect(self.on_select_py_path_clicked)
        # .spec路径设置
        self.ui.spec_file_path_gp.toggled.connect(self.on_spec_file_path_state_toggled)
        self.ui.spec_file_path_le.textChanged.connect(self.on_spec_file_path_text_changed)
        self.ui.select_spec_file_path_pb.clicked.connect(self.on_select_spec_file_button_clicked)
        # app name 设置
        self.ui.app_name_gp.toggled.connect(self.on_app_name_state_toggled)
        self.ui.app_name_le.textChanged.connect(self.on_app_name_text_changed)

        # 生成文件的形式
        self.ui.one_file_rb.toggled.connect(self.on_file_format_state_toggled)
        # self.ui.one_dir_rb.toggled.connect(self.on_one_dir_state_toggled)  # 只需要一个就够了,不然一次进入两个

    def load_config_information(self):
        # debug
        self.ui.debug_gb.setChecked(int(get_debug_level_state()))
        self.ui.debug_cb.setCurrentText(get_debug_level())

        # strip
        self.ui.strip_cb.setChecked(int(get_strip_state()))
        # UPX
        self.ui.no_upx_cb.setChecked(int(get_no_upx_state()))
        self.ui.upx_exclude_file_cb.setChecked(int(get_exclude_upx_state()))
        self.ui.upx_exclude_file_le.setText(get_exclude_upx_file())

        # spec path
        state = get_spec_state()
        self.ui.spec_file_path_gp.setChecked(int(state))
        self.ui.spec_file_path_le.setText(get_spec_path())
        # app name
        state = get_app_name_state()
        self.ui.app_name_gp.setChecked(int(state))
        self.ui.app_name_le.setText(get_app_name())
        # file format
        fmt = get_build_format()
        if fmt == ONE_FILE_FORMAT:
            self.ui.one_file_rb.setChecked(True)
        else:
            self.ui.one_dir_rb.setChecked(True)

        # input file
        file_path = get_input_file_path()
        self.ui.select_py_le.setText(file_path)

    @staticmethod
    def on_debug_level_text_changed(level):
        logging.info("debug level changed:" + level)
        set_debug_level(level)

    @staticmethod
    def on_debug_state_toggle(state):
        logging.info("debug level state:" + str(state))
        set_debug_level_state(state)

    @staticmethod
    def on_strip_table_state_changed(state):
        logging.info("strip state:" + str(state))
        set_strip_state(state)

    @staticmethod
    def on_select_py_path_changed(text):
        set_input_file_path(text)

    @staticmethod
    def on_no_upx_state_changed(state):
        logging.info("no upx state:" + str(state))
        set_no_upx_state(state)

    @staticmethod
    def on_upx_exclude_state_changed(state):
        logging.info("upx exclude file state:" + str(state))
        set_exclude_upx_state(state)

    def on_upx_exclude_file_edit_finished(self):
        files = self.ui.upx_exclude_file_le.text()
        logging.info("exclude file edit finished:")
        # 再做一次检查,因为可能用户手动输入
        try:
            file_names = ""  # 多个名字之间分号隔开
            for file in files.split(';'):
                _, file_name = os.path.split(file)
                if file_name != '':
                    file_names += file_name + ';'
            self.ui.upx_exclude_file_le.setText(file_names)  # 在回调中设置,要注意会不会永无止境的循环
            logging.info("set upx exclude file to:" + file_names)

        except Exception as e:
            logging.error(e)

    def on_upx_exclude_file_changed(self, file_names):
        logging.info("exclude file changed:" + file_names)
        set_exclude_upx_file(file_names)

    def on_add_upx_exclude_file_button_clicked(self):
        try:
            def_path = get_input_file_path()
            file_path_list, fmt = QFileDialog.getOpenFileNames(self, '选择.py文件', def_path, "python (*.py)")
            file_names = ""  # 多个名字之间分号隔开
            for file in file_path_list:
                _, file_name = os.path.split(file)
                file_names += file_name + ';'
            self.ui.upx_exclude_file_le.insert(file_names)
        except Exception as e:
            logging.error(e)
            logging.error(str(e))

    def on_select_py_path_clicked(self):
        try:
            def_path = get_input_file_path()
            file_path, fmt = QFileDialog.getOpenFileName(self, '选择.py文件', def_path, "python (*.py)")
            self.ui.select_py_le.setText(file_path)
            set_input_file_path(file_path)
        except Exception as e:
            logging.error(e)

    @staticmethod
    def on_spec_file_path_state_toggled(state):
        set_spec_state(state)

    @staticmethod
    def on_spec_file_path_text_changed(text):
        set_spec_path(text)

    def on_select_spec_file_button_clicked(self):
        try:
            def_path = get_spec_path()
            file_path = QFileDialog.getExistingDirectory(self, '选择目录存放.spec', def_path)
            self.ui.spec_file_path_le.setText(file_path)
            set_spec_path(file_path)
        except Exception as e:
            logging.error(e)

    @staticmethod
    def on_app_name_state_toggled(state):
        set_app_name_state(state)

    @staticmethod
    def on_app_name_text_changed(name):
        set_app_name(name)

    @staticmethod
    def on_file_format_state_toggled(state):
        # 因为这个槽链接到one_file_rb,所以state为True，则为ONE_FILE_FORMAT
        if state:
            set_build_format(fmt=ONE_FILE_FORMAT)
        else:
            set_build_format(fmt=ONE_DIR_FORMAT)


