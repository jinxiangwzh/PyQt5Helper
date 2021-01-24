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

name = "XXX"
version = "0.2.0"  # 工程文件xml的版本
description = "PyQt5 Helper"
long_description = "PyQt5 Helper for build"

author = "Great Master"
author_email = "great_master_wu@163.com"
pyqt5_helper_version = "V1.0.0B"
cmd_path_sep = '&'  # SRC和dest之间可能是;分隔，所以这里特殊
semi_colon_sep = ';'

# 节点
# general下
version_cmd = '--version'
dist_path_cmd = '--distpath'
work_path_cmd = '--workpath'
no_confirm_cmd = '--noconfirm'
upx_dir_cmd = '--upx-dir'
ascii_cmd = '--ascii'
clean_cmd = '--clean'
log_level_cmd = '--log-level'

# 生成什么下
one_dir_cmd = '--onedir'
one_file_cmd = '--onefile'

spec_path_cmd = '--specpath'
app_name_cmd = '--name'

# 怎么打包哪里搜索
add_data_cmd = '--add-data'  # <SRC;DEST or SRC:DEST>
add_binary_cmd = '--add-binary'  # <SRC;DEST or SRC:DEST>
paths_cmd = '--paths'  # --paths DIR
hidden_import_cmd = '--hidden-import'  # --hidden-import MODULENAME,
additional_hooks_dir_cmd = '--additional-hooks-dir'  # --additional-hooks-dir HOOKSPATH
runtime_hook_cmd = '--runtime-hook'  # --runtime-hook RUNTIME_HOOKS
exclude_module_cmd = '--exclude-module'  # --exclude-module EXCLUDES
key_cmd = '--key'  # --key KEY

# 如何让生成
debug_cmd = '--debug'  # --debug <all,imports,bootloader,noarchive>
strip_cmd = '--strip'
noupx_cmd = '--noupx'
upx_exclude_cmd = '--upx-exclude'  # --upx-exclude FILE

# Windows和Mac OS X的特定选项
console_cmd = '--console'
windowed_cmd = '--windowed'
icon_cmd = '--icon'  # --icon <FILE.ico or FILE.exe,ID or FILE.icns>

# 6.Windows特定的选项
version_file_cmd = '--version-file'  # --version-file FILE
manifest_cmd = '--manifest'
resource_cmd = '--resource'  # --resource RESOURCE
uac_admin_cmd = '--uac-admin'  # --uac-admin
uac_uiaccess_cmd = '--uac-uiaccess'

# 7. Windows并排程序集搜索选项(高级)
win_private_assemblies_cmd = '--win-private-assemblies'
win_no_prefer_redirects_cmd = '--win-no-prefer-redirects'

# 9. 很少使用的特殊选项
runtime_tmpdir_cmd = '--runtime-tmpdir'  # --runtime-tmpdir PATH
bootloader_ignore_signals_cmd = '--bootloader-ignore-signals'

