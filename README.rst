Custom Tooltips for PySide
--------

To use you will need to subclass Tooltip or TooltipWithArrow and implement the getWidget function::

    >>> class MyTooltip(Tooltip):
    >>>   def getWidget(self):
    >>>	    return MyQWidget()

Then, your tooltip will need a few parameters to initialize

	>>> my_tooltip = MyTooltip(hoverable_widget, list_of_positionings, main_window, gap=7)

hoverable_widget is the widget that will trigger the tooltip.

list_of_positionings is a list of tuples: (TooltipPositioning, TooltipAlignment)
TooltipPositioning can be one of Tooltips Macros: Tooltip.LEFT_POSITIONING, Tooltip.TOP_POSITIONING, Tooltip.RIGHT_POSITIONING or Tooltip.BOTTOM_POSITIONING
Positionings should be TooltipWithArrow.*_POSITIONING if you chose to subclass TooltipWithArrow

TooltipAlignment should be one of the functions included in TooltipAlignment.

Therefore, a list_of_positioning could be: [(TooltipWithArrow.RIGHT_POSITIONING, alignToTop), (TooltipWithArrow.LEFT_POSITIONING, alignToTop)]
