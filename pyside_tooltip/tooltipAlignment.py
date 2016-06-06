class TooltipAlignment(object):
	@staticmethod
	def mapToMainWindow(widget, mainWindow):
		return widget.parent().mapTo(mainWindow, widget.pos())

	@classmethod
	def alignToBottom(cls, hoveredWidget, tooltip, mainWindow):
		return min(cls.mapToMainWindow(hoveredWidget, mainWindow).y(), mainWindow.height() - tooltip.height())

	@classmethod
	def alignToVCenter(cls, hoveredWidget, tooltip, mainWindow):
		return max(cls.mapToMainWindow(hoveredWidget, mainWindow).y() + ((hoveredWidget.height() - tooltip.height()) / 2), 0)

	@classmethod
	def alignToHCenter(cls, hoveredWidget, tooltip, mainWindow):
		return max(cls.mapToMainWindow(hoveredWidget, mainWindow).x() + (hoveredWidget.width() - tooltip.width()) / 2, 0)

	@classmethod
	def alignToRight(cls, hoveredWidget, tooltip, mainWindow):
		return min(cls.mapToMainWindow(hoveredWidget, mainWindow).x(), mainWindow.width() - tooltip.width())

	@classmethod
	def alignToLeft(cls, hoveredWidget, tooltip, mainWindow):
		return max(cls.mapToMainWindow(hoveredWidget, mainWindow).x() + hoveredWidget.width() - tooltip.width(), 0)

	@classmethod
	def alignToTop(cls, hoveredWidget, tooltip, mainWindow):
		return max(cls.mapToMainWindow(hoveredWidget, mainWindow).y() + hoveredWidget.height() - tooltip.height(), 0)
