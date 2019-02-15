from TestStack.White.UIItems import UIItem   # noqa: F401
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.utils.click import Clicks

from TestStack.White.InputDevices import Mouse
from robot.api import logger

class UiItemKeywords(LibraryComponent):
    @keyword
    def click_item(self, locator, x_offset=0, y_offset=0):
        """Clicks an item.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to fine tune
        mouse position relative to the center of the item.
        """
        item = self.state._get_item_by_locator(locator)
        Clicks.click(item, x_offset, y_offset)

    @keyword
    def right_click_item(self, locator, x_offset=0, y_offset=0):
        """Right clicks an item.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to fine tune
        mouse position relative to the center of the item.
        """
        item = self.state._get_item_by_locator(locator)
        Clicks.right_click(item, x_offset, y_offset)

    @keyword
    def double_click_item(self, locator, x_offset=0, y_offset=0):
        """Double clicks an item.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to fine tune
        mouse position relative to the center of the item.
        """
        item = self.state._get_item_by_locator(locator)
        Clicks.double_click(item, x_offset, y_offset)

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

