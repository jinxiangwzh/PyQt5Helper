#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         c_add_data_item_widget
# Description:
# Author:       Great Master
# Date:         2020/5/6
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import logging
import subprocess
import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget, QMessageBox

from widget.build_process_info_ui import Ui_build_process_widget


class SubProcessWidget(QWidget):
    update_log = pyqtSignal(str)
    msg_box = pyqtSignal(str)

    def __init__(self):
        super(SubProcessWidget, self).__init__()
        self.ui = Ui_build_process_widget()
        self.ui.setupUi(self)
        self.proc: subprocess.Popen = None
        self.init_ui()
        self._signal_init()

    def _signal_init(self):
        self.ui.pushButton.clicked.connect(self.on_force_exit_button_clicked)
        self.update_log.connect(self._on_update_text)
        self.msg_box.connect(self.on_message_box_show)
        # self.ui.textEdit

    def init_ui(self):
        # Create the text output widget.
        self.ui.build_process_te.ensureCursorVisible()

    def closeEvent(self, event):
        try:
            logging.info("kill subprocess child")
            self.proc.kill()
        except Exception as e:
            logging.error(e)
        super().closeEvent(event)

    def _on_update_text(self, text):
        """Write console output to text widget."""
        cursor = self.ui.build_process_te.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.ui.build_process_te.setTextCursor(cursor)
        self.ui.build_process_te.ensureCursorVisible()

    def on_force_exit_button_clicked(self):
        self.close()

    def send_log_to_display(self, text):
        self.update_log.emit(text)

    def execute_cmd(self, cmd):
        logging.info("execute subprocess Popen")
        self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, encoding="utf-8")
        while self.proc.poll() is None:  # 检查子进程是否被终止
            out = self.proc.stdout.readline().strip()
            if out:
                self.send_log_to_display(str(out) + '\n')
                logging.debug(out)
                if out.find("COLLECT-00.toc completed successfully") != -1:
                    self.show_message_box_msg("恭喜你构建成功")
                elif out.find('syntax error') != -1:
                    self.show_message_box_msg("貌似你选择的文件有语法错误哦!")
                elif out.find('Executing command failed!') != -1:
                    self.show_message_box_msg("命令执行失败!")

    def show_message_box_msg(self, msg):
        self.msg_box.emit(msg)

    def on_message_box_show(self, msg):
        QMessageBox.information(self, "提示", msg)