"""
有些参数在Pyinstaller中有默认值,这个时候命令状态True或False无意义
state主要时应用于在禁止命令时，依然使系统能够保留参数
列表第三项时tag name，为了方便处理也放在这,第三项不要修改
cmd:[argv,state,tag],打开项目时读入xml的内容到这个字典
"""
project_item_dict = {
    # general
    'general': {
        version_cmd: ['', False, 'version'],  # 查询版本号,参数填写版本号,state设置为False——不加入build
        dist_path_cmd: ['./dist', False, 'dist_path'],  # 有开关状态，但是关闭之后参数还是有默认值，开关状态也只是开关设置的状态
        work_path_cmd: ['./build', False, 'work_path'],  # 有开关状态，但是关闭之后参数还是有默认值，开关状态也只是开关设置的状态
        no_confirm_cmd: [None, True, 'no_confirm'],  # 没有参数，只有开启和关闭状态
        upx_dir_cmd: ['', False, 'upx_dir'],  # 这里有开关状态，但是关闭之后参数还是有默认值，开关状态也只是开关设置的状态，关闭有单独指令
        ascii_cmd: [None, False, 'ascii'],  # 没有参数，只有开启和关闭状态
        clean_cmd: [None, True, 'clean'],  # 没有参数，只有开启和关闭状态
        log_level_cmd: ['INFO', True, 'log_level'],  # 没有关闭状态，只能更改参数
    },
    # 生成什么
    'generate_what': {
        one_dir_cmd: [None, True, 'packet_dir'],  # default
        one_file_cmd: [None, False, 'packet_one_file'],  # 为了统一方便解析,这两个都加上,但是必须有一个为None,与GUI交互时要注意
        spec_path_cmd: ['./', False, 'spec_path'],  # default './'
        app_name_cmd: [name, False, 'app_name']
    },

    # What to bundle, where to search
    'bundle_and_search': {
        add_data_cmd: ['', False, 'data_path'],  # 有开关状态，但是关闭之后参数还是有默认值，开关状态也只是开关设置的状态
        add_binary_cmd: ['', False, 'binary_path'],  # 同上
        paths_cmd: ['', False, 'import_search_path'],
        hidden_import_cmd: ['', False, 'hidden_import'],
        additional_hooks_dir_cmd: ['', False, 'additional_hooks'],
        runtime_hook_cmd: ['', False, 'runtime_hooks'],
        exclude_module_cmd: ['', False, 'exclude_module'],
        key_cmd: ['', False, 'key_cmd'],
    },
    'window_special': {
        # window ad mac special
        console_cmd: ['', False, 'nowindowed'],
        windowed_cmd: ['', True, 'noconsole'],
        icon_cmd: ['', False, 'icon'],
        # # 6.Windows特定的选项
        version_file_cmd: ['', False, 'version_file'],
        # manifest_cmd = '--manifest'
        manifest_cmd: ['', False, 'manifest'],
        # resource_cmd = '--resource'  # --resource RESOURCE
        resource_cmd: ['', False, 'resource'],
        # uac_admin_cmd = '--uac-admin'  # --uac-admin
        uac_admin_cmd: ['', False, 'uac_admin'],
        # uac_uiaccess_cmd = '--uac-uiaccess'
        uac_uiaccess_cmd: ['', False, 'uac_uiaccess'],
        #
        # # 7. Windows并排程序集搜索选项(高级)
        # win_private_assemblies_cmd = '--win-private-assemblies'
        win_private_assemblies_cmd: ['', False, 'win_private_assemblies'],
        # win_no_prefer_redirects_cmd = '--win-no-prefer-redirects'
        win_no_prefer_redirects_cmd: ['', False, 'win_no_prefer_redirects'],
    },
    # 如何让生成

    'how_to_generate': {
        debug_cmd: ['', False, 'debug'],  # 参数为level
        strip_cmd: [None, False, 'strip'],
        noupx_cmd: [None, False, 'spec_path'],  # default './'
        upx_exclude_cmd: ["", False, 'upx_exclude']
    },

    # 只能通过本文件特定接口访问
    'none_cmd': {
        'project_path': ['', True, 'project_path'],  # 默认 '',只有这个可以改
        'py_file_path': ['', True, 'input_file_path']  # 默认 '',只有这个可以改
    }
}


# general
# TODO: delete later
def get_pyinstaller_version():
    try:
        cmd = ['pyinstaller', version_cmd]
        proc = os.subprocess.Popen(cmd)
        outs, errs = proc.communicate(timeout=15)
        logging.error(str(outs, errs))
        return outs
    except Exception as e:
        logging.error(str(e))


def set_dist_path(dist_path: str):
    project_item_dict['general'][dist_path_cmd][0] = dist_path


def get_dist_path():
    return project_item_dict['general'][dist_path_cmd][0]


def set_dist_state(state: bool):
    project_item_dict['general'][dist_path_cmd][1] = state


def get_dist_state():
    return project_item_dict['general'][dist_path_cmd][1]


# --workpath

def set_work_path(path: str):
    project_item_dict['general'][work_path_cmd][0] = path


