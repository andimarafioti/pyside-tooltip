# coding: utf-8
from PySide.QtGui import QColor

from gui.tooltip.tooltip import Tooltip
from gui.tooltip.positioning.bottomTooltipPositioningWithArrow import BottomTooltipPositioningWithArrow
from gui.tooltip.positioning.leftTooltipPositioningWithArrow import LeftTooltipPositioningWithArrow
from gui.tooltip.positioning.nullTooltipPositioning import NullTooltipPositioning
from gui.tooltip.positioning.rightTooltipPositioningWithArrow import RightTooltipPositioningWithArrow
from gui.tooltip.positioning.topTooltipPositioningWithArrow import TopTooltipPositioningWithArrow

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
