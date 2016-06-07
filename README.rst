# Custom Tooltips for PySide
--------

To use you will need to subclass Tooltip or TooltipWithArrow and implement the getWidget function::

    >>> class MyTooltip(Tooltip):
    >>> 	def getWidget(self):
    >>>			return MyQWidget()
