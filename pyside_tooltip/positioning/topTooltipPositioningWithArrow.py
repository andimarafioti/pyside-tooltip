# coding: utf-8

from PySide.QtGui import QColor

from pyside_tooltip.positioning.tooltipPositioningWithArrow import TooltipPositioningWithArrow

__author__ = 'Andres'


class TopTooltipPositioningWithArrow(TooltipPositioningWithArrow):
	def showTooltip(self, tooltip, align, main_window):
		widget = tooltip.widget()
		hoveredWidget = tooltip.hoveredWidget()

		alignment = align(hoveredWidget, widget, main_window)
		tooltipContainer = self._getContainerFor(tooltip, main_window)
		tooltipContainer.layout().addWidget(tooltip.widget())
		tooltipContainer.layout().addWidget(self._getTopOrBottomArrow(alignment, tooltip, main_window))
		tooltipContainer.adjustSize()

		tooltipHeight = tooltipContainer.height()

		x = alignment
		y = self.mapToMainWindow(hoveredWidget, main_window).y() - tooltipHeight

		tooltipContainer.move(x, y)
		tooltipContainer.show()

		return tooltipContainer

	def _getContainerFor(self, tooltip, main_window):
		container = super(TopTooltipPositioningWithArrow, self)._getContainerFor(tooltip, main_window)
		container.setContentsMargins(0, 0, 0, tooltip.gap())
		return container

	def _getArrowStylesheet(self, color=QColor(255, 255, 255)):
		angle = 270
		cx = 0.5
		cy = 1

		color = "rgb({},{},{})".format(color.red(), color.green(), color.blue())

		return "background-color: qconicalgradient(cx:{}, cy:{}, angle:{}, stop:0 rgba(0,0,0,0), " \
				"stop:0.42 rgba(0,0,0,0), stop:0.43 {}, stop: 0.56 {}, stop:0.57 rgba(0, 0, 0, 0), " \
				"stop:1 rgba(0, 0, 0, 0))".format(cx, cy, angle, color, color)

	def isPossibleFor(self, hovered_widget, tooltip, main_window):
		minimized = super(TopTooltipPositioningWithArrow, self).isPossibleFor(hovered_widget, tooltip, main_window)
		floatingWidgetHeight = tooltip.widget().height() + self.ARROW_SIZE

		return minimized and self.mapToMainWindow(hovered_widget, main_window).y() \
							 - floatingWidgetHeight - tooltip.gap() > 0
