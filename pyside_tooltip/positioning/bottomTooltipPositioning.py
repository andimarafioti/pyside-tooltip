from gui.tooltip.positioning.tooltipPositioning import TooltipPositioning


class BottomTooltipPositioning(TooltipPositioning):

	def showTooltip(self, tooltip, align, main_window):
		tooltipContainer = self._getContainerFor(tooltip, main_window)
		tooltipContainer.adjustSize()

		hoveredWidget = tooltip.hoveredWidget()

		x = align(hoveredWidget, tooltipContainer)
		y = self.mapToMainWindow(hoveredWidget, main_window).y() + hoveredWidget.height()

		tooltipContainer.move(x, y)
		tooltipContainer.show()

		return tooltipContainer

	def _getContainerFor(self, tooltip, main_window):
		container = super(BottomTooltipPositioning, self)._getContainerFor(tooltip, main_window)
		container.setContentsMargins(0, tooltip.gap(), 0, 0)
		container.layout().addWidget(tooltip.widget())
		return container

	def isPossibleFor(self, hovered_widget, tooltip, main_window):
		minimized = super(BottomTooltipPositioning, self).isPossibleFor(hovered_widget, tooltip, main_window)
		floatingWidgetHeight = tooltip.widget().height()
		return minimized and self.mapToMainWindow(hovered_widget, main_window).y() + hovered_widget.height() + \
								 floatingWidgetHeight + tooltip.gap() < self.screenHeight(main_window)
