#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 9:34
# @Author  : JAMO WOO
# email    : jinxiangwzh@163.com
# @File    : test.py
import logging
import sys

from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget

import Toast


class SelfTest:
    def __init__(self):
        self.test_widget = QWidget()
        self.test_widget.show()
        self.test_widget.resize(500, 200)
        # self.test_widget.move(483,284)

        try:

            Toast.make_text(self.test_widget, "This is a PyQt5 Toast", Toast.LENGTH_LONG)

            #Toast.make_text(self.test_widget, "This is a PyQt5 Toast", Toast.LENGTH_LONG, background_color=QColor("#555555"))

        except Exception as e:
            logging.info(e)
        #QMessageBox.information(None,"提示","This is a PyQt5 QMessageBox")
        # toaster = win10toast.ToastNotifier()
        # toaster.show_toast("Notifier!!!",
        #                    "This is a PyQt5 Notifier",
        #                    icon_path="python.ico",
        #                    duration=10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        test = SelfTest()
    except Exception as e:
        logging.error(e)
    sys.exit(app.exec_())
