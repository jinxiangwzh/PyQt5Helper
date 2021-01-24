#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         normal_style
# Description:  
# Author:       Great Master
# Date:         2020/4/26
# Change Logs:
# Date           Author       Notes
# -------------------------------------------------------------------------------
from css.resource_css import *

normal_style = """
QGroupBox {
    /*background-color: red;*/
    border: 0px none;
    margin-top:16px;
    font: bold 12px;
}

QGroupBox::title{
    /*background-color: green;*/
    margin: -16px 0px 0px 0px;
    /*font: bold 14px;*/
    height:30px;
}

QGroupBox::indicator{
    /*background-color: blue;*/
    width:10px;
    height:10px;
    border: 1px solid black;
    border-radius:5px;
}

QGroupBox::indicator:checked{
    image: url(":/css/icon/checked.png");
    width:10px;
    height:10px;
    border: 0px none;
}

QFrame#left_menu_frame{
    background-color:rgb(252, 255, 248);
    border: 0px none;
}

QFrame{
    border: 0px none;
}

/*选中的列表更改背景色*/
QToolButton:checked{ 
    background-color: #FFE4E1;
    border: 0px none;
    width:100 px;
    height:30px;
    margin: 0px 0px 0px 0px;
}

QToolButton{ 
    width:100 px;
    height:30px;
    margin: 0px 0px 0px 0px;
}

QPushButton#start_build_pb{ 
    width: 60px;
    height:60px;
    border-radius:30px;
    background-color:green;
    Font:bold;
}
QPushButton#start_build_pb:pressed{ 
    width: 60px;
    height:60px;
    border-radius:30px;
    background-color:green;
    Font:bold;
}

QPushButton#start_build_pb:hover:!pressed{ 
    width: 60px;
    height:60px;
    border-radius:30px;
    background-color:grey;
    Font:bold;
}

QPushButton#start_build_pb:checked{ 
    width: 60px;
    height:60px;
    border-radius:30px;
    background-color:red;
    Font:bold;
}

QPushButton#start_build_pb:!checked{ 
    width: 60px;
    height:60px;
    border-radius:30px;
    background-color:green;
    Font:bold;
}
"""