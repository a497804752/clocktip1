# -*- coding:UTF-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *


class clockForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DN时钟盘小助手v0.1")
        self.timer = QTimer()
        # 设置窗口计时器
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def paintEvent(self, event):

        hourColor = QColor(255,0,0)
        minColor = QColor(0, 127, 127, 150)

        side = min(self.width(), self.height())

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)  # painter坐标系原点移至widget中央
        painter.scale(side / 200, side / 200)  # 缩放painterwidget坐标系，使绘制的时钟位于widge中央,即钟表支持缩放

        # 绘制小时和分钟刻度线
        painter.save()
        for i in range(0, 60):
            if (i % 5) != 0:
                painter.setPen(minColor)
                painter.drawLine(92, 0, 96, 0)  # 绘制分钟刻度线
            else:
                painter.setPen(hourColor)
                painter.drawLine(88, 0, 96, 0)  # 绘制小时刻度线
            painter.rotate(360 / 60)
        painter.restore()

        # 绘制小时数字
        painter.save()
        font = painter.font()
        font.setBold(True)
        painter.setFont(font)
        pointSize = font.pointSize()
        painter.setPen(hourColor)
        nhour = 0
        radius = 100
        for i in range(0, 12):
            nhour = i + 3  # 按QT-Qpainter的坐标系换算，3小时的刻度线对应坐标轴0度
            if nhour > 12:
                nhour = nhour - 12

            x = radius * 0.8 * cos(i * 30 * pi / 180.0) - pointSize
            y = radius * 0.8 * sin(i * 30 * pi / 180.0) - pointSize / 2.0
            width = pointSize * 2
            height = pointSize
            painter.drawText(QRectF(x, y, width, height), Qt.AlignCenter, str(nhour))
        painter.restore()

    def closeEvent(self, event):

        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            os._exit(0)
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = clockForm()
    form.setWindowOpacity(0.5)
    form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    form.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint| QtCore.Qt.Tool |QtCore.Qt.WindowMaximizeButtonHint|
         QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)
    form.show()
    form.resize(200,200)
    sys.exit(app.exec_())
