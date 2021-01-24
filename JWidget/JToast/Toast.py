#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 9:41
# @Author  : JAMO WOO
# email    : jinxiangwzh@163.com
# @File    : Toast.py
# Change Logs:
# Date           Author       Notes
# 2019/01/17     JAMO WOO     First Version
# 2019/02/13     JAMO WOO     fix the bug of chinese display
# 2019/02/18     JAMO WOO     fix the bug of multiple default value,modify default background color
# 2019/02/18     JAMO WOO     add judgement to parent type,fix the bug that toast is not stacked on top
# 2019/05/17     JAMO WOO     fix the bug of main thread exit and the toast not exit
# 2020/04/29     JAMO WOO     remove print
import logging
import threading

from PyQt5.QtCore import Qt, QRectF, pyqtProperty
from PyQt5.QtGui import QColor, QPainter, QFont, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication

LENGTH_SHORT = 2
LENGTH_LONG = 3.5


def make_text(parent, text, times,
              background_color=QColor("#555555"),
              text_color=Qt.white,
              font=QFont('SimSun', 15), *args, **kwargs):
    """
    note: can not be used in sub thread
    :param parent:
    :param text:
    :param times:
    :param background_color:
    :param text_color:
    :param font:
    :param args:
    :param kwargs:
    :return:
    """
    toast = Toast(parent=parent, text=text, show_times=times, background_color=background_color,
                  text_color=text_color, font=font)
    global toast_timer
    toast_timer = threading.Timer(times, toast_timeout, [toast])
    toast_timer.setDaemon(True)
    toast_timer.start()

    return toast


def toast_timeout(widget):
    widget.close()


class Toast(QWidget):
    _background_color = QColor("#00CD00")
    _text_color = Qt.white
    _font = QFont('SimSun', 50)
    _text = ''
    _parent = None
    _x_pos = 0
    _y_pos = 0  # 在窗口/屏幕的中心位置,必须放在widget_parent前 不然又变为0

    def __init__(self, parent: QWidget, text, show_times, background_color, text_color, font, *args, **kwargs):
        super(Toast, self).__init__(*args, **kwargs)
        self.widget_parent = parent
        self.background_color = background_color
        self.text_color = text_color
        self.text_font = font
        self.text = text
        self._min_width = 50
        self._min_height = 15
        self._show_times = show_times
        self._cb_times = 0

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)  # Qt.Tool  使窗口不再显示任务栏图标
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()
        self.fade_timer = threading.Timer(0.5, self.fade_timer_timeout)
        self.fade_timer.start()

    def paintEvent(self, event):
        # 调用父类的绘图事件
        super(Toast, self).paintEvent(event)
        try:
            self.raise_()
            height = self.get_font_size()
            # 编码为二进制并计算长度,不然中英文会导致长度不一或者错误
            width = len(self._text.encode('utf-8', "ignore")) * height * 0.8
            if height < self._min_height:
                height = self._min_height
            else:
                height = self._min_height * 2

            if width < self._min_width:
                width = self._min_width
            self.resize(width, height)
            if self._x_pos != 0 and self._y_pos != 0:
                self.move(self._x_pos - width / 2, self._y_pos - height / 2)
            painter = QPainter(self)
            # 设置渲染提示——反锯齿
            painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
            rectangle = QRectF(0, 0, width, height)
            brush = QBrush(QColor(self._background_color), Qt.SolidPattern)
            painter.setBrush(brush)
            painter.setPen(QPen(QColor(self._background_color)))
            # 为替换矩形的每个角而绘制的四分之一椭圆的 x/y 半径。
            painter.drawRoundedRect(rectangle, height / 2, height / 2, Qt.AbsoluteSize)
            self._draw_text(painter, rectangle, self._text)
        except Exception as e:
            logging.error(e)

    def _draw_text(self, painter: QPainter, rect: QRectF, text: str):
        # 绘制文字
        painter.save()
        painter.setPen(self._text_color)
        painter.setFont(self._font)
        painter.drawText(rect, Qt.AlignCenter, text)
        painter.restore()

    @pyqtProperty(QWidget)
    def widget_parent(self):
        return self._parent

    @widget_parent.setter
    def widget_parent(self, widget: QWidget):
        self._parent = widget
        if widget is not None and isinstance(widget, QWidget) is False:
            raise TypeError("Parent type error")
        try:
            if self._parent is None:
                desktop = QApplication.desktop()
                screen_rect = desktop.screenGeometry()
                self._x_pos = screen_rect.width() / 2
                self._y_pos = screen_rect.height() / 2
                self.move(self._x_pos, self._y_pos)
            else:
                self._x_pos = self._parent.pos().x() + self._parent.size().width() / 2
                self._y_pos = self._parent.pos().y() + self._parent.size().height() / 2
                self.move(self._x_pos, self._y_pos)
            self.update()
        except Exception as e:
            logging.error(e)

    @pyqtProperty(QColor)
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, text_color: QColor):
        if self._text_color != text_color:
            self._text_color = text_color
            self.update()

    @pyqtProperty(QColor)
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, color: QColor):
        if self._background_color != color:
            self._background_color = color
            self.update()

    @pyqtProperty(QFont)
    def text_font(self):
        return self._font

    @text_font.setter
    def text_font(self, font: QFont):
        self._font = font

    @pyqtProperty(str)
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text
        self.update()

    def get_font_size(self):
        # Returns -1 if the font size was specified in pixels.
        font = self._font.pointSize()
        if font != -1:
            return font
        # Returns -1 if the size was set with setPointSize() or setPointSizeF().
        font = self._font.pixelSize()
        if font != -1:
            return font
        # Returns -1 if the font size was specified in pixels.
        font = self._font.pointSizeF()
        if font != -1:
            return font
        raise ValueError("No Font size")

    def fade_timer_timeout(self):
        self.setWindowOpacity(1 - 1 / self._show_times * self._cb_times / 10)
        self._cb_times += 1
        if self._cb_times < self._show_times / 0.2:
            self.fade_timer = threading.Timer(0.1, self.fade_timer_timeout)
            self.fade_timer.start()
        else:
            self.fade_timer.cancel()
