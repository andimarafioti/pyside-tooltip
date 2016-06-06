# coding: utf-8
from PySide.QtGui import QColor

from gui.tooltip.positioning.tooltipPositioningWithArrow import TooltipPositioningWithArrow

__author__ = 'Andres'


class LeftTooltipPositioningWithArrow(TooltipPositioningWithArrow):
	def showTooltip(self, tooltip, align, main_window):
		tooltipContainer = self._getContainerFor(tooltip, main_window)

		widget = tooltip.widget()
		hoveredWidget = tooltip.hoveredWidget()

		alignment = align(hoveredWidget, widget, main_window)
		arrow = self._getLeftOrRightArrow(alignment, tooltip, main_window)
		tooltipContainer.layout().addWidget(widget)
		tooltipContainer.layout().addWidget(arrow)
		tooltipContainer.adjustSize()
		tooltipWidth = tooltipContainer.width()

		x = self.mapToMainWindow(hoveredWidget, main_window).x() - tooltipWidth
		y = alignment

		tooltipContainer.move(x, y)
		tooltipContainer.show()

		return tooltipContainer

	def _getContainerFor(self, tooltip, main_window):
		container = super(LeftTooltipPositioningWithArrow, self)._getHorizontalContainerFor(tooltip, main_window)
		container.setContentsMargins(0, 0, tooltip.gap(), 0)
		return container

	def _getArrowStylesheet(self, color=QColor(255, 255, 255)):
		angle = 0
		cx = 1
		cy = 0.5
		color = "rgb({},{},{})".format(color.red(), color.green(), color.blue())
		return "background-color: qconicalgradient(cx:{}, cy:{}, angle:{}, stop:0 rgba(0,0,0,0), " \
				"stop:0.42 rgba(0,0,0,0), stop:0.43 {}, stop: 0.56 {}, stop:0.57 rgba(0, 0, 0, 0), " \
				"stop:1 rgba(0, 0, 0, 0))".format(cx, cy, angle, color, color)

	def isPossibleFor(self, hovered_widget, tooltip, main_window):
		minimized = super(LeftTooltipPositioningWithArrow, self).isPossibleFor(hovered_widget, tooltip, main_window)
		floatingWidgetWidth = tooltip.widget().width() + self.ARROW_SIZE

		return minimized and self.mapToMainWindow(hovered_widget, main_window).x() \
							 - floatingWidgetWidth - tooltip.gap() > 0