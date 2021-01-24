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
import os
import threading

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QLineEdit

from app_global import cmd_path_sep
from widget.sub_add_data.new_src_dest_ui import Ui_new_src_dest


class NewSrcDestWidget(QWidget):
    def __init__(self, parent_le):
        super(NewSrcDestWidget, self).__init__()
        # 实例化后先保存,点击取消后恢复
        self.src_history = ''
        self.dest_history = ''

        # 对选择的文件做两种预处理,用处不同
        self.fmt_file_group: dict = {}  # 格式为key, value为文件路径，用于选择目录下所有相同格式
        # 用于最终命令,和父界面；内容为 文件名:路径,如 'src/README.txt:.'， 多个之间分号隔开
        self.single_file_group = ''  # 和下面的由checkbox决定用哪个
        # 文件夹下所有相同格式
        self.common_fmt_group = ''
        self.raw_files = ''  # 原始的，没有格式修改的文件

        self.parent_le: QLineEdit = parent_le
        self.ui = Ui_new_src_dest()
        self.ui.setupUi(self)
        self._custom_init()
        self._signal_init()

    def _custom_init(self):
        self.setWindowModality(Qt.ApplicationModal)
        hl = QHBoxLayout()
        hl.setContentsMargins(0, 0, 0, 0)
        self.ui.src_le.setLayout(hl)
        sp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hl.addItem(sp)

        self.add_file_pb = QPushButton('...')
        self.add_file_pb.setFlat(True)
        self.add_file_pb.setMaximumWidth(24)
        hl.addWidget(self.add_file_pb)

    def _signal_init(self):
        self.ui.src_le.textChanged.connect(self.on_src_text_changed)
        # self.ui.src_le.editingFinished.connect(self.on_src_text_changed)
        self.ui.dest_le.textChanged.connect(self.on_dest_text_changed)
        self.add_file_pb.clicked.connect(self.on_browse_file_button_clicked)

        self.ui.select_all_common_fmt_cb.stateChanged.connect(self.on_select_all_commom_fmt_changed)

        # 确认取消
        self.ui.ok_pb.clicked.connect(self.on_ok_button_pressed)
        self.ui.cancel_pb.clicked.connect(self.on_cancel_button_pressed)

    def on_browse_file_button_clicked(self):
        try:
            def_dir = os.getcwd()
            data_fmt = "All files (*);;" \
                       "Images (*.png *.xpm *.jpg);;" \
                       "Text files (*.txt);;" \
                       "XML files (*.xml)"
            binary_fmt = "Binary Data(*.dll *.so *.bin *.hex *.a *.dylib *.lib);;" \
                         "All files (*)"
            if self.parent_le.objectName() == 'add_binary_le':
                fmt = binary_fmt
            else:
                fmt = data_fmt
            file_list, fmt = QFileDialog.getOpenFileNames(self, '选择文件', def_dir, fmt)
            logging.info("file list:" + str(file_list) + "file type:" + str(fmt))
            # 预处理以下字符串列表，分号分隔
            file_str = ''
            for file in file_list:
                file_str += file + cmd_path_sep
            self.ui.src_le.setText(file_str)
            self.raw_files = file_str
            pre_process_thread = threading.Thread(target=self.pre_process_for_thread)
            pre_process_thread.setDaemon(False)
            pre_process_thread.start()
        except Exception as e:
            logging.error(e)

    def on_ok_button_pressed(self):
        logging.info("ok button pressed")
        if self.ui.select_all_common_fmt_cb.checkState() == Qt.Checked:
            self.parent_le.insert(self.common_fmt_group)
        else:
            self.parent_le.insert(self.single_file_group)
        self.close()

    def pre_process_for_thread(self):
        src = self.raw_files
        for file_path in src.split(cmd_path_sep):
            if os.path.isfile(file_path):
                f_name, f_fmt = os.path.splitext(file_path)
                f_list = self.fmt_file_group.get(f_fmt)
                if f_list is None:
                    self.fmt_file_group[f_fmt] = [f_name]
                else:
                    if file_path not in f_list:
                        logging.info("append:" + str(file_path))
                        f_list.append(file_path)

    def changed_process_thread_entry(self):
        logging.info("changed_process_thread_entry")
        dest = self.ui.dest_le.text()
        if dest == '':
            dest = '.'  # 默认为'.'

        # 用于最终命令, 文件名:路径,如 'src/README.txt:.'， 多个之间分号隔开
        src = self.raw_files
        self.single_file_group = ''
        for file_path in src.split(cmd_path_sep):
            if os.path.isfile(file_path):
                logging.info(file_path)
                self.single_file_group += file_path + os.pathsep + dest + cmd_path_sep
        self.common_fmt_group = self.parse_fmt_path(dest)
        logging.info("common:" + str(self.common_fmt_group))

        if self.ui.select_all_common_fmt_cb.checkState() == Qt.Checked:
            self.ui.src_le.setText(self.common_fmt_group)
        else:
            self.ui.src_le.setText(self.single_file_group)

        # self.parent_le.insert(self.single_file_group)

    def parse_fmt_path(self, dest):
        value = ''
        for key in self.fmt_file_group.keys():
            tmp = ''
            file_list = self.fmt_file_group[key]
            for file in file_list:
                f_path, f_name = os.path.split(file)  # f_name没有后缀就是文件名
                logging.info("file path:" + f_path + "file name:" + f_name)
                if tmp == '':
                    tmp = f_path
                else:
                    if tmp == f_path:
                        logging.info("file path is common:" + f_path)
                        continue
                    else:
                        tmp = f_path
                value += tmp + '/' + '*' + key + os.pathsep + dest + cmd_path_sep
        return value

    def on_cancel_button_pressed(self):
        logging.info("cancel button pressed")
        self.close()

    def on_src_text_changed(self, text):
        # 获取源目录/文件
        logging.info("src changed start thread")
        process_thread = threading.Thread(target=self.changed_process_thread_entry)
        process_thread.setDaemon(False)
        process_thread.start()

    def on_dest_text_changed(self, text):
        # 获取源目录/文件
        logging.info("dest changed start thread")
        process_thread = threading.Thread(target=self.changed_process_thread_entry)
        process_thread.setDaemon(False)
        process_thread.start()

    def on_select_all_commom_fmt_changed(self, state):
        # 获取源目录/文件
        logging.info("checkbox changed start thread")
        process_thread = threading.Thread(target=self.changed_process_thread_entry)
        process_thread.setDaemon(False)
        process_thread.start()


