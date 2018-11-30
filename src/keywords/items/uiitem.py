from TestStack.White.UIItems import UIItem
from librarycomponent import LibraryComponent
from robotlibcore import keyword


class UiItemKeywords(LibraryComponent):
    @keyword
    def click_item(self, locator):
        """
        Click an item
        Parameters
        ----------
        locator - element id, text or index prefixed with <locator_type>=
        """
        item = self.state._get_item_by_locator(locator)
        item.Click()
    
    @keyword
    def right_click_item(self, locator):
        """
        Right click an item
        Parameters
        ----------
        locator - element id, text or index prefixed with <locator_type>=
        """
        item = self.state._get_item_by_locator(locator)
        item.RightClick()

    @keyword
    def double_click_item(self, locator):
        """
        Double click an item
        Parameters
        ----------
        locator - element id, text or index prefixed with <locator_type>=
        """
        item = self.state._get_item_by_locator(locator)
        item.DoubleClick()
