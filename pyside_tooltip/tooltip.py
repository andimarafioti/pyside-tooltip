# coding: utf-8

from PySide.QtCore import QEvent, QObject, Property, QPropertyAnimation, QEasingCurve
from PySide.QtGui import QCursor, QGraphicsOpacityEffect

from gui.tooltip.positioning.bottomTooltipPositioning import BottomTooltipPositioning
from gui.tooltip.positioning.leftTooltipPositioning import LeftTooltipPositioning
from gui.tooltip.positioning.nullTooltipPositioning import NullTooltipPositioning
from gui.tooltip.positioning.rightTooltipPositioning import RightTooltipPositioning
from gui.tooltip.positioning.topTooltipPositioning import TopTooltipPositioning

__author__ = 'Andres'


class Tooltip(QObject):
	# Positioning:
	LEFT_POSITIONING = LeftTooltipPositioning()
	TOP_POSITIONING = TopTooltipPositioning()
	RIGHT_POSITIONING = RightTooltipPositioning()
	BOTTOM_POSITIONING = BottomTooltipPositioning()

	NULL_POSITIONING = NullTooltipPositioning()

	# Tiempos de fade
	FADE_IN_TIME = 300
	FADE_OUT_TIME = 500

	def __init__(self, hoverable_widget, positionings, main_window, gap=7):
		super(Tooltip, self).__init__()

		self._current_positioning = None
		self._tooltipContainer = None

		self._widget = None
		self._hoverable_widget = hoverable_widget
		self._mainWindow = main_window
		self._gap = gap
		self._positionings = positionings
		self._positionings.append([Tooltip.NULL_POSITIONING, None])
		self.isHoverable = True

		self._hoverable_widget.installEventFilter(self)

	def gap(self):
		return self._gap

	def getWidget(self):
		raise NotImplementedError("Subclass Responsibility")

	def widget(self):
		return self._widget

	def hoveredWidget(self):
		return self._hoverable_widget

	def positionings(self):
		return self._positionings

	def close(self):
		self._tooltipContainer.close()
		self._tooltipContainer = None

	def closeTooltip(self):
		if self._tooltipContainer is not None:
			self._tooltipContainer.removeEventFilter(self)
			opacity = self._getOpacity() + 0.01
			self._fade(opacity, 0.0, self.FADE_OUT_TIME * opacity)
			self.anim.finished.connect(self.close)

	def _closeTooltipWithoutAnimation(self):
		"""
		No superponer explicitamente animaciones.
		Si el tooltip se cierra y detras suyo se abre otra vista, usar este metodo.
		"""
		if self._tooltipContainer is not None:
			self.close()

	def setHoverability(self):
		self.isHoverable = True

	def _handleHoveredWidgetEnterEvent(self):
		if self._tooltipContainer is None:
			self._widget = self.getWidget()
			self._current_positioning = self._getBestPossiblePositioning()
			self._tooltipContainer = self._current_positioning[0].showTooltip(self, self._current_positioning[1], self._mainWindow)
			self._tooltipContainer.installEventFilter(self)
			self._fade(0.0, 1.0, self.FADE_IN_TIME)
		else:
			opacity = self._getOpacity()
			self._fade(opacity, 1.0, self.FADE_IN_TIME * (1 - opacity))
			self._tooltipContainer.installEventFilter(self)

	def _handleHoveredWidgetLeaveEvent(self):
		if not self.isHoverable:
			self._closeTooltipWithoutAnimation()
		elif self._tooltipContainer is not None and not self._tooltipContainerUnderMouse():
			self.closeTooltip()

	def _handleTooltipLeaveEvent(self):
		try:
			if not self._hoveredWidgetUnderMouse():
				self.closeTooltip()
		except RuntimeError:
			self.closeTooltip()

	def _getBestPossiblePositioning(self):
		return next(positioning for positioning in self._positionings
					if positioning[0].isPossibleFor(self._hoverable_widget, self, self._mainWindow))

	def _tooltipContainerUnderMouse(self):
		return self._tooltipContainer.rect().contains(self._tooltipContainer.mapFromGlobal(QCursor.pos()))

	def _hoveredWidgetUnderMouse(self):
		return self._hoverable_widget.rect().contains(self._hoverable_widget.mapFromGlobal(QCursor.pos()))

	def eventFilter(self, obj, event):
		if obj is self._hoverable_widget:
			if event.type() is QEvent.Enter:
				self._handleHoveredWidgetEnterEvent()
			elif event.type() is QEvent.Leave:
				self._handleHoveredWidgetLeaveEvent()
				self.setHoverability()
		elif obj is self._tooltipContainer:
			if event.type() is QEvent.Leave:
				self._handleTooltipLeaveEvent()
		return False

	# Aca viene la mierda del fade

	def _getOpacity(self):
		return self._tooltipContainer.graphicsEffect().opacity()

	def _setOpacity(self, opacity):
		if self._tooltipContainer is not None:
			effect = QGraphicsOpacityEffect(self._tooltipContainer)
			effect.setOpacity(opacity)
			self._tooltipContainer.setGraphicsEffect(effect)

	_opacity_property = Property(type(0.0), _getOpacity, _setOpacity)

	def _fade(self, start, end, duration):
		effect = QGraphicsOpacityEffect(self)
		effect.setOpacity(start)
		self._tooltipContainer.setGraphicsEffect(effect)

		self.anim = QPropertyAnimation(self, "_opacity_property")
		self.anim.setDuration(duration)
		self.anim.setStartValue(start)
		self.anim.setEndValue(end)
		self.anim.setEasingCurve(QEasingCurve.OutQuad)
		self.anim.start()
