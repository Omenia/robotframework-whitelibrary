from TestStack.White.UIItems import UIItem
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class UiItemKeywords(LibraryComponent):
    @keyword
    def click_item(self, locator):
        """
        Clicks an item.
        
        ``locator`` is the locator of the item.
        """
        item = self.state._get_item_by_locator(locator)
        item.Click()
    
    @keyword
    def right_click_item(self, locator):
        """
        Right clicks an item.

        ``locator`` is the locator of the item.
        """
        item = self.state._get_item_by_locator(locator)
        item.RightClick()

    @keyword
    def double_click_item(self, locator):
        """
        Double clicks an item.
        
        ``locator`` is the locator of the item.
        """
        item = self.state._get_item_by_locator(locator)
        item.DoubleClick()
