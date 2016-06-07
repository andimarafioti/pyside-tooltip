# coding: utf-8
from PySide.QtGui import QColor

from pyside_tooltip.tooltip import Tooltip
from pyside_tooltip.positioning.bottomTooltipPositioningWithArrow import BottomTooltipPositioningWithArrow
from pyside_tooltip.positioning.leftTooltipPositioningWithArrow import LeftTooltipPositioningWithArrow
from pyside_tooltip.positioning.nullTooltipPositioning import NullTooltipPositioning
from pyside_tooltip.positioning.rightTooltipPositioningWithArrow import RightTooltipPositioningWithArrow
from pyside_tooltip.positioning.topTooltipPositioningWithArrow import TopTooltipPositioningWithArrow

__author__ = 'Andres'


class TooltipWithArrow(Tooltip):
	ARROW_SIZE = 14

	# orientation:
	LEFT_POSITIONING = LeftTooltipPositioningWithArrow()
	TOP_POSITIONING = TopTooltipPositioningWithArrow()
	RIGHT_POSITIONING = RightTooltipPositioningWithArrow()
	BOTTOM_POSITIONING = BottomTooltipPositioningWithArrow()

	NULL_POSITIONING = NullTooltipPositioning()

	def __init__(self, hoverable_widget, positionings, main_window, gap=7, color_rgb=QColor(247, 247, 247)):
		super(TooltipWithArrow, self).__init__(hoverable_widget, positionings, main_window, gap=gap)
		self._color = color_rgb

	def color(self):
		return self._color

	def getWidget(self):
		raise NotImplementedError("Subclass responsibility")
