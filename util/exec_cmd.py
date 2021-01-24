#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         global
# Description:
# Author:       Great Master
# Date:         2020/4/28
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import logging
import os
import subprocess
import threading
import time

from PyQt5.QtCore import QObject, pyqtSignal


class ExecCmd(QObject):
    """
    TODO:后面把输出到GUI的功能合并过来，作为标准包使用
    """
    finished_signal = pyqtSignal(tuple)  # 用来通知执行结束的

    def __init__(self):
        super(ExecCmd, self).__init__()
        self.cmd = None
        self.cmd_thread = threading.Thread(target=self.cmd_thread_entry)

    def cmd_thread_entry(self):
        try:
            proc = subprocess.Popen(self.cmd, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, encoding="utf-8")
            while proc.poll() is None:
                time.sleep(3)
            outs, errs = proc.communicate()
            logging.info("out:" + str(outs) + ";error:" + errs)
            self.finished_signal.emit((outs, errs,))  # command is execute finished
        except Exception as e:
            logging.error(e)

    def execute(self, cmd):
        self.cmd = cmd
        self.cmd_thread.start()
