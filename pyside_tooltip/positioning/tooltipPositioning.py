from PySide.QtGui import QWidget, QVBoxLayout, QHBoxLayout


class TooltipPositioning(object):
	def mapToMainWindow(self, widget, main_window):
		return widget.parent().mapTo(main_window, widget.pos())

	def screenWidth(self, main_window):
		return main_window.width()

	def screenHeight(self, main_window):
		return main_window.height()

	def showTooltip(self, tooltip, align, main_window):
		raise NotImplementedError("Subclass responsibility")

	def isPossibleFor(self, hovered_widget, tooltip, main_window):
		return not main_window.isMinimized()

	def _getContainerFor(self, tooltip, main_window):
		container = QWidget(main_window)
		container.setLayout(QVBoxLayout())
		container.layout().setContentsMargins(0, 0, 0, 0)
		container.layout().setSpacing(0)
		return container

	def _getHorizontalContainerFor(self, tooltip, main_window):
		container = QWidget(main_window)
		container.setLayout(QHBoxLayout())
		container.layout().setContentsMargins(0, 0, 0, 0)
		container.layout().setSpacing(0)
		return container
