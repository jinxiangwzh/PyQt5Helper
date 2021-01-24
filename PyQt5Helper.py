#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         app
# Description:  
# Author:       Great Master
# Date:         2020/4/24
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import logging
import platform
import sys
from logging import handlers

from PyQt5.QtWidgets import QApplication

from css.normal import normal_style
from widget.c_main_widget import PyQt5Helper

fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
file_name = 'PyinstallerGUI.log'

th = handlers.TimedRotatingFileHandler(filename=file_name, when='D', backupCount=3, encoding='utf-8')
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    print('running in a PyInstaller bundle')
    logging.basicConfig(
        level=logging.DEBUG,
        format=fmt,
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='PyinstallerGUI.log',
        filemode='w'
    )
else:
    logging.basicConfig(
        level=logging.DEBUG,
        format=fmt,
        datefmt='%a, %d %b %Y %H:%M:%S',
    )
    logging.info('running in a normal Python process')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if platform.system() == "Windows":
        import ctypes

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("PyinstallerGUI")
    logging.debug("application is start")
    try:
        app.setStyleSheet(normal_style)
    except Exception as e:
        logging.error("app setStyle error:" + str(e))
    helper = PyQt5Helper()
    helper.show()
    sys.exit(app.exec_())
