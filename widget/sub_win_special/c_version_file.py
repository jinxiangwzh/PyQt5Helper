#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         c_version_file.py
# Description:
# Author:       Great Master
# Date:         2020/8/13
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import logging
import os
import threading
from shutil import copyfile

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIntValidator, QValidator
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QLineEdit, QComboBox, QHBoxLayout, QMessageBox, QFileDialog

from css.sub_widget_css import version_file_css
from widget.sub_win_special.version_file_ui import Ui_file_version_desc_widget


class VersionFile(QWidget):
    # 这个字典作为StringTable中QLineEdit的objectname
    str_tab = {
        0: "CompanyName",
        1: "FileDescription",
        2: "FileVersion",
        3: "InternalName",
        4: "LegalCopyright",
        5: "LegalTrademarks",
        6: "OriginalFilename",
        7: "ProductName",
        8: "ProductVersion",
    }

    # https://docs.microsoft.com/en-us/windows/win32/menurc/varfileinfo-block
    lang_id = {
        0x0401: "Arabic",
        0x0415: "Polish",
        0x0402: "Bulgarian",
        0x0416: "Portuguese(Brazil)",
        0x0403: "Catalan",
        0x0417: "Rhaeto-Romanic",
        0x0404: "Traditional Chinese",
        0x0418: "Romanian",
        0x0405: "Czech",
        0x0419: "Russian",
        0x0406: "Danish",
        0x041A: "Croato-Serbian(Latin)",
        0x0407: "German",
        0x041B: "Slovak",
        0x0408: "Greek",
        0x041C: "Albanian",
        0x0409: "U.S.English",
        0x041D: "Swedish",
        0x040A: "Castilian Spanish",
        0x041E: "Thai",
        0x040B: "Finnish",
        0x041F: "Turkish",
        0x040C: "French",
        0x0420: "Urdu",
        0x040D: "Hebrew",
        0x0421: "Bahasa",
        0x040E: "Hungarian",
        0x0804: "Simplified Chinese",
        0x040F: "Icelandic",
        0x0807: "Swiss German",
        0x0410: "Italian",
        0x0809: "U.K.English",
        0x0411: "Japanese",
        0x080A: "Spanish(Mexico)",
        0x0412: "Korean",
        0x080C: "Belgian French",
        0x0413: "Dutch",
        0x0C0C: "Canadian French",
        0x0414: "Norwegian–Bokmal",
        0x100C: "Swiss French",
        0x0810: "Swiss Italian",
        0x0816: "Portuguese(Portugal)",
        0x0813: "Belgian Dutch",
        0x081A: "Serbo - Croatian(Cyrillic)",
        0x0814: "Norwegian–Nynorsk",
    }

    charset_id = {
        0: "7 - bit ASCII",
        932: "Japan(Shift–JISX-0208)",
        949: "Korea(Shift–KSC 5601)",
        950: "Taiwan(Big5)",
        1200: "Unicode",
        1250: "Latin-2(Eastern European)",
        1251: "Cyrillic",
        1252: "Multilingual",
        1253: "Greek",
        1254: "Turkish",
        1255: "Hebrew",
        1256: "Arabic",
    }

    file_type = {
        0x00000001: 'Application',
        0x00000002: 'DLL',
        0x00000003: 'Device Driver',
        0x00000004: 'Font',
        0x00000007: "Static LIB",
        0x00000000: "UNKNOWN",
        0x00000005: "Virtual Device",
    }

    msg_signal = pyqtSignal(str)
    update_ui = pyqtSignal()

    def __init__(self, le: QLineEdit):
        super(VersionFile, self).__init__()
        # 这个字符串不一定对要做检查
        self.version_file_le = le
        self.version_file = self.version_file_le.text()
        self.ui = Ui_file_version_desc_widget()
        self.ui.setupUi(self)
        self.tree = self.ui.file_version_tree
        self.fixed_file_info_item: QTreeWidgetItem = None
        self.kids_item: QTreeWidgetItem = None
        self.tab_child: QTreeWidgetItem = None
        self.version_file_flag = ""  # 标记用的是传入的还是模板
        # 添加的控件
        self.file_version_le = QLineEdit()
        self.product_version_le = QLineEdit()
        self.file_type_cb = QComboBox()
        self.lang_id_cb = QComboBox()
        self.charset_id_cb = QComboBox()
        self._signal_init()
        self._custom_ui()
        # 载入数据
        self.load_config_information()

    def _signal_init(self):
        self.tree.itemExpanded.connect(self.on_tree_item_expanded)
        self.msg_signal.connect(self.on_message_box_show)
        self.update_ui.connect(self.on_update_ui)  # 线程从文件中解析完成后，数据保存在内存，然后从内存更新到UI
        self.ui.ok_pb.clicked.connect(self.on_ok_button_clicked)
        self.ui.cancel_pb.clicked.connect(self.on_cancel_button_clicked)
        # 其他的在设置widget的时候设置

    def _custom_ui(self):
        self.ui.file_version_tree.setColumnWidth(0, 220)
        # 根item默认展开
        items = self.tree.findItems("VSVersionInfo", Qt.MatchExactly, 0)
        # root item
        for item in items:
            self.ui.file_version_tree.expandItem(item)

        for index in range(items[0].childCount()):
            child = items[0].child(index)
            if child.text(0) == "FixedFileInfo":
                child.setExpanded(True)
                self.fixed_file_info_item = child
            elif child.text(0) == "kids":
                child.setExpanded(True)
                self.kids_item = child
                for i in range(child.childCount()):
                    kids_child = child.child(i)
                    kids_child.setExpanded(True)  # kids 下一级不做判断 都展开
            else:
                continue  # no handle
        # 设置输入值的widget
        try:
            self._set_widget_for_item()
        except Exception as e:
            logging.error(e)

    def _set_widget_for_item(self):
        # 先设置widget，再把数据加载进去
        try:
            for index in range(self.fixed_file_info_item.childCount()):
                child = self.fixed_file_info_item.child(index)
                if child.text(0) == "File Version":
                    self._set_widget_for_file_version(child)
                elif child.text(0) == "Product Version":
                    self._set_widget_for_product_version(child)
                elif child.text(0) == "File Type":
                    self._set_widget_for_file_type(child)
        except Exception as e:
            logging.error(e)
        try:
            for index in range(self.kids_item.childCount()):
                child = self.kids_item.child(index)
                if child.text(0) == "StringFileInfo":
                    self._set_widget_for_string_table(child)
                elif child.text(0) == "VarFileInfo":
                    self._set_translation_widget(child)
                else:
                    logging.error("not support")
        except Exception as e:
            logging.error(e)

    def _set_widget_for_file_version(self, child):
        self.file_version_le.setStyleSheet(version_file_css)
        self.file_version_le.setReadOnly(True)
        self.file_version_le.setText("[0 , 0, 0, 0]")  # default,做成列表便于索引修改
        self.file_version_le.setToolTip("(2, 0, 4, 0)解析为16进制的0002000000040000")
        self.file_version_le.textChanged.connect(self.on_file_version_changed)
        self.tree.setItemWidget(child, 1, self.file_version_le)
        for i in range(child.childCount()):
            pos_child = child.child(i)  # 代表元组中的4位
            le = QLineEdit()
            le.setObjectName(str(i))
            le.setAutoFillBackground(True)
            le.setStyleSheet(version_file_css)
            le.setInputMethodHints(Qt.ImhDigitsOnly)  # 给输入法的提示
            validator: QValidator = QIntValidator(0, 0xFFFF, self)
            le.setValidator(validator)
            le.textChanged.connect(self.on_file_version_pos_text_changed)
            self.tree.setItemWidget(pos_child, 1, le)

    def _set_widget_for_product_version(self, child):
        self.product_version_le.setStyleSheet(version_file_css)
        self.product_version_le.setReadOnly(True)
        self.product_version_le.setText("[0 , 0, 0, 0]")  # default,做成列表便于索引修改
        self.product_version_le.setToolTip("(2, 0, 4, 0)解析为16进制的0002000000040000")
        self.product_version_le.textChanged.connect(self.on_product_version_changed)
        self.tree.setItemWidget(child, 1, self.product_version_le)
        for i in range(child.childCount()):
            pos_child = child.child(i)  # 代表元组中的4位
            le = QLineEdit()
            le.setObjectName(str(i))
            le.setAutoFillBackground(True)
            le.setStyleSheet(version_file_css)
            le.setInputMethodHints(Qt.ImhDigitsOnly)  # 给输入法的提示
            validator: QValidator = QIntValidator(0, 0xFFFF, self)
            le.setValidator(validator)
            le.textChanged.connect(self.on_product_version_pos_text_changed)
            self.tree.setItemWidget(pos_child, 1, le)

    def _set_widget_for_file_type(self, child):
        # https://docs.microsoft.com/zh-cn/windows/win32/api/verrsrc/ns-verrsrc-vs_fixedfileinfo?redirectedfrom=MSDN

        self.file_type_cb.addItem("Application", userData=0x00000001)  # itemData(0)可以获取到设置的userData
        self.file_type_cb.setItemData(0, "The file contains an application.", role=Qt.ToolTipRole)

        self.file_type_cb.addItem("DLL", userData=0x00000002)
        self.file_type_cb.setItemData(1, "The file contains a DLL.", role=Qt.ToolTipRole)

        self.file_type_cb.addItem("Device Driver", userData=0x00000003)
        self.file_type_cb.setItemData(2, "The file contains a device driver.", role=Qt.ToolTipRole)

        self.file_type_cb.addItem("Font", userData=0x00000004)
        self.file_type_cb.setItemData(3, "The file contains a font.", role=Qt.ToolTipRole)

        self.file_type_cb.addItem("Static LIB", userData=0x00000007)
        self.file_type_cb.setItemData(4, "The file contains a static-link library.", role=Qt.ToolTipRole)

        self.file_type_cb.addItem("UNKNOWN", userData=0x00000000)
        self.file_type_cb.setItemData(5, "The file type is unknown to the system.", role=Qt.ToolTipRole)

        self.file_type_cb.addItem("Virtual Device", userData=0x00000005)
        self.file_type_cb.setItemData(6, "The file contains a virtual device.", role=Qt.ToolTipRole)

        self.file_type_cb.currentIndexChanged.connect(self.on_file_type_index_changed)
        self.tree.setItemWidget(child, 1, self.file_type_cb)

    def _set_widget_for_string_table(self, str_child):
        """
        str_child 是 StringFileInfo
        :param str_child:
        :return:
        """
        for i in range(str_child.childCount()):
            child = str_child.child(i)
            if child.text(0) == "StringTable":
                self.tab_child = child

                for str_index in range(self.tab_child.childCount()):
                    str_child = self.tab_child.child(str_index)
                    le = QLineEdit()
                    le.setObjectName(self.str_tab.get(str_index))
                    # le.setText(self.str_tab.get(str(str_index)))
                    le.setStyleSheet(version_file_css)
                    le.setInputMethodHints(Qt.ImhDigitsOnly)  # 给输入法的提示
                    le.textChanged.connect(self.on_string_tab_text_changed)
                    self.tree.setItemWidget(str_child, 1, le)

    def _set_translation_widget(self, child):
        try:
            for i in range(child.childCount()):
                c = child.child(i)
                if c.text(0) == "Translation":
                    widget = QWidget()
                    hl = QHBoxLayout()
                    hl.setContentsMargins(0, 0, 0, 0)
                    widget.setLayout(hl)
                    hl.addWidget(self.lang_id_cb)
                    hl.addWidget(self.charset_id_cb)
                    self.tree.setItemWidget(c, 1, widget)
                    # 添加字典中的数据
                    self.lang_id_cb.setToolTip("选择语言")
                    self.lang_id_cb.currentIndexChanged.connect(self.on_select_language_changed)
                    for num, key in enumerate(self.lang_id.keys()):
                        self.lang_id_cb.addItem(self.lang_id[key], userData=key)
                        self.lang_id_cb.setItemData(num, self.lang_id[key] + ":" + str(key), role=Qt.ToolTipRole)
                    # 设置默认选择
                    self.lang_id_cb.setCurrentText(self.lang_id[0x0804])

                    self.charset_id_cb.setToolTip("设置字符")
                    self.charset_id_cb.currentIndexChanged.connect(self.on_select_charset_changed)
                    for num, key in enumerate(self.charset_id.keys()):
                        self.charset_id_cb.addItem(self.charset_id[key], userData=key)
                        self.charset_id_cb.setItemData(num, self.charset_id[key] + ":" + str(key), role=Qt.ToolTipRole)
                    # 设置默认选择
                    self.charset_id_cb.setCurrentText(self.charset_id[1200])
        except Exception as e:
            logging.error(e)

    def load_config_information(self):
        load_thread = threading.Thread(target=self.load_config_thread_entry)
        load_thread.daemon = True
        load_thread.start()

    def load_config_thread_entry(self):
        if os.path.isfile(self.version_file):
            logging.info("version file is exist, use it")
            # 用户选择的文件,如果解析有问题,还要把self.version_file_flag置为空字符
            self.version_file_flag = self.version_file
            self.read_user_select_version(self.version_file)
        else:
            logging.info("version file is not exist, use template")
            # 使用模板，那么这个路径还不确定,由用户选择保存位置
            self.version_file_flag = ""
            self.read_version_file_template("./template/file_version_info.txt")

    def read_user_select_version(self, path):
        self.parse_content(path)

    def read_version_file_template(self, path):
        self.parse_content(path)

    def parse_content(self, path):
        CheckItem.check_pos = 0
        with open(path, 'r', encoding='utf-8') as f:
            while True:
                text = f.readline()
                if text == "":
                    break
                try:
                    if text.find(CheckItem.must[CheckItem.check_pos]) != -1:
                        if CheckItem.must[CheckItem.check_pos] == "filevers=":
                            data = text[text.find('('): text.find(')') + 1]
                            logging.info("parse filevers=" + str(data))
                            VersionFileData.file_version = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "prodvers=":
                            data = text[text.find('('): text.find(')') + 1]
                            logging.info("parse prodvers=" + str(data))
                            VersionFileData.production_version = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "fileType=":
                            data = text[text.find('=') + 1: text.find(',')]
                            logging.info("parse fileType=" + str(data))
                            VersionFileData.file_type = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "CompanyName":
                            data = text[text.find(', u') + 2: text.find('),')]
                            logging.info("parse CompanyName=" + str(data))
                            VersionFileData.company_name = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "FileDescription":
                            data = text[text.find(', u') + 2: text.find('),')]
                            logging.info("parse FileDescription=" + str(data))
                            VersionFileData.file_description = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "FileVersion":
                            data = text[text.find(', u') + 2: text.find('),')]
                            logging.info("parse FileVersion=" + str(data))
                            VersionFileData.file_version_str = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "InternalName":
                            data = text[text.find(', u') + 2: text.find('),')]
                            logging.info("parse InternalName=" + str(data))
                            VersionFileData.internal_name = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "LegalCopyright":
                            data = text[text.find(', u') + 2: text.find('),')]
                            logging.info("parse LegalCopyright=" + str(data))
                            VersionFileData.legal_copyright = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "OriginalFilename":
                            data = text[text.find(', u') + 2: text.find('),')]
                            logging.info("parse OriginalFilename=" + str(data))
                            VersionFileData.original_filename = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "ProductName":
                            data = text[text.find(', u') + 2: text.find('),')]
                            logging.info("parse ProductName=" + str(data))
                            VersionFileData.product_name = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "ProductVersion":
                            data = text[text.find(', u') + 2: text.find(')])')]
                            logging.info("parse ProductVersion=" + str(data))
                            VersionFileData.product_version_str = eval(data)
                        elif CheckItem.must[CheckItem.check_pos] == "Translation":
                            data = text[text.find('[', 20): text.find(')])')]
                            logging.info("parse Translation=" + str(data))
                            VersionFileData.translation = eval(data)
                        else:
                            logging.error("no match find")  # will not here
                        CheckItem.check_pos += 1
                        if CheckItem.check_pos == len(CheckItem.must):
                            logging.info("parse finish")
                            self.update_ui.emit()
                            break
                except Exception as e:
                    logging.error(e)
                    self.set_message("数据解析错误,载入,默认模板")
                    self.version_file = ""
                    self.load_config_information()

    def check_integrity(self, content: str):
        """
        :param content: 用户自己选择的文件和模板都用这个解析
        :return:
        """
        # 先对整个内容做个完整性检查
        for check_item in CheckItem.integrity:
            pos = content.find(check_item)
            if pos < CheckItem.check_pos or pos == -1:
                self.set_message("文件内容解析错误")
                CheckItem.state_msg = "文件内容解析错误"
                return
            else:
                CheckItem.check_pos = pos
        CheckItem.check_pos = 0  # 没用了复位一下

    def on_tree_item_expanded(self, item: QTreeWidgetItem):
        """
        展开时从父LE中载入数据
        :param item:
        :return:
        """
        logging.info("on_tree_item_expanded")
        try:
            if item.text(0) == "File Version":
                logging.info("File Version->expanded")
                for index in range(item.childCount()):
                    child = item.child(index)
                    v = self.file_version_le.text()
                    le: QLineEdit = self.tree.itemWidget(child, 1)
                    le.setText(str(eval(v)[index]))

            elif item.text(0) == "Product Version":
                logging.info("Product Version->expanded")
                for index in range(item.childCount()):
                    child = item.child(index)
                    v = self.product_version_le.text()
                    le: QLineEdit = self.tree.itemWidget(child, 1)
                    le.setText(str(eval(v)[index]))
            else:
                logging.info("not concern item->expanded")
        except Exception as e:
            logging.error(e)

    def on_file_version_pos_text_changed(self, text):
        if text == '':
            return
        sender: QLineEdit = self.sender()
        v_str = self.file_version_le.text()
        if v_str == '':
            v = [0, 0, 0, 0]  # 已经初始化,永远不会到这
        else:
            v = eval(v_str)
        try:
            if not isinstance(v, list):
                logging.error("version file string cannot convert to list")
            index = int(sender.objectName())
            v[index] = int(text)
            self.file_version_le.setText(str(v))
        except Exception as e:
            logging.error(e)

    def on_product_version_pos_text_changed(self, text):
        if text == '':
            return
        sender: QLineEdit = self.sender()
        v_str = self.product_version_le.text()
        if v_str == '':
            v = [0, 0, 0, 0]  # 已经初始化,永远不会到这
        else:
            v = eval(v_str)
        try:
            if not isinstance(v, list):
                logging.error("version file string cannot convert to list")
            index = int(sender.objectName())
            v[index] = int(text)
            self.product_version_le.setText(str(v))
        except Exception as e:
            logging.error(e)

    def on_file_type_index_changed(self, index):
        user_data = self.file_type_cb.itemData(index)
        VersionFileData.file_type = user_data

    @staticmethod
    def on_file_version_changed(version):
        VersionFileData.file_version = tuple(eval(version))

    @staticmethod
    def on_product_version_changed(version):
        VersionFileData.production_version = tuple(eval(version))

    def on_string_tab_text_changed(self, text):
        sender: QLineEdit = self.sender()
        object_name = sender.objectName()
        # 保持跟上面的表格一致
        if object_name == "CompanyName":
            VersionFileData.company_name = text
        elif object_name == "FileDescription":
            VersionFileData.file_description = text
        elif object_name == "FileVersion":
            VersionFileData.file_version_str = text
        elif object_name == "InternalName":
            VersionFileData.internal_name = text
        elif object_name == "LegalCopyright":
            VersionFileData.legal_copyright = text
        elif object_name == "LegalTrademarks":
            VersionFileData.legal_trademarks = text
        elif object_name == "OriginalFilename":
            VersionFileData.original_filename = text
        elif object_name == "ProductName":
            VersionFileData.product_name_str = text
        elif object_name == "ProductVersion":
            VersionFileData.product_version_str = text
        else:
            logging.error("send object name error")

    def on_select_language_changed(self, index):
        try:
            VersionFileData.translation[0] = self.lang_id_cb.itemData(index)
            logging.info("language changed to:" + str(VersionFileData.translation))
        except Exception as e:
            logging.error(e)

    def on_select_charset_changed(self, index):
        try:
            VersionFileData.translation[1] = self.charset_id_cb.itemData(index)
            logging.info("charset changed to:" + str(VersionFileData.translation))
        except Exception as e:
            logging.error(e)

    def on_message_box_show(self, msg):
        QMessageBox.critical(self, "错误", msg)

    def set_message(self, msg):
        # 调用信号
        self.msg_signal.emit(msg)

    def on_update_ui(self):
        try:
            self.file_version_le.setText(str(list(VersionFileData.file_version)))
            self.product_version_le.setText(str(list(VersionFileData.production_version)))
            self.file_type_cb.setCurrentText(self.file_type.get(VersionFileData.file_type))
            self.lang_id_cb.setCurrentText(self.lang_id.get(VersionFileData.translation[0]))
            self.charset_id_cb.setCurrentText(self.charset_id.get(VersionFileData.translation[1]))
            for index in range(self.tab_child.childCount()):
                child = self.tab_child.child(index)
                le: QLineEdit = self.tree.itemWidget(child, 1)
                if child.text(0) == "CompanyName":
                    le.setText(VersionFileData.company_name)  # 不用eval,有u和引号
                elif child.text(0) == "FileDescription":
                    le.setText(VersionFileData.file_description)
                elif child.text(0) == "FileVersion":
                    le.setText(VersionFileData.file_version_str)
                elif child.text(0) == "InternalName":
                    le.setText(VersionFileData.internal_name)
                elif child.text(0) == "LegalCopyright":
                    le.setText(VersionFileData.legal_copyright)
                elif child.text(0) == "LegalTrademarks":
                    le.setText(VersionFileData.legal_trademarks)
                elif child.text(0) == "OriginalFilename":
                    le.setText(VersionFileData.original_filename)
                elif child.text(0) == "ProductName":
                    le.setText(VersionFileData.product_name)
                elif child.text(0) == "ProductVersion":
                    le.setText(VersionFileData.product_version_str)
        except Exception as e:
            logging.error(e)

    def on_ok_button_clicked(self):
        save_thread = threading.Thread(target=self.save_version_file_entry)
        save_thread.daemon = False
        save_thread.start()
        self.close()

    def on_cancel_button_clicked(self):
        pass

    def save_version_file_entry(self):
        if self.version_file_flag == '':
            logging.info("use template, select a path")
            (file_path, file_type) = QFileDialog.getSaveFileName(self, "保存版本文件", './file_version_info.txt',
                                                                 "版本文件 (*.txt)")
            self.version_file_le.setText(file_path)
            self.version_file = file_path
            try:
                copyfile("./template/file_version_info.txt", self.version_file)
            except Exception as e:
                logging.error(e)
                self.set_message(str(e))
                return
        content = ""
        with open(self.version_file, 'r+', encoding='utf-8') as f:
            logging.info("open " + self.version_file)
            CheckItem.check_pos = 0
            while True:
                text = f.readline()
                if text == "":
                    break
                if  CheckItem.check_pos < len(CheckItem.must) and text.find(CheckItem.must[CheckItem.check_pos]) != -1:
                    if CheckItem.must[CheckItem.check_pos] == "filevers=":
                        data = text[text.find('('): text.find(')') + 1]
                        logging.info("parse filevers=" + str(data))
                        text = text.replace(data, str(VersionFileData.file_version))
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "prodvers=":
                        data = text[text.find('('): text.find(')') + 1]
                        logging.info("parse prodvers=" + str(data))
                        text = text.replace(data, str(VersionFileData.production_version))
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "fileType=":
                        data = text[text.find('=') + 1: text.find(',')]
                        logging.info("parse fileType=" + str(data))
                        text = text.replace(data, "{:#x}".format(VersionFileData.file_type))  # 0x1->"0x1"
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "CompanyName":
                        data = text[text.find(', u') + 3: text.find('),')]
                        logging.info("parse CompanyName=" + str(data))
                        text = text.replace(data, '\'' + VersionFileData.company_name + '\'')
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "FileDescription":
                        data = text[text.find(', u') + 3: text.find('),')]
                        logging.info("parse FileDescription=" + str(data))
                        text = text.replace(data, '\'' + VersionFileData.file_description + '\'')
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "FileVersion":
                        data = text[text.find(', u') + 3: text.find('),')]
                        logging.info("parse FileVersion=" + str(data))
                        text = text.replace(data, '\'' + VersionFileData.file_version_str + '\'')
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "InternalName":
                        data = text[text.find(', u') + 3: text.find('),')]
                        logging.info("parse InternalName=" + str(data))
                        text = text.replace(data, '\'' + VersionFileData.internal_name + '\'')
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "LegalCopyright":
                        data = text[text.find(', u') + 3: text.find('),')]
                        logging.info("parse LegalCopyright=" + str(data))
                        text = text.replace(data, '\'' + VersionFileData.legal_copyright + '\'')
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "OriginalFilename":
                        data = text[text.find(', u') + 3: text.find('),')]
                        logging.info("parse OriginalFilename=" + str(data))
                        text = text.replace(data, '\'' + VersionFileData.original_filename + '\'')
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "ProductName":
                        data = text[text.find(', u') + 3: text.find('),')]
                        logging.info("parse ProductName=" + str(data))
                        text = text.replace(data, '\'' + VersionFileData.product_name + '\'')
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "ProductVersion":
                        data = text[text.find(', u') + 3: text.find(')])')]
                        logging.info("parse ProductVersion=" + str(data))
                        text = text.replace(data, '\'' + VersionFileData.product_version_str + '\'')
                        logging.info("after replace:" + text)
                    elif CheckItem.must[CheckItem.check_pos] == "Translation":
                        data = text[text.find('[', 20): text.find(')])')]
                        logging.info("parse Translation=" + str(data))
                        text = text.replace(data, str(VersionFileData.translation))
                        logging.info("after replace:" + text)
                    else:
                        logging.error("no match find")  # will not here
                        return

                    content += text
                    if CheckItem.check_pos >= len(CheckItem.must) - 1:
                        logging.info("must item has copy finish, may be have not conecrn, read will be continue")
                    CheckItem.check_pos += 1  # 必须加,不然会重复替换
                else:
                    logging.info("not concern:" + text)
                    content += text
        with open(self.version_file, 'w', encoding='utf-8') as f:
            logging.info("all parameter in memory has copy, now write it into file")
            f.write(content)


