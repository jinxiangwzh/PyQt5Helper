#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         c_left_menu_widget
# Description:  
# Author:       Great Master
# Date:         2020/4/24
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import threading

from PyQt5.QtWidgets import QFrame, QButtonGroup, QMessageBox

from JWidget.JToast import Toast
from app_global import *
from util.xml_prj import update_project
from widget.c_add_data_item_widget import AddDataItemWidget
from widget.c_build_process import SubProcessWidget
from widget.c_general_item_widget import GeneralItemWidget
from widget.c_generate_packet_widget import GeneratePacketWidget
from widget.c_sys_spec_widget import SysSpecWidget
from widget.left_menu_widget_ui import Ui_pyinstaller_gui


class PyinstallerGUI(QFrame):
    def __init__(self):
        super(PyinstallerGUI, self).__init__()
        self.ui = Ui_pyinstaller_gui()
        self.ui.setupUi(self)
        # self.setStyleSheet("background-color:white;")
        self.current_widget = {'current': QFrame}
        self.general_item_widget = None
        self.add_data_item_widget = None
        self.sys_spec_item_widget = None
        self.generate_packet_item_widget = None
        self.sub_process_widget: SubProcessWidget = None
        self._signal_init()
        self._widget_init()
        self.building_thread = None

    def _signal_init(self):
        self.ui.general_item_tb.clicked.connect(self.on_general_item_button_clicked)
        self.ui.general_item_tb.setAutoFillBackground(True)
        self.ui.add_data_item_tb.clicked.connect(self.on_add_data_item_button_clicked)
        self.ui.system_spec_item_tb.clicked.connect(self.on_system_spec_item_button_clicked)
        self.ui.generate_item_tb.clicked.connect(self.on_generate_item_button_clicked)
        self.ui.start_build_pb.clicked.connect(self.on_start_building_button_clicked)

    def _widget_init(self):
        # 左侧按键,确保菜单一次只能选择一个
        self.left_menu_button_gp = QButtonGroup()
        self.left_menu_button_gp.addButton(self.ui.generate_item_tb)
        self.left_menu_button_gp.addButton(self.ui.general_item_tb)
        self.left_menu_button_gp.addButton(self.ui.add_data_item_tb)
        self.left_menu_button_gp.addButton(self.ui.system_spec_item_tb)

        # 默认显示general widget
        self.general_item_widget: QFrame = GeneralItemWidget()
        self.ui.scroll_area_vl.addWidget(self.general_item_widget)
        self.ui.general_item_tb.setChecked(True)  # 默认选中
        self.current_widget['current'] = self.general_item_widget

        self.add_data_item_widget = AddDataItemWidget()
        self.ui.scroll_area_vl.addWidget(self.add_data_item_widget)
        self.add_data_item_widget.hide()

        self.sys_spec_item_widget = SysSpecWidget()
        self.ui.scroll_area_vl.addWidget(self.sys_spec_item_widget)
        self.sys_spec_item_widget.hide()

        self.generate_packet_item_widget = GeneratePacketWidget()
        self.ui.scroll_area_vl.addWidget(self.generate_packet_item_widget)
        self.generate_packet_item_widget.hide()

    def _widget_manage(self, widget):
        """
        manage the widget in item_widget_hl,which will show and which will hide
        :param widget: widget that triggered and will be show
        :return:
        """
        current_widget: QFrame = self.current_widget['current']
        logging.debug("{} is current show".format(current_widget.objectName()))
        logging.debug("{} is request".format(widget.objectName()))
        if widget is current_widget:
            logging.debug("do nothing")
        else:
            logging.debug("update current, hide old current, and show request")
            self.current_widget['current'] = widget
            current_widget.hide()
            widget.show()

    def on_general_item_button_clicked(self):
        self._widget_manage(self.general_item_widget)

    def on_add_data_item_button_clicked(self):
        self._widget_manage(self.add_data_item_widget)

    def on_system_spec_item_button_clicked(self):
        self._widget_manage(self.sys_spec_item_widget)

    def on_generate_item_button_clicked(self):
        self._widget_manage(self.generate_packet_item_widget)

    def on_start_building_button_clicked(self):
        logging.debug("start build button state:")
        if not self.ui.start_build_pb.isChecked():
            Toast.make_text(None, "正在构建,请稍后", Toast.LENGTH_LONG)
            return
        if get_input_file_path() == '':
            Toast.make_text(None, "请选择输入文件", Toast.LENGTH_LONG)
            self.ui.start_build_pb.setChecked(False)
            return
        self.sub_process_widget = SubProcessWidget()
        self.sub_process_widget.show()
        self.building_thread = threading.Thread(target=self.building_thread_entry, daemon=True)
        self.building_thread.start()

    @staticmethod
    def assemble_execute_cmd(cmd, argv, build_cmd):
        # 先单拉出来,处理一些特别的命令
        if cmd == add_data_cmd:
            add_data_list = []
            for data in argv.split(cmd_path_sep):
                if data != '':
                    add_data_list.append(add_data_cmd + '=' + data)
            build_cmd.extend(add_data_list)
        elif cmd == add_binary_cmd:
            bin_list = []
            for data in argv.split(cmd_path_sep):
                if data != '':
                    bin_list.append(add_binary_cmd + '=' + data)
            build_cmd.extend(bin_list)
        elif cmd == hidden_import_cmd:
            import_list = []
            for data in argv.split(semi_colon_sep):
                if data != '':
                    import_list.append(hidden_import_cmd + '=' + data)
            build_cmd.extend(import_list)
        elif cmd == additional_hooks_dir_cmd:
            hook_list = []
            for data in argv.split(semi_colon_sep):
                if data != '':
                    hook_list.append(additional_hooks_dir_cmd + '=' + data)
            build_cmd.extend(hook_list)
        elif cmd == runtime_hook_cmd:
            hook_list = []
            for data in argv.split(semi_colon_sep):
                if data != '':
                    hook_list.append(runtime_hook_cmd + '=' + data)
            build_cmd.extend(hook_list)
        elif cmd == exclude_module_cmd:
            hook_list = []
            for data in argv.split(semi_colon_sep):
                if data != '':
                    hook_list.append(exclude_module_cmd + '=' + data)
            build_cmd.extend(hook_list)
        elif cmd == upx_exclude_cmd:
            exclude_files = []
            for data in argv.split(semi_colon_sep):
                if data != '':
                    exclude_files.append(upx_exclude_cmd + '=' + data)
            build_cmd.extend(exclude_files)
        else:
            build_cmd.append(cmd + '=' + argv)

        return build_cmd

    def building_thread_entry(self):
        logging.debug("building_thread_entry->")
        build_cmd = ['pyinstaller']
        prj_path = get_project_path()
        if prj_path != '':
            update_project(prj_path)
        try:
            item_list = project_item_dict.keys()
            for item in item_list:
                if item == 'none_cmd':
                    continue
                cmd_list = project_item_dict[item].keys()  # 每一个选项页
                for cmd in cmd_list:
                    # 先确定命令是否使能
                    argv = project_item_dict[item][cmd][0]
                    state = project_item_dict[item][cmd][1]
                    if int(state):
                        # logging.debug("%s" % cmd + " is enable")
                        if argv != '':
                            # build_cmd.append(cmd + '=' + argv)
                            # build_cmd.append(argv)
                            build_cmd = self.assemble_execute_cmd(cmd, argv, build_cmd)
                        else:
                            build_cmd.append(cmd)
                    else:
                        pass
        except Exception as e:
            logging.debug(str(e))
            self.sub_process_widget.show_message_box_msg(str(e))
        build_cmd.append(os.path.join(get_input_file_path()))
        logging.debug(build_cmd)  # ['--distpath', 'E:/PyQt5Helper/spec/dist', '--onefile', '', '--specpath',
        # 'E:/PyQt5Helper/spec', '--name', 'PyQt5Helpey', 'E:/PyQt5Helper/PyQt5Helper.py']
        try:
            self.sub_process_widget.execute_cmd(build_cmd)
            logging.debug("build complete")
        except Exception as e:
            logging.error("pyInstaller.__main__.run" + str(e))
        self.ui.start_build_pb.setChecked(False)
