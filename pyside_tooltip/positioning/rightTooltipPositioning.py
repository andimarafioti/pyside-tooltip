from pyside_tooltip.positioning.tooltipPositioning import TooltipPositioning


class RightTooltipPositioning(TooltipPositioning):
	def showTooltip(self, tooltip, align, main_window):
		tooltipContainer = self._getContainerFor(tooltip, main_window)
		tooltipContainer.adjustSize()

		hoveredWidget = tooltip.hoveredWidget()

		x = self.mapToMainWindow(hoveredWidget, main_window).x() + hoveredWidget.width()
		y = align(hoveredWidget, tooltipContainer, main_window)

		tooltipContainer.move(x, y)
		tooltipContainer.show()

		return tooltipContainer

	def _getContainerFor(self, tooltip, main_window):
		container = super(RightTooltipPositioning, self)._getContainerFor(tooltip, main_window)
		container.setContentsMargins(tooltip.gap(), 0, 0, 0)
		container.layout().addWidget(tooltip.widget())
		return container

	def isPossibleFor(self, hovered_widget, tooltip, main_window):
		minimized = super(RightTooltipPositioning, self).isPossibleFor(hovered_widget, tooltip, main_window)
		floatingWidgetWidth = tooltip.widget().width()

		return minimized and self.mapToMainWindow(hovered_widget, main_window).x() + hovered_widget.width() + \
							 floatingWidgetWidth + tooltip.gap() < self.screenWidth(main_window)

