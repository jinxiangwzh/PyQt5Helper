#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         xml_prj
# Description:  
# Author:       Great Master
# Date:         2020/4/27
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
import logging

from PyQt5.QtCore import QFile, QIODevice, QTextStream
from PyQt5.QtXml import QDomDocument, QDomProcessingInstruction, QDomElement, QDomText, QDomNode, QDomAttr, QDomComment, \
    QDomNodeList
from app_global import *


def new_project():
    """
    所有的命令都存储在属性'cmd'，参数都存储在属性’argv‘中，全局配置的词典key使用'cmd'，方便解析
    没有参数的命令,使能把命令的存储参数设置为True
    有参数的命令,使能就存储参数
    :return:
    """
    doc = QDomDocument("PyQt5Helper.prj")  # QDomDocument类
    instruction: QDomProcessingInstruction = doc.createProcessingInstruction("PyQt5Helper",
                                                                             "version={} " "encoding=\"UTF-8\"".format(version))
    doc.appendChild(instruction)

    root: QDomElement = doc.createElement("PyQt5Helper.prj-config")  # 创建general节点
    doc.appendChild(root)

    # 1. 通用选项
    item_list = project_item_dict.keys()
    for item in item_list:
        logging.debug(item)   # general,generate_what
        item_element: QDomElement = doc.createElement(item)  # 创建general节点
        root.appendChild(item_element)

        item_dict = project_item_dict[item]  # dist_path_cmd: ['./restore_dist', True, 'dist_path']},
        for child_item in item_dict.keys(): # dist_path_cmd
            save_item = item_dict[child_item]
            e: QDomElement = doc.createElement(save_item[2])  # child tag
            item_element.appendChild(e)  # --onedir,--onefile
            e.setAttribute("argv", save_item[0])
            e.setAttribute("cmd", child_item)
            e.setAttribute("state", save_item[1])

    return doc


def update_project_item(item='general', child_tag='dist_path', cmd=dist_path_cmd, file_name="test.xml"):
    # 打开文件
    file = QFile(file_name)  # 相对路径、绝对路径、资源路径都可以
    if not file.open(QFile.ReadOnly):
        return

    # 更新一个标签项, 如果知道xml的结构，直接定位到那个标签上定点更新
    # 或者用遍历的方法去匹配tagname或者attribut，value来更新
    doc = QDomDocument()
    if not doc.setContent(file):
        file.close()
        return
    file.close()

    root_element: QDomElement = doc.documentElement()
    dom_list: QDomNodeList = root_element.elementsByTagName(item)
    if dom_list.length() != 1:  # 必然存在一个
        logging.debug("解析出错")
    else:
        node: QDomNode = dom_list.item(0)
        general_e = node.toElement()  #
        old_node: QDomElement = general_e.firstChildElement(child_tag)
        new_node: QDomElement = general_e.firstChildElement(child_tag)
        new_node.setAttribute("cmd", cmd)
        new_node.setAttribute("argv", project_item_dict[cmd][0])
        new_node.setAttribute("state", project_item_dict[cmd][1])
        if general_e.replaceChild(new_node, old_node) is None:
            logging.debug("replace failure")

    if not file.open(QFile.WriteOnly | QFile.Truncate):
        return
    # 输出到文件
    out_stream = QTextStream(file)
    doc.save(out_stream, 4)  # 缩进4格
    file.close()

    return doc


def update_project(file_name="test.xml"):
    # 打开文件
    file = QFile(file_name)  # 相对路径、绝对路径、资源路径都可以
    if not file.open(QFile.ReadOnly):
        return

    # 更新一个标签项, 如果知道xml的结构，直接定位到那个标签上定点更新
    # 或者用遍历的方法去匹配tagname或者attribut，value来更新
    doc = QDomDocument()
    if not doc.setContent(file):
        file.close()
        return
    file.close()

    root_item_list = project_item_dict.keys()
    for root_item in root_item_list:
        logging.debug(root_item)  # general,generate_what
        root_element: QDomElement = doc.documentElement()
        dom_list: QDomNodeList = root_element.elementsByTagName(root_item)
        if dom_list.length() != 1:  # 必然存在一个,且只有一个
            logging.debug("解析出错")
        else:
            node: QDomNode = dom_list.item(0)
            root_e = node.toElement()  # general level
            for cmd_key in project_item_dict[root_item].keys():  # dist_path_cmd , one_dir_cmd,level
                logging.debug("tag " + str(project_item_dict[root_item][cmd_key][2]))
                old_node: QDomElement = root_e.firstChildElement(project_item_dict[root_item][cmd_key][2])
                if old_node.isNull():
                    logging.debug("parse error, no tag")
                new_node: QDomElement = root_e.firstChildElement(project_item_dict[root_item][cmd_key][2])
                new_node.setAttribute("cmd", cmd_key)
                new_node.setAttribute("argv", project_item_dict[root_item][cmd_key][0])
                new_node.setAttribute("state", project_item_dict[root_item][cmd_key][1])
                if root_e.replaceChild(new_node, old_node) is None:
                    logging.debug("replace failure")

    if not file.open(QFile.WriteOnly | QFile.Truncate):
        return
    # 输出到文件
    out_stream = QTextStream(file)
    doc.save(out_stream, 4)  # 缩进4格
    file.close()
    logging.debug("configure is updated")

    return doc


def save_project(doc: QDomDocument, file_name="./test.xml"):
    file = QFile(file_name)
    if not file.open(QIODevice.ReadWrite):
        return False
    out = QTextStream(file)
    out.setCodec("UTF-8")
    doc.save(out, 4, QDomNode.EncodingFromTextStream)
    file.close()

    return True


def open_project(file_name="./test.xml"):
    doc = QDomDocument()
    file = QFile(file_name)
    if not file.open(QIODevice.ReadOnly):
        return False

    if not doc.setContent(file):
        file.close()
        return False
    file.close()

    root: QDomElement = doc.documentElement()  # 读取根节点
    logging.debug(root.tagName())  # PyQt5Helper.prj-config

    root_item_list = project_item_dict.keys()
    for root_item in root_item_list:
        logging.debug(root_item)  # general,generate_what
        # general
        dom_item: QDomElement = root.firstChildElement(root_item)
        logging.debug(dom_item.tagName())  # general
        item: QDomElement = dom_item.firstChildElement()  # dist_path level
        while item.tagName() != '':
            logging.debug('read ' + item.tagName())  # dist_path
            argv = item.attribute('argv', 'None')
            logging.debug(argv)
            cmd = item.attribute('cmd', 'None')
            logging.debug(cmd)
            state = item.attribute('state', 'default')
            logging.debug(state)
            project_item_dict[root_item][cmd][0] = argv
            project_item_dict[root_item][cmd][1] = state   # 第三项不更新
            logging.debug("update default" + str(project_item_dict[root_item]))
            item: QDomElement = item.nextSiblingElement()


if __name__ == '__main__':
    # doc = new_project()
    doc = update_project()
    # save_xml(doc)
    # read_xml()