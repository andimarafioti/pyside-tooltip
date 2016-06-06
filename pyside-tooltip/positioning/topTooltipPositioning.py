from gui.tooltip.positioning.tooltipPositioning import TooltipPositioning


class TopTooltipPositioning(TooltipPositioning):
	def showTooltip(self, tooltip, align, main_window):
		tooltipContainer = self._getContainerFor(tooltip, main_window)
		tooltipContainer.adjustSize()

		tooltipHeight = tooltipContainer.height()
		hoveredWidget = tooltip.hoveredWidget()

		x = align(hoveredWidget, tooltipContainer)
		y = self.mapToMainWindow(hoveredWidget, main_window).y() - tooltipHeight

		tooltipContainer.move(x, y)

		tooltipContainer.show()

		return tooltipContainer

	def _getContainerFor(self, tooltip, main_window):
		container = super(TopTooltipPositioning, self)._getContainerFor(tooltip, main_window)
		container.setContentsMargins(0, 0, 0, tooltip.gap())
		container.layout().addWidget(tooltip.widget())
		return container

	def isPossibleFor(self, hovered_widget, tooltip, main_window):
		minimized = super(TopTooltipPositioning, self).isPossibleFor(hovered_widget, tooltip, main_window)
		floatingWidgetHeight = tooltip.widget().height()
		return minimized and self.mapToMainWindow(hovered_widget, main_window).y() - floatingWidgetHeight - tooltip.gap() > 0
