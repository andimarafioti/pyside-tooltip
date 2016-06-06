# coding: utf-8
from PySide.QtGui import QColor

from pyside_tooltip.positioning.tooltipPositioningWithArrow import TooltipPositioningWithArrow

__author__ = 'Andres'


class BottomTooltipPositioningWithArrow(TooltipPositioningWithArrow):
	def showTooltip(self, tooltip, align, main_window):
		tooltipContainer = self._getContainerFor(tooltip, main_window)

		widget = tooltip.widget()
		hoveredWidget = tooltip.hoveredWidget()

		alignment = align(hoveredWidget, widget, main_window)
		arrow = self._getTopOrBottomArrow(alignment, tooltip, main_window)
		tooltipContainer.layout().addWidget(arrow)
		tooltipContainer.layout().addWidget(widget)
		tooltipContainer.adjustSize()

		x = alignment
		y = self.mapToMainWindow(hoveredWidget, main_window).y() + hoveredWidget.height()

		tooltipContainer.move(x, y)
		tooltipContainer.show()

		return tooltipContainer

	def _getContainerFor(self, tooltip, main_window):
		container = super(BottomTooltipPositioningWithArrow, self)._getContainerFor(tooltip, main_window)
		container.setContentsMargins(0, tooltip.gap(), 0, 0)
		return container

	def _getArrowStylesheet(self, color=QColor(255, 255, 255)):
		angle = 90
		cx = 0.5
		cy = 0
		color = "rgb({},{},{})".format(color.red(), color.green(), color.blue())
		return "background-color: qconicalgradient(cx:{}, cy:{}, angle:{}, stop:0 rgba(0,0,0,0), " \
				"stop:0.42 rgba(0,0,0,0), stop:0.43 {}, stop: 0.56 {}, stop:0.57 rgba(0, 0, 0, 0), " \
				"stop:1 rgba(0, 0, 0, 0))".format(cx, cy, angle, color, color)

	def isPossibleFor(self, hovered_widget, tooltip, main_window):
		minimized = super(BottomTooltipPositioningWithArrow, self).isPossibleFor(hovered_widget, tooltip, main_window)
		floatingWidgetHeight = tooltip.widget().height()
		return minimized and self.mapToMainWindow(hovered_widget, main_window).y() + hovered_widget.height() + \
							 floatingWidgetHeight + tooltip.gap() < self.screenHeight(main_window)

