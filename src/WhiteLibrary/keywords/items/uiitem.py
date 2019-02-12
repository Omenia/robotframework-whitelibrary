from TestStack.White.UIItems import UIItem   # noqa: F401
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class UiItemKeywords(LibraryComponent):
    @keyword
    def click_item(self, locator):
        """Clicks an item.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.
        """
        item = self.state._get_item_by_locator(locator)
        item.Click()

    @keyword
    def right_click_item(self, locator):
        """Right clicks an item.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.
        """
        item = self.state._get_item_by_locator(locator)
        item.RightClick()

    @keyword
    def double_click_item(self, locator):
        """Double clicks an item.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.
        """
        item = self.state._get_item_by_locator(locator)
        item.DoubleClick()

    @keyword
    def get_items(self, locator):
        """Returns a list of items that match the given `locator`.

        Locator syntax is explained in `Item locators`.
        """
        return self.state._get_multiple_items_by_locator(locator)

    @keyword
    def get_item(self, locator):
        """Returns the first item that matches the given locator.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.
        """
        return self.state._get_item_by_locator(locator)