class VersionFileData:
    # FixedFileInfo
    file_version: tuple = (0, 0, 0, 0)
    production_version: tuple = (0, 0, 0, 0)
    file_type: int = 0x01
    # StringFileInfo->StringTable
    company_name: str = "The XXX Inc."
    file_description: str = "XXX Starter Application"
    file_version_str: str = "0.0.0.000000"
    internal_name: str = "aaa"
    legal_copyright: str = "Copyright © 2020"
    legal_trademarks: str = "aaa® is a registered trademark of The XXX, Inc."
    original_filename: str = "aaa.exe"
    product_name: str = "AAA"
    product_version_str: str = "0.0.0.000000"
    # VarFileInfo
    translation: list = [1033, 1200]


class CheckItem:
    check_pos = 0
    state_msg = ""
    # 完整想
    integrity = ["VSVersionInfo",
                 "ffi=FixedFileInfo(",
                 "filevers=",
                 "prodvers=",
                 "mask=",
                 "flags=",
                 "OS=",
                 "fileType=",
                 "subtype=",
                 "date=",
                 "kids=[",
                 "StringFileInfo(",
                 "StringTable(",
                 "CompanyName",
                 "FileDescription",
                 "FileVersion",
                 "InternalName",
                 "LegalCopyright",
                 "OriginalFilename",
                 "ProductName",
                 "ProductVersion",
                 "Translation"
                 ]
    # 必须项
    must = ["filevers=",
            "prodvers=",
            "fileType=",

            "CompanyName",
            "FileDescription",
            "FileVersion",
            "InternalName",
            "LegalCopyright",
            "OriginalFilename",
            "ProductName",
            "ProductVersion",

            "Translation"
            ]
