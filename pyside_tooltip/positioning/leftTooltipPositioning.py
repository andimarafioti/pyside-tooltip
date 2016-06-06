from pyside_tooltip.positioning.tooltipPositioning import TooltipPositioning


class LeftTooltipPositioning(TooltipPositioning):
	def showTooltip(self, tooltip, align, main_window):
		tooltipContainer = self._getContainerFor(tooltip, main_window)
		tooltipContainer.adjustSize()

		tooltipWidth = tooltipContainer.width()

		hoveredWidget = tooltip.hoveredWidget()

		x = self.mapToMainWindow(hoveredWidget, main_window).x() - tooltipWidth
		y = align(hoveredWidget, tooltipContainer, main_window)

		tooltipContainer.move(x, y)
		tooltipContainer.show()

		return tooltipContainer

	def _getContainerFor(self, tooltip, main_window):
		container = super(LeftTooltipPositioning, self)._getContainerFor(tooltip, main_window)
		container.setContentsMargins(0, 0, tooltip.gap(), 0)
		container.layout().addWidget(tooltip.widget())
		return container

	def isPossibleFor(self, hovered_widget, tooltip, main_window):
		minimized = super(LeftTooltipPositioning, self).isPossibleFor(hovered_widget, tooltip, main_window)
		floatingWidgetWidth = tooltip.widget().width()
		return minimized and self.mapToMainWindow(hovered_widget, main_window).x() - floatingWidgetWidth - tooltip.gap() > 0
