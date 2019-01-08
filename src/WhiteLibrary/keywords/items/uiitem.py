from TestStack.White.UIItems import UIItem   # noqa: F401
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class UiItemKeywords(LibraryComponent):
    @keyword
    def click_item(self, locator):
        """Click an item.

        ``locator`` is the locator of the item.
        """
        item = self.state._get_item_by_locator(locator)
        item.Click()

    @keyword
    def right_click_item(self, locator):
        """Right click an item.

        ``locator`` is the locator of the item.
        """
        item = self.state._get_item_by_locator(locator)
        item.RightClick()

    @keyword
    def double_click_item(self, locator):
        """Double click an item.

        ``locator`` is the locator of the item.
        """
        item = self.state._get_item_by_locator(locator)
        item.DoubleClick()

    @keyword
    def get_items(self, locator):
        """Return a list of items that match the given locator.

        ``locator`` is the locator of the item.
        """
        return self.state._get_multiple_items_by_locator(locator)
