# coding: utf-8
from PySide.QtCore import Qt
from PySide.QtGui import QLabel, QWidget, QHBoxLayout, QVBoxLayout

from pyside_tooltip.positioning.tooltipPositioning import TooltipPositioning
from pyside_tooltip.tooltipAlignment import TooltipAlignment

__author__ = 'Andres'


class TooltipPositioningWithArrow(TooltipPositioning):
	ARROW_MARGIN = 7
	ARROW_SIZE = 11
	ARROW_ODD_SIZE = 15

	def _getTopOrBottomArrow(self, alignment, tooltip, main_window):
		arrow_alignment = TooltipAlignment.mapToMainWindow(tooltip.hoveredWidget(), main_window).x() - alignment + \
						  tooltip.hoveredWidget().width() / 2 - self.ARROW_ODD_SIZE / 2

		if arrow_alignment > tooltip.widget().width():
			arrow_alignment = tooltip.widget().width() - self.ARROW_ODD_SIZE

		self._arrow = QWidget()
		self._arrow.setLayout(self._getTopOrBottomArrowLayout(arrow_alignment))

		self._label_arrow = QLabel()
		self._label_arrow.setStyleSheet(self._getArrowStylesheet(tooltip.color()))
		self._label_arrow.setFixedWidth(self.ARROW_ODD_SIZE)
		self._label_arrow.setFixedHeight(self.ARROW_SIZE)

		self._arrow.layout().addWidget(self._label_arrow)
		return self._arrow

	def _getTopOrBottomArrowLayout(self, arrow_alignment):
		self._arrow_layout = QHBoxLayout()
		self._arrow_layout.setAlignment(Qt.AlignLeft)
		self._arrow_layout.setContentsMargins(arrow_alignment, 0, 0, 0)
		return self._arrow_layout

	def _getLeftOrRightArrow(self, alignment, tooltip, main_window):
		arrow_alignment = TooltipAlignment.mapToMainWindow(tooltip.hoveredWidget(), main_window).y() \
						  - alignment + tooltip.hoveredWidget().height() / 2 - self.ARROW_ODD_SIZE / 2

		if arrow_alignment > tooltip.widget().height():
			arrow_alignment = tooltip.widget().height() - self.ARROW_ODD_SIZE

		self._arrow = QWidget()
		self._arrow.setLayout(self._getLeftOrRightArrowLayout(arrow_alignment))

		self._label_arrow = QLabel()
		self._label_arrow.setStyleSheet(self._getArrowStylesheet(tooltip.color()))
		self._label_arrow.setFixedWidth(self.ARROW_SIZE)
		self._label_arrow.setFixedHeight(self.ARROW_ODD_SIZE)

		self._arrow.layout().addWidget(self._label_arrow)
		return self._arrow

	def _getLeftOrRightArrowLayout(self, arrow_alignment):
		self._arrow_layout = QVBoxLayout()
		self._arrow_layout.setAlignment(Qt.AlignTop)
		self._arrow_layout.setContentsMargins(0, arrow_alignment, 0, 0)
		return self._arrow_layout

	def _getArrowStylesheet(self, color="rgb(255, 255, 255)"):
		raise NotImplementedError("Subclass responsibility")

	def showTooltip(self, tooltip, align, main_window):
		raise NotImplementedError("Subclass responsibility")
