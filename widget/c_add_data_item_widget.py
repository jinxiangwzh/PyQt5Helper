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

from PyQt5.QtWidgets import QFrame

from app_global import *
from widget.add_data_widget_ui import Ui_add_data_widget
from widget.sub_add_data.c_edit_src_dest import EditSrcDest
from widget.sub_add_data.c_new_src_dest import NewSrcDestWidget


class AddDataItemWidget(QFrame):
    def __init__(self):
        super(AddDataItemWidget, self).__init__()
        self.new_widget = None  # 新增子窗口
        self.edit_widget = None  # 编辑子窗口
        self.ui = Ui_add_data_widget()
        self.ui.setupUi(self)
        self.load_config_information()
        self._signal_init()

    def _signal_init(self):
        # 添加非二进制文件
        self.ui.add_non_binary_gb.toggled.connect(self.on_add_non_binary_file_state_changed)
        self.ui.add_non_binary_le.textChanged.connect(self.on_add_non_binary_text_changed)
        self.ui.add_non_binary_pb.clicked.connect(self.on_add_non_binary_button_clicked)
        self.ui.edit_non_binary_pb.clicked.connect(self.edit_non_binary_button_clicked)
        # 添加二进制文件
        self.ui.add_binary_gb.toggled.connect(self.on_add_binary_file_state_changed)
        self.ui.add_binary_le.textChanged.connect(self.on_add_binary_text_changed)
        self.ui.add_binary_pb.clicked.connect(self.on_add_binary_button_clicked)
        self.ui.edit_binary_pb.clicked.connect(self.edit_binary_button_clicked)
        # import搜索路径
        self.ui.p_cmd_gb.toggled.connect(self.on_p_cmd_state_changed)
        self.ui.p_cmd_le.textChanged.connect(self.on_p_cmd_text_changed)
        # hidden-import
        self.ui.hidden_import_gb.toggled.connect(self.on_hidden_import_state_changed)
        self.ui.hidden_import_le.textChanged.connect(self.on_hidden_import_text_changed)
        # additional hook
        self.ui.additional_hook_gb.toggled.connect(self.on_additional_hook_state_changed)
        self.ui.additional_hook_le.textChanged.connect(self.on_additional_hook_text_changed)

        # runtime hook
        self.ui.runtime_hook_gb.toggled.connect(self.on_runtime_hook_state_changed)
        self.ui.runtime_hook_le.textChanged.connect(self.on_runtime_hook_text_changed)

        # exclude module
        self.ui.exclude_module_gb.toggled.connect(self.on_exclude_module_state_changed)
        self.ui.exclude_module_le.textChanged.connect(self.on_exclude_module_text_changed)

        # --key
        self.ui.encrypt_gb.toggled.connect(self.on_encrypt_state_changed)
        self.ui.encrypt_le.textChanged.connect(self.on_encrypt_text_changed)

    def load_config_information(self):
        try:
            # --add-data <SRC;DEST or SRC:DEST>
            self.ui.add_non_binary_le.setText(get_non_binary_path())
            state = get_non_binary_state()
            self.ui.add_non_binary_gb.setChecked(int(state))

            # --add-binary <SRC;DEST or SRC:DEST>
            self.ui.add_binary_le.setText(get_binary_path())
            state = get_binary_state()
            self.ui.add_binary_gb.setChecked(int(state))

            # -p
            self.ui.p_cmd_le.setText(get_import_search_path())
            state = get_import_search_state()
            self.ui.p_cmd_gb.setChecked(int(state))

            # --hidden-import
            self.ui.hidden_import_le.setText(get_hidden_import_package())
            state = get_hidden_import_state()
            self.ui.hidden_import_gb.setChecked(int(state))

            # additional_hooks_dir
            self.ui.additional_hook_le.setText(get_additional_hook())
            state = get_additional_hook_state()
            self.ui.additional_hook_gb.setChecked(int(state))

            # runtime hook
            self.ui.runtime_hook_le.setText(get_runtime_hook())
            state = get_runtime_hook_state()
            self.ui.runtime_hook_gb.setChecked(int(state))

            # exclude module
            self.ui.exclude_module_le.setText(get_exclude_module())
            state = get_exclude_module_state()
            self.ui.exclude_module_gb.setChecked(int(state))

            # encrypt
            self.ui.encrypt_le.setText(get_encrypt())
            state = get_encrypt_state()
            self.ui.encrypt_gb.setChecked(int(state))
        except Exception as e:
            logging.error("What to bundle, where to search load config:" + str(e))

    @staticmethod
    def on_add_non_binary_file_state_changed(state):
        logging.info("--add-data cmd state changed:" + str(state))
        set_non_binary_state(state)

    @staticmethod
    def on_add_non_binary_text_changed(path_str):
        logging.info("--add-data text changed:" + path_str)
        set_non_binary_path(path_str)

    def on_add_non_binary_button_clicked(self):
        try:
            self.new_widget = NewSrcDestWidget(self.ui.add_non_binary_le)
            self.new_widget.show()
        except Exception as e:
            logging.error(str(e))

    def edit_non_binary_button_clicked(self):
        try:
            self.edit_widget = EditSrcDest(self.ui.add_non_binary_le)
            self.edit_widget.show()
        except Exception as e:
            logging.error(str(e))

    @staticmethod
    def on_add_binary_file_state_changed(state):
        logging.info("--add-binary cmd state changed:" + str(state))
        set_binary_state(state)

    @staticmethod
    def on_add_binary_text_changed(path_str):
        logging.info("on add binary_text_changed:" + path_str)
        set_binary_path(path_str)

    def on_add_binary_button_clicked(self):
        try:
            self.new_widget = NewSrcDestWidget(self.ui.add_binary_le)
            self.new_widget.show()
        except Exception as e:
            logging.error(str(e))

    def edit_binary_button_clicked(self):
        try:
            self.edit_widget = EditSrcDest(self.ui.add_binary_le)
            self.edit_widget.show()
        except Exception as e:
            logging.error(str(e))

    # p cmd
    @staticmethod
    def on_p_cmd_state_changed(state):
        logging.info("-p cmd state changed:" + str(state))
        set_import_search_state(state)

    @staticmethod
    def on_p_cmd_text_changed(text):
        # TODO 好像路径需要用""包起来
        logging.info("-p cmd text changed:" + text)
        set_import_search_path(text)

    @staticmethod
    def on_hidden_import_state_changed(state):
        logging.info("-hidden import state changed:" + str(state))
        set_hidden_import_state(state)

    @staticmethod
    def on_hidden_import_text_changed(text):
        logging.info("-hidden import text changed:" + text)
        set_hidden_import_package(text)

    @staticmethod
    def on_additional_hook_state_changed(state):
        logging.info("additional hook state changed:" + str(state))
        set_additional_hook_state(state)

    @staticmethod
    def on_additional_hook_text_changed(text):
        logging.info("additional hook text changed:" + text)
        set_additional_hook(text)

    @staticmethod
    def on_runtime_hook_state_changed(state):
        logging.info("runtime hook state changed:" + str(state))
        set_runtime_hook_state(state)

    @staticmethod
    def on_runtime_hook_text_changed(text):
        logging.info("runtime hook text changed:" + text)
        set_runtime_hook(text)

    @staticmethod
    def on_exclude_module_state_changed(state):
        logging.info("exclude module state changed:" + str(state))
        set_exclude_module_state(state)

    @staticmethod
    def on_exclude_module_text_changed(text):
        logging.info("exclude module text changed:" + text)
        set_exclude_module(text)

    @staticmethod
    def on_encrypt_state_changed(state):
        logging.info("encrypt state changed:" + str(state))
        set_encrypt_state(state)

    @staticmethod
    def on_encrypt_text_changed(text):
        logging.info("encrypt text changed:" + text)
        set_encrypt(text)
