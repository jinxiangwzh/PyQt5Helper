#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         c_main_widget
# Description:  
# Author:       Great Master
# Date:         2020/4/24
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import logging
import os

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices, QFont
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel

from JWidget.JToast import Toast
from app_global import set_project_path, get_project_path, version_cmd, pyqt5_helper_version
from great_master_sdk.about_software.c_about_software import AboutSoftware
from great_master_sdk.app_stat_task import StatTask
from great_master_sdk.business_card.business_card import BusinessCard
from great_master_sdk.donate.c_donate import Donate
from great_master_sdk.software_update.software_update import Update
from util.exec_cmd import ExecCmd
from util.xml_prj import new_project, save_project, update_project, open_project
from widget.c_left_menu_widget import PyinstallerGUI
from widget.main_widget_ui import Ui_PyQt5Helper


class PyQt5Helper(QMainWindow):
    def __init__(self) -> None:
        super(PyQt5Helper, self).__init__()
        self.ui = Ui_PyQt5Helper()
        self.ui.setupUi(self)
        self.pyinstaller_gui = None
        self.status_bar_lb = QLabel()
        self.exe_cmd = ExecCmd()
        self._signal_init()
        self._custom_init()
        self.business_card_widget = None
        self.update_widget = None
        self.donate_widget = None
        self.about_software_widget = None
        self.stat_task = None

    def _signal_init(self):
        # File
        self.ui.new_action.triggered.connect(self.on_new_project_action_triggered)
        self.ui.save_action.triggered.connect(self.on_save_project_action_triggered)
        self.ui.open_action.triggered.connect(self.on_open_project_action_triggered)
        #self.ui.config_action.triggered.connect(self.on_config_action_triggered)
        self.ui.exit_action.triggered.connect(self.on_exit_action_triggered)

        # help
        self.ui.about_author_action.triggered.connect(self.on_about_author_triggered)
        self.ui.donate_action.triggered.connect(self.on_donate_triggered)
        self.ui.check_update_action.triggered.connect(self.on_check_update_triggered)
        self.ui.pyinstaller_pdf_action.triggered.connect(self.on_open_pyinstaller_pdf)
        self.ui.about_software_action.triggered.connect(self.on_about_software_triggered)
        self.exe_cmd.finished_signal.connect(self.show_version_message)

    def _custom_init(self):
        self.ui.pyqt_helper_status_bar.addWidget(self.status_bar_lb)
        cmd = ['pyinstaller', version_cmd]
        self.exe_cmd.execute(cmd)  # 查询pyinstaller版本在状态栏显示
        self.stat_task = StatTask(port=8001, server_ip="123.56.169.67")
        self.stat_task.setDaemon(True)
        self.stat_task.start()

    def on_new_project_action_triggered(self):
        try:
            (file_path, file_type) = QFileDialog.getSaveFileName(self, "创建新项目", './', "Project Files(*.gm)")
            logging.info("project file path:" + file_path)
            if file_path != "":
                set_project_path(file_path)
                prj_doc = new_project()
                save_project(prj_doc, file_path)
                set_project_path(file_path)
                self.load_pyinstaller_gui()
        except Exception as e:
            logging.error("[new project] " + str(e))

    def on_save_project_action_triggered(self):
        if self.pyinstaller_gui is None:
            Toast.make_text(None, "没有数据可以保存", Toast.LENGTH_LONG).show()
            return
        prj_path = get_project_path()
        if prj_path != '':
            update_project(prj_path)
            Toast.make_text(None, "项目已更新", Toast.LENGTH_LONG)
        else:
            logging.warning("[save project] path should not null")
            (file_path, file_type) = QFileDialog.getSaveFileName(self, "保存项目", './', "Project Files(*.gm)")
            logging.info(file_path)
            set_project_path(file_path)
            try:
                prj_doc = new_project()
                save_project(prj_doc, file_path)
                set_project_path(file_path)
                Toast.make_text(None, "已保存", Toast.LENGTH_LONG)
            except Exception as e:
                logging.error(e)

    def on_open_project_action_triggered(self):
        try:
            def_path = get_project_path()
            file_path, fmt = QFileDialog.getOpenFileName(self, "打开项目", def_path, "Project Files(*.gm)")
            if file_path == '':
                logging.debug("open project is cancel")
                return
            # 载入打开得项目参数
            logging.debug("open project:" + file_path)
            open_project(file_path)
            self.load_pyinstaller_gui()
        except Exception as e:
            logging.error('Open Project:' + str(e))

    def on_config_action_triggered(self):
        pass

    def on_exit_action_triggered(self):
        logging.info("exit app")
        self.close()

    def on_about_author_triggered(self):
        try:
            self.business_card_widget = BusinessCard()
        except Exception as e:
            logging.error("business card:" + str(e))

    def on_check_update_triggered(self):
        self.update_widget = Update()
        self.update_widget.set_window_icon(":/left_menu/app_icon.png")
        self.update_widget.show()

    def on_donate_triggered(self):
        self.donate_widget = Donate()
        self.donate_widget.show()

    def load_pyinstaller_gui(self):
        # 新建和打开导入
        try:
            if self.pyinstaller_gui is not None:
                logging.debug("pyinstaller_gui is not None, now close->remove->destoryit")
                self.pyinstaller_gui.close()
                self.ui.main_parent_hl.removeWidget(self.pyinstaller_gui)
                self.pyinstaller_gui.destroy()
            self.pyinstaller_gui = PyinstallerGUI()
            self.ui.main_parent_hl.addWidget(self.pyinstaller_gui)
        except Exception as e:
            logging.error(str(e))

    def show_version_message(self, msg_tuple):
        if msg_tuple[1] == '':
            self.status_bar_lb.setText('本机pyinstaller版本:' + msg_tuple[0])  # 后面加两个空格，免得显示太靠边
        else:
            self.status_bar_lb.setText('查询本机pyinstaller出错：' + msg_tuple[1])

    @staticmethod
    def on_open_pyinstaller_pdf():
        logging.info("current path:" + os.getcwd())
        QDesktopServices.openUrl(QUrl.fromLocalFile("./doc/pyinstaller.pdf"))

    def on_about_software_triggered(self):
        try:
            desc = """PyQt5Helper的开发旨在减少Python开发人员在打包过程中遇到的问题，软件采用图形化的界面操作方式实现Pyinstaller的命令，在使用的过程中，如果您有任何关于本软件的问题，都可以联系作者。"""
            self.about_software_widget = AboutSoftware()
            serif_font = QFont("Times", 10, QFont.Bold)
            self.about_software_widget.set_top_title("PyQt5Helper-" + pyqt5_helper_version, serif_font)
            self.about_software_widget.set_about_software_desc(desc)
            self.about_software_widget.show()
        except Exception as e:
            logging.error(e)
