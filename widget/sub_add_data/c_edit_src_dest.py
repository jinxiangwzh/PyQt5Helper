#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         c_edit_src_dest
# Description:  
# Author:       Great Master
# Date:         2020/8/10
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import logging
import os

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QLineEdit

from app_global import cmd_path_sep
from widget.sub_add_data.edit_src_dest_ui import Ui_edit_src_dest


class EditSrcDest(QWidget):
    # TODO 添加创建按键，调用创建接口
    def __init__(self, parent_le):
        super(EditSrcDest, self).__init__()
        self.parent_le: QLineEdit = parent_le
        # 从主界面--add-data传进来的参数
        self.add_data = self.parent_le.text()
        self.ui = Ui_edit_src_dest()
        self.ui.setupUi(self)
        self._signal_init()
        try:
            self.parse_cmd_to_table()
        except Exception as e:
            logging.error(str(e))

    def _signal_init(self):
        self.ui.ok_pb.clicked.connect(self.on_ok_button_clicked)
        self.ui.detail_tb.cellChanged.connect(self.on_cell_changed)
        self.ui.delete_pb.clicked.connect(self.on_delete_button_clicked)
        self.ui.cancel_pb.clicked.connect(self.on_cancel_button_clicked)

    def parse_cmd_to_table(self):
        # 解析主界面传递过来的命令到表格
        for cmd in self.add_data.split(cmd_path_sep):
            logging.info(cmd)
            if cmd == '':
                continue
            src_path, dest = cmd.split(os.pathsep)
            count = self.ui.detail_tb.rowCount()
            new_index = count + 1
            self.ui.detail_tb.setRowCount(new_index)
            item = QTableWidgetItem()
            item.setText(str(count))
            self.ui.detail_tb.setVerticalHeaderItem(new_index, item)

            item = QTableWidgetItem(src_path)
            self.ui.detail_tb.setItem(count, 0, item)

            item = QTableWidgetItem(dest)
            self.ui.detail_tb.setItem(count, 1, item)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)

    def on_ok_button_clicked(self):
        count = self.ui.detail_tb.rowCount()

        logging.info(self.ui.detail_tb.isWindowModified())
        if self.ui.detail_tb.isWindowModified():
            logging.info("src dest table has modified")
            modified_str = ''
            for index in range(count):
                item1 = self.ui.detail_tb.item(index, 0)
                item2 = self.ui.detail_tb.item(index, 1)
                modified_str += item1.text() + os.pathsep + item2.text() + cmd_path_sep
            self.parent_le.setText(modified_str)
        else:
            logging.info("src dest table not modify,close direct")

        self.close()

    def on_cell_changed(self, row, column):
        logging.info("on_cell_changed")
        self.ui.detail_tb.setWindowModified(True)

    def on_delete_button_clicked(self):
        current_row = self.ui.detail_tb.currentRow()
        self.ui.detail_tb.removeRow(current_row)
        self.ui.detail_tb.setWindowModified(True)

    def on_cancel_button_clicked(self):
        self.close()



