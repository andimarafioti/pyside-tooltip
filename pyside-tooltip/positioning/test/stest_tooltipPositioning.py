# coding: utf-8
from unittest import TestCase

from mock import Mock, patch

from gui.tooltip.positioning.tooltipPositioning import TooltipPositioning
from models.esttelaServices import Esttela

__author__ = 'Andres'


class TestTooltipPositioning(TestCase):
	@classmethod
	def setUpClass(cls):
		patcher = patch('gui.tooltip.positioning.tooltipPositioning.QWidget')
		cls.patched_QWidget = patcher.start()
		patcher = patch('gui.tooltip.positioning.tooltipPositioning.QVBoxLayout')
		cls.patched_QVBoxLayout = patcher.start()
		cls.widget = Mock()
		cls.positioning = TooltipPositioning()

	def setUp(self):
		Esttela.presenter = Mock()
		Esttela.presenter.view = Mock()

	def tearDown(self):
		pass

	def testGetContainerForReturnsTheDesiredContainer(self):
		container = self.positioning._getContainerFor(self.widget, self.widget)
		container.layout().setContentsMargins.assert_called_with(0, 0, 0, 0)
		container.layout().setSpacing.assert_called_with(0)

	def testGetHorizontalContainerForReturnsTheDesiredContainer(self):
		container = self.positioning._getHorizontalContainerFor(self.widget, self.widget)
		container.layout().setContentsMargins.assert_called_with(0, 0, 0, 0)
		container.layout().setSpacing.assert_called_with(0)

	def testisPossibleForReturnsIsNotMiminized(self):
		self.widget.isMinimized.return_value = True
		self.assertFalse(self.positioning.isPossibleFor(self.widget, self.widget, self.widget))
		self.widget.isMinimized.return_value = False
		self.assertTrue(self.positioning.isPossibleFor(self.widget, self.widget, self.widget))

