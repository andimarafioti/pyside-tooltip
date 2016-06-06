# coding: utf-8
import logging

from PySide.QtGui import QWidget

from pyside_tooltip.positioning.tooltipPositioning import TooltipPositioning

__author__ = 'Andres'


class NullTooltipPositioning(TooltipPositioning):
	def isPossibleFor(self, hovered_widget, tooltip, main_window):
		return True

	def showTooltip(self, tooltip, align, main_window):
		logging.warning("The floating widget of type %s with reference widget of type %s, could not be deployed", type(tooltip.widget()).__name__, type(tooltip.hoveredWidget()).__name__)
		widget = QWidget()
		widget.resize(0, 0)  # De esta forma el widget nunca va a contener al mouse
		return widget