def get_work_path():
    return project_item_dict['general'][work_path_cmd][0]


def set_work_path_state(state: bool):
    project_item_dict['general'][work_path_cmd][1] = state


def get_work_path_state():
    return project_item_dict['general'][work_path_cmd][1]


# --noconfirm
def set_no_confirm_state(state):
    project_item_dict['general'][no_confirm_cmd][1] = state


def get_no_confirm_state():
    return project_item_dict['general'][no_confirm_cmd][1]


# --upx-dir UPX_DIR
def set_upx_search_path_state(state):
    project_item_dict['general'][upx_dir_cmd][1] = state


def get_upx_search_path_state():
    return project_item_dict['general'][upx_dir_cmd][1]


def set_upx_search_path(path):
    project_item_dict['general'][upx_dir_cmd][0] = path


def get_upx_search_path():
    return project_item_dict['general'][upx_dir_cmd][0]


# --ascii
def set_not_support_unicode_state(state):
    project_item_dict['general'][ascii_cmd][1] = state


def get_not_support_unicode_state():
    return project_item_dict['general'][ascii_cmd][1]


# --clean
def set_clean_cache_state(state):
    project_item_dict['general'][clean_cmd][1] = state


def get_clean_cache_state():
    return project_item_dict['general'][clean_cmd][1]


# --log-level LEVEL
def set_log_level(level):
    project_item_dict['general'][log_level_cmd][0] = level


def get_log_level():
    return project_item_dict['general'][log_level_cmd][0]


#  在哪里搜索

def set_non_binary_path(non_bin_path: str):
    project_item_dict['bundle_and_search'][add_data_cmd][0] = non_bin_path


def get_non_binary_path():
    return project_item_dict['bundle_and_search'][add_data_cmd][0]


def set_non_binary_state(state: bool):
    project_item_dict['bundle_and_search'][add_data_cmd][1] = state


def get_non_binary_state():
    return project_item_dict['bundle_and_search'][add_data_cmd][1]


def set_binary_path(non_bin_path: str):
    project_item_dict['bundle_and_search'][add_binary_cmd][0] = non_bin_path


def get_binary_path():
    return project_item_dict['bundle_and_search'][add_binary_cmd][0]


def set_binary_state(state: bool):
    project_item_dict['bundle_and_search'][add_binary_cmd][1] = state


def get_binary_state():
    return project_item_dict['bundle_and_search'][add_binary_cmd][1]


# -p cmd,A path to search for imports (like using PYTHONPATH)

def set_import_search_path(search_path: str):
    project_item_dict['bundle_and_search'][paths_cmd][0] = search_path


def get_import_search_path():
    return project_item_dict['bundle_and_search'][paths_cmd][0]


def set_import_search_state(state: bool):
    project_item_dict['bundle_and_search'][paths_cmd][1] = state


def get_import_search_state():
    return project_item_dict['bundle_and_search'][paths_cmd][1]


# --hidden-import

def set_hidden_import_package(package_name: str):
    project_item_dict['bundle_and_search'][hidden_import_cmd][0] = package_name


def get_hidden_import_package():
    return project_item_dict['bundle_and_search'][hidden_import_cmd][0]


def set_hidden_import_state(state: bool):
    project_item_dict['bundle_and_search'][hidden_import_cmd][1] = state


def get_hidden_import_state():
    return project_item_dict['bundle_and_search'][hidden_import_cmd][1]


# additional_hooks_dir_cmd

def set_additional_hook(hook: str):
    project_item_dict['bundle_and_search'][additional_hooks_dir_cmd][0] = hook


def get_additional_hook():
    return project_item_dict['bundle_and_search'][additional_hooks_dir_cmd][0]


def set_additional_hook_state(state: bool):
    project_item_dict['bundle_and_search'][additional_hooks_dir_cmd][1] = state


def get_additional_hook_state():
    return project_item_dict['bundle_and_search'][additional_hooks_dir_cmd][1]


# runtime_hook_cmd

