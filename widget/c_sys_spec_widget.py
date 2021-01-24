import logging
import platform

from PyQt5.QtWidgets import QFrame, QWidget, QHBoxLayout, QFileDialog

from JWidget.JToast import Toast
from app_global import *
from widget.linux_spec_widget_ui import Ui_linux_spec_widget
from widget.sub_win_special.c_version_file import VersionFile
from widget.win_spec_widget_ui import Ui_win_spec_widget


class SysSpecWidget(QFrame):
    def __init__(self):
        super(SysSpecWidget, self).__init__()
        logging.info(platform.system())
        if platform.system() == "Windows":
            logging.debug("use windows system")
            try:
                self.sys_special = WindowsSpecWidget()
            except Exception as e:
                logging.error(e)
        elif platform.system() == 'Linux':
            logging.debug("use linux system")
            self.sys_special = Ui_linux_spec_widget()
        hl = QHBoxLayout()
        self.setLayout(hl)
        hl.addWidget(self.sys_special)


class WindowsSpecWidget(QWidget):
    def __init__(self):
        super(WindowsSpecWidget, self).__init__()
        self.ui = Ui_win_spec_widget()
        self.ui.setupUi(self)
        self.load_config_information()
        self._signal_init()
        self.version_file_widget = None

    def _signal_init(self):
        # 控制台
        self.ui.open_console_rb.toggled.connect(self.on_console_state_toggled)
        # 图标
        self.ui.select_icon_pb.clicked.connect(self.on_select_icon_button_clicked)
        self.ui.icon_path_le.textChanged.connect(self.on_icon_path_changed)
        self.ui.icon_gb.toggled.connect(self.on_icon_state_toggle)
        # 选择版本文件
        self.ui.select_version_file_pb.clicked.connect(self.on_select_version_file_button_clicked)
        self.ui.version_file_le.textChanged.connect(self.on_version_file_text_changed)
        self.ui.edit_version_file_pb.clicked.connect(self.on_edit_version_file_button_clicked)
        self.ui.version_file_gb.toggled.connect(self.on_version_file_state_toggle)
        # manifest file
        self.ui.selcet_manifest_pb.clicked.connect(self.on_select_manifest_button_clicked)
        self.ui.manifest_path_le.textChanged.connect(self.on_manifest_file_changed)
        self.ui.manifest_gb.toggled.connect(self.on_manifest_state_toggle)

        # 资源文件
        self.ui.resource_gb.clicked.connect(self.on_resource_groupbox_clicked)
        # UAC
        self.ui.uac_admin_cb.setChecked(int(get_uac_admin_state()))
        self.ui.uac_uiaccess_cb.setChecked(int(get_uac_uiaccess_state()))
        # advanced
        self.ui.private_assembies_cb.setChecked(int(get_win_private_assemblies_state()))
        self.ui.no_prefer_redirects_cb.setChecked(int(get_win_no_prefer_redirects_state()))

    def load_config_information(self):
        # 控制台
        state = get_no_windowed_state()
        logging.info("load console state:" + str(state))
        # TODO: 明明互斥，这里用同一个控件设置True和False却不可以，可能是缺少一个默认状态
        if int(state):
            self.ui.open_console_rb.setChecked(True)
        else:
            self.ui.close_console_rb.setChecked(True)
        # icon
        state = get_icon_state()
        self.ui.icon_gb.setChecked(int(state))
        self.ui.icon_path_le.setText(get_icon())
        # version file
        state = get_version_file_state()
        self.ui.version_file_gb.setChecked(int(state))
        self.ui.version_file_le.setText(get_version_file())
        # manifest file
        state = get_manifest_file_state()
        self.ui.manifest_gb.setChecked(int(state))
        self.ui.manifest_path_le.setText(get_manifest_file())
        # 资源文件

        # UAC
        self.ui.uac_admin_cb.toggled.connect(self.on_uac_admin_toggle)
        self.ui.uac_uiaccess_cb.toggled.connect(self.on_uac_uiaccess_toggle)

        # advanced
        self.ui.private_assembies_cb.toggled.connect(self.on_private_assembies_toggle)
        self.ui.no_prefer_redirects_cb.toggled.connect(self.on_prefer_redirects_toggle)

    @staticmethod
    def on_console_state_toggled(state):
        logging.info("open console state:" + str(state))
        if state:
            set_no_windowed_state(True)
            set_no_console_state(False)
        else:
            set_no_windowed_state(False)
            set_no_console_state(True)

    def on_select_icon_button_clicked(self):
        img_fmt = "Image(*.ico *.icns);;" \
                  "exe(*.exe);;" \
                  "All files (*)"
        def_dir = os.getcwd()
        file_path, fmt = QFileDialog.getOpenFileName(self, '选择文件', def_dir, img_fmt)
        self.ui.icon_path_le.setText(file_path)

    @staticmethod
    def on_icon_path_changed(path):
        logging.info("select ico:" + path)
        set_icon(path)

    @staticmethod
    def on_icon_state_toggle(state):
        logging.info("icon state:" + str(state))
        set_icon_state(state)

    def on_select_version_file_button_clicked(self):
        # 选中版本文件
        img_fmt = "文本(*.txt);;" \
                  "All files (*)"
        def_dir = os.getcwd()
        file_path, fmt = QFileDialog.getOpenFileName(self, '选择文件', def_dir, img_fmt)
        self.ui.version_file_le.setText(file_path)

    @staticmethod
    def on_version_file_text_changed(text):
        logging.info("version file changed:" + text)
        set_version_file(text)

    def on_edit_version_file_button_clicked(self):
        try:
            self.version_file_widget = VersionFile(self.ui.version_file_le)
            self.version_file_widget.show()
        except Exception as e:
            logging.error(e)

    @staticmethod
    def on_version_file_state_toggle(state):
        logging.info("version file gp changed:" + str(state))
        set_version_file_state(state)

    def on_select_manifest_button_clicked(self):
        # 选中版本资源文件
        img_fmt = "XML(*.xml);;" \
                  "All files (*)"
        def_dir = os.getcwd()
        file_path, fmt = QFileDialog.getOpenFileName(self, '选择文件', def_dir, img_fmt)
        logging.info("manifest set to:" + file_path)
        self.ui.manifest_path_le.setText(file_path)

    @staticmethod
    def on_manifest_file_changed(text):
        logging.info("manifest file changed:" + text)
        set_manifest_file(text)

    @staticmethod
    def on_manifest_state_toggle(state):
        logging.info("manifest file gp changed:" + str(state))
        set_manifest_file_state(state)

    @staticmethod
    def on_uac_admin_toggle(state):
        logging.info("uac admin:" + str(state))
        set_uac_admin_state(state)

    @staticmethod
    def on_uac_uiaccess_toggle(state):
        logging.info("uac uiaccess:" + str(state))
        set_uac_uiaccess_state(state)

    # advanced
    @staticmethod
    def on_private_assembies_toggle(state):
        logging.info("win private assembies:" + str(state))
        set_win_private_assemblies_state(state)

    @staticmethod
    def on_prefer_redirects_toggle(state):
        logging.info("win prefer redirects:" + str(state))
        set_win_no_prefer_redirects_state(state)

    def on_resource_groupbox_clicked(self):
        self.ui.resource_gb.setChecked(False)
        Toast.make_text(None, "功能还未加入，如有需要请联系作者", Toast.LENGTH_SHORT)
