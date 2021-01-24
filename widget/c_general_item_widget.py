#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         c_general_item_widget
# Description:  
# Author:       Great Master
# Date:         2020/4/26
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog

from app_global import get_dist_path, get_dist_state, set_dist_state, set_dist_path, set_work_path_state, set_work_path, \
    get_work_path, get_work_path_state, get_no_confirm_state, set_no_confirm_state, set_upx_search_path_state, \
    get_upx_search_path_state, get_upx_search_path, set_upx_search_path, set_not_support_unicode_state, \
    get_not_support_unicode_state, set_clean_cache_state, get_clean_cache_state, set_log_level, get_log_level
from widget.general_item_widget_ui import Ui_general_item_widget


class GeneralItemWidget(QWidget):
    def __init__(self):
        super(GeneralItemWidget, self).__init__()
        self.ui = Ui_general_item_widget()
        self.ui.setupUi(self)
        self.load_config_information()
        self._signal_init()

    def _signal_init(self):
        # --distpath DIR
        self.ui.dist_gb.toggled.connect(self.on_dist_group_box_toggled)
        self.ui.dist_path_le.textChanged.connect(self.on_dist_path_text_changed)
        self.ui.select_dist_path_pb.clicked.connect(self.on_select_dist_button_clicked)

        # --workpath WORKPATH
        self.ui.temp_work_path_gb.toggled.connect(self.on_work_path_group_box_toggled)
        self.ui.temp_work_path_le.textChanged.connect(self.on_work_path_text_changed)
        self.ui.select_temp_work_path_pb.clicked.connect(self.on_select_work_path_button_clicked)

        # -y, --noconfirm
        self.ui.no_confirm_rb.toggled.connect(self.on_no_confirm_rb_toggled)

        # --upx-dir UPX_DIR
        self.ui.upx_search_path_gb.toggled.connect(self.on_upx_group_box_toggled)
        self.ui.upx_search_path_le.textChanged.connect(self.on_upx_search_path_text_changed)
        self.ui.upx_search_path_pb.clicked.connect(self.on_select_upx_search_path_button_clicked)

        # --ascii
        self.ui.unicode_not_support_rb.toggled.connect(self.on_unicode_not_support_toggled)

        # --clean
        self.ui.clean_cache_cb.stateChanged.connect(self.on_clean_cache_checked)

        # --log-level LEVEL
        self.ui.log_level_cb.currentTextChanged.connect(self.on_log_level_text_changed)

    def load_config_information(self):
        try:
            # --distpath DIR
            self.ui.dist_path_le.setText(get_dist_path())
            state = get_dist_state()
            self.ui.dist_gb.setChecked(int(state))

            # --workpath WORKPATH
            self.ui.temp_work_path_le.setText(get_work_path())
            state = get_work_path_state()
            self.ui.temp_work_path_gb.setChecked(int(state))

            # -y, --noconfirm
            state = get_no_confirm_state()
            self.ui.no_confirm_rb.setChecked(int(state))

            # --upx-dir UPX_DIR
            state = get_upx_search_path_state()
            self.ui.upx_search_path_gb.setChecked(int(state))
            self.ui.upx_search_path_le.setText(get_upx_search_path())

            # --ascii
            state = get_not_support_unicode_state()
            self.ui.unicode_not_support_rb.setChecked(int(state))

            # --clean
            state = get_clean_cache_state()
            self.ui.clean_cache_cb.setChecked(int(state))

            # --log-level LEVEL
            level = get_log_level()
            self.ui.log_level_cb.setCurrentText(level)

        except Exception as e:
            logging.error("general load config:" + str(e))

    @staticmethod
    def on_dist_group_box_toggled(state):
        set_dist_state(state)

    @staticmethod
    def on_dist_path_text_changed(path):
        logging.debug("dist path changed to " + path)
        set_dist_path(path)

    def on_select_dist_button_clicked(self):
        try:
            def_path = get_dist_path()
            file_path = QFileDialog.getExistingDirectory(self, "选择打包文件存放目录", def_path)
            self.ui.dist_path_le.setText(file_path)
            set_dist_path(file_path)
        except Exception as e:
            logging.error(str(e))

    # --workpath
    @staticmethod
    def on_work_path_group_box_toggled(state):
        set_work_path_state(state)

    @staticmethod
    def on_work_path_text_changed(path):
        logging.debug("temp work path changed to " + path)
        set_work_path(path)

    def on_select_work_path_button_clicked(self):
        try:
            def_path = get_work_path()
            file_path = QFileDialog.getExistingDirectory(self, "选择临时工作目录", def_path)
            self.ui.temp_work_path_le.setText(file_path)
            set_work_path(file_path)
        except Exception as e:
            logging.error(str(e))

    # --noconfirm
    @staticmethod
    def on_no_confirm_rb_toggled(state):
        set_no_confirm_state(state)

    # --upx-dir UPX_DIR
    @staticmethod
    def on_upx_group_box_toggled(state):
        set_upx_search_path_state(state)

    @staticmethod
    def on_upx_search_path_text_changed(path):
        logging.info("upx search path changed to:" + path)
        set_upx_search_path(path)

    def on_select_upx_search_path_button_clicked(self):
        try:
            def_path = get_dist_path()
            file_path = QFileDialog.getExistingDirectory(self, "选择UPX搜索目录", def_path)
            self.ui.upx_search_path_le.setText(file_path)
            logging.info("select upx search path" + file_path)
            set_upx_search_path(file_path)
        except Exception as e:
            logging.error(str(e))

    # --ascii
    @staticmethod
    def on_unicode_not_support_toggled(state):
        set_not_support_unicode_state(state)

    # --clean
    @staticmethod
    def on_clean_cache_checked(state):
        if state == Qt.Checked:
            set_clean_cache_state(True)
        else:
            set_clean_cache_state(False)

    # --log-level LEVEL
    @staticmethod
    def on_log_level_text_changed(level):
        set_log_level(level)