def set_runtime_hook(hook: str):
    project_item_dict['bundle_and_search'][runtime_hook_cmd][0] = hook


def get_runtime_hook():
    return project_item_dict['bundle_and_search'][runtime_hook_cmd][0]


def set_runtime_hook_state(state: bool):
    project_item_dict['bundle_and_search'][runtime_hook_cmd][1] = state


def get_runtime_hook_state():
    return project_item_dict['bundle_and_search'][runtime_hook_cmd][1]


# runtime_hook_cmd

def set_exclude_module(module: str):
    project_item_dict['bundle_and_search'][exclude_module_cmd][0] = module


def get_exclude_module():
    return project_item_dict['bundle_and_search'][exclude_module_cmd][0]


def set_exclude_module_state(state: bool):
    project_item_dict['bundle_and_search'][exclude_module_cmd][1] = state


def get_exclude_module_state():
    return project_item_dict['bundle_and_search'][exclude_module_cmd][1]


# key

def set_encrypt(module: str):
    project_item_dict['bundle_and_search'][key_cmd][0] = module


def get_encrypt():
    return project_item_dict['bundle_and_search'][key_cmd][0]


def set_encrypt_state(state: bool):
    project_item_dict['bundle_and_search'][key_cmd][1] = state


def get_encrypt_state():
    return project_item_dict['bundle_and_search'][key_cmd][1]


# generate_what
def set_spec_path(spec_path: str):
    project_item_dict['generate_what'][spec_path_cmd][0] = spec_path


def get_spec_path():
    return project_item_dict['generate_what'][spec_path_cmd][0]


def set_spec_state(state: bool):
    project_item_dict['generate_what'][spec_path_cmd][1] = state


def get_spec_state():
    return project_item_dict['generate_what'][spec_path_cmd][1]


# WINDOWS and MAC Special cmd

# --nowindowed
def set_no_windowed_state(state):
    # 设置未True开启控制台
    project_item_dict['window_special'][console_cmd][1] = state


def get_no_windowed_state():
    return project_item_dict['window_special'][console_cmd][1]


# --noconsole
def set_no_console_state(state):
    # 设置未True，关闭控制台
    project_item_dict['window_special'][windowed_cmd][1] = state


def get_no_console_state():
    return project_item_dict['window_special'][windowed_cmd][1]


# icon_cmd
def set_icon(icon: str):
    project_item_dict['window_special'][icon_cmd][0] = icon


def get_icon():
    return project_item_dict['window_special'][icon_cmd][0]


def set_icon_state(state: bool):
    project_item_dict['window_special'][icon_cmd][1] = state


def get_icon_state():
    return project_item_dict['window_special'][icon_cmd][1]


# # # 6.Windows特定的选项
# version_file_cmd:


def set_version_file(file: str):
    project_item_dict['window_special'][version_file_cmd][0] = file


def get_version_file():
    return project_item_dict['window_special'][version_file_cmd][0]


def set_version_file_state(state: bool):
    project_item_dict['window_special'][version_file_cmd][1] = state


def get_version_file_state():
    return project_item_dict['window_special'][version_file_cmd][1]


# # manifest_cmd = '--manifest'

def set_manifest_file(file: str):
    project_item_dict['window_special'][manifest_cmd][0] = file


def get_manifest_file():
    return project_item_dict['window_special'][manifest_cmd][0]


def set_manifest_file_state(state: bool):
    project_item_dict['window_special'][manifest_cmd][1] = state


def get_manifest_file_state():
    return project_item_dict['window_special'][manifest_cmd][1]


# # resource_cmd = '--resource'  # --resource RESOURCE


def set_resource_file(file: str):
    project_item_dict['window_special'][resource_cmd][0] = file


def get_resource_file():
    return project_item_dict['window_special'][resource_cmd][0]


def set_resource_file_state(state: bool):
    project_item_dict['window_special'][resource_cmd][1] = state


def get_resource_file_state():
    return project_item_dict['window_special'][resource_cmd][1]


# # uac_admin_cmd = '--uac-admin'  # --uac-admin

