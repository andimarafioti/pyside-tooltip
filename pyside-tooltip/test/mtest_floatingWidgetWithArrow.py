# coding: utf-8
import logging
import sys

from PySide import QtGui
from PySide.QtCore import Qt
from mock import Mock

from gui.tooltip.tooltipAlignment import TooltipAlignment
from models.esttelaServices import Esttela
from gui.tooltip.tooltipWithArrow import TooltipWithArrow
from gui.generic.flatButton import FlatButton

__author__ = 'Andres'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class HoverableButtonTooltip(TooltipWithArrow):
	def getWidget(self):
		button = FlatButton()
		button.setText('World!')
		button.clicked.connect(self.onButton1Click)
		button.setFlat(True)
		button.setFixedSize(200, 50)
		button.setAttribute(Qt.WA_StyledBackground)
		button.setStyleSheet("background-color: rgb(0, 255, 0);")

		return button

	def onButton1Click(self):
		print "bubalabadubdub"


class HoverableButton(QtGui.QPushButton):
	def __init__(self):
		super(HoverableButton, self).__init__()
		self.setContentsMargins(0, 0, 0, 0)
		self.tooltip = HoverableButtonTooltip(self,
											[(TooltipWithArrow.TOP_POSITIONING, TooltipAlignment.alignToRight),
											 (TooltipWithArrow.RIGHT_POSITIONING, TooltipAlignment.alignToTop)],
											gap=10)


class HoverableButton1(QtGui.QPushButton):
	def __init__(self):
		super(HoverableButton1, self).__init__()
		self.setContentsMargins(0, 0, 0, 0)
		self.tooltip = HoverableButtonTooltip(self,
											[(TooltipWithArrow.BOTTOM_POSITIONING, TooltipAlignment.alignToLeft),
											 (TooltipWithArrow.LEFT_POSITIONING, TooltipAlignment.alignToBottom)],
											gap=20)


def main():
	class Window(QtGui.QWidget):
		def __init__(self):
			""""""
			super(Window, self).__init__()
			self.resize(1000, 600)
			self.initUi()

		def onButton1Click(self):
			print "Clock"

		def onButton2Click(self):
			print "click"

		def initUi(self):
			layout = QtGui.QVBoxLayout()
			layout.setContentsMargins(0, 0, 0, 0)

			self.button2 = HoverableButton()
			self.button2.setText("Top|Right")
			self.button2.clicked.connect(self.onButton2Click)

			self.button1 = HoverableButton1()
			self.button1.setText("Bottom|Left")

			layout.addWidget(self.button2)
			layout.addWidget(self.button1)
			layout.setAlignment(self.button2, Qt.AlignCenter | Qt.AlignBottom)
			layout.setAlignment(self.button1, Qt.AlignCenter | Qt.AlignTop)
			self.setLayout(layout)

	app = QtGui.QApplication(sys.argv)
	w = Window()
	Esttela.presenter = Mock(view=w)
	w.show()
	app.exec_()


if __name__ == '__main__':
	main()