def set_uac_admin_state(state):
    project_item_dict['window_special'][uac_admin_cmd][1] = state


def get_uac_admin_state():
    return project_item_dict['window_special'][uac_admin_cmd][1]


def set_uac_uiaccess_state(state):
    project_item_dict['window_special'][uac_uiaccess_cmd][1] = state


def get_uac_uiaccess_state():
    return project_item_dict['window_special'][uac_uiaccess_cmd][1]


# # # 7. Windows并排程序集搜索选项(高级)
# # win_private_assemblies_cmd = '--win-private-assemblies'
def set_win_private_assemblies_state(state):
    project_item_dict['window_special'][win_private_assemblies_cmd][1] = state


def get_win_private_assemblies_state():
    return project_item_dict['window_special'][win_private_assemblies_cmd][1]


# # win_no_prefer_redirects_cmd = '--win-no-prefer-redirects'

def set_win_no_prefer_redirects_state(state):
    project_item_dict['window_special'][win_no_prefer_redirects_cmd][1] = state


def get_win_no_prefer_redirects_state():
    return project_item_dict['window_special'][win_no_prefer_redirects_cmd][1]


ONE_DIR_FORMAT = 0
ONE_FILE_FORMAT = 1


# 打包生成的格式
def set_build_format(fmt=ONE_DIR_FORMAT):
    if fmt == ONE_FILE_FORMAT:
        project_item_dict['generate_what'][one_file_cmd][1] = True
        project_item_dict['generate_what'][one_dir_cmd][1] = False
    else:
        project_item_dict['generate_what'][one_dir_cmd][1] = True
        project_item_dict['generate_what'][one_file_cmd][1] = False


def get_build_format():
    state = project_item_dict['generate_what'][one_file_cmd][1]
    if int(state):
        return ONE_FILE_FORMAT
    else:
        return ONE_DIR_FORMAT


def set_app_name(app_name: str):
    project_item_dict['generate_what'][app_name_cmd][0] = app_name


def get_app_name():
    return project_item_dict['generate_what'][app_name_cmd][0]


def set_app_name_state(state: bool):
    project_item_dict['generate_what'][app_name_cmd][1] = state


def get_app_name_state():
    # -> '0'/'1'
    return project_item_dict['generate_what'][app_name_cmd][1]


def set_project_path(prj_path: str):
    project_item_dict['none_cmd']["project_path"][0] = prj_path


def get_project_path():
    return project_item_dict['none_cmd']["project_path"][0]


# 如何生成

def set_debug_level(level: str):
    project_item_dict['how_to_generate'][debug_cmd][0] = level


def get_debug_level():
    return project_item_dict['how_to_generate'][debug_cmd][0]


def set_debug_level_state(state: bool):
    project_item_dict['how_to_generate'][debug_cmd][1] = state


def get_debug_level_state():
    return project_item_dict['how_to_generate'][debug_cmd][1]


# strip

def set_strip_state(state):
    project_item_dict['how_to_generate'][strip_cmd][1] = state


def get_strip_state():
    return project_item_dict['how_to_generate'][strip_cmd][1]


# UPX
def set_no_upx_state(state):
    project_item_dict['how_to_generate'][noupx_cmd][1] = state


def get_no_upx_state():
    return project_item_dict['how_to_generate'][noupx_cmd][1]


def set_exclude_upx_state(state):
    project_item_dict['how_to_generate'][upx_exclude_cmd][1] = state


def get_exclude_upx_state():
    return project_item_dict['how_to_generate'][upx_exclude_cmd][1]


def set_exclude_upx_file(files: str):
    project_item_dict['how_to_generate'][upx_exclude_cmd][0] = files


def get_exclude_upx_file():
    return project_item_dict['how_to_generate'][upx_exclude_cmd][0]


# none_cmd
def set_input_file_path(py_path: str):
    project_item_dict['none_cmd']["py_file_path"][0] = py_path


def get_input_file_path():
    return project_item_dict.get('none_cmd').get("py_file_path")[0]
