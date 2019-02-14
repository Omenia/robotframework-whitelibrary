from TestStack.White.UIItems import UIItem   # noqa: F401
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.UIA import RectX
from System.Windows import Point, Rect
from TestStack.White.InputDevices import Mouse
from robot.api import logger

class UiItemKeywords(LibraryComponent):
    @keyword
    def click_item(self, locator, x_offset=0, y_offset=0):
        """Clicks an item.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to fine tune
        mouse position relative to the center of the item. Their default is 0.
        """
        item = self.state._get_item_by_locator(locator)
        UiItemKeywords.click(item, x_offset, y_offset)

    @keyword
    def right_click_item(self, locator, x_offset=0, y_offset=0):
        """Right clicks an item.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to fine tune
        mouse position relative to the center of the item. Their default is 0.
        """
        item = self.state._get_item_by_locator(locator)
        UiItemKeywords.right_click(item, x_offset, y_offset)

    @keyword
    def double_click_item(self, locator, x_offset=0, y_offset=0):
        """Double clicks an item.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to fine tune
        mouse position relative to the center of the item. Their default is 0.
        """
        item = self.state._get_item_by_locator(locator)
        UiItemKeywords.double_click(item, x_offset, y_offset)

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

    #Low level function to handle offset click.
    @staticmethod
    def click(item, x_offset=0, y_offset=0):
        offset_position = UiItemKeywords._get_offset_point(item, x_offset, y_offset)
        Mouse.Instance.Click(offset_position)

    #Low level helper function to handle offset right click.
    @staticmethod
    def right_click(item, x_offset=0, y_offset=0):
        offset_position = UiItemKeywords._get_offset_point(item, x_offset, y_offset)
        Mouse.Instance.Location = offset_position
        Mouse.Instance.RightClick()

    #Low level helper function to handle offset right click.
    @staticmethod
    def double_click(item, x_offset=0, y_offset=0):
        offset_position = UiItemKeywords._get_offset_point(item, x_offset, y_offset)
        Mouse.Instance.DoubleClick(offset_position)

    #Helper function to translate item center to offset point
    @staticmethod
    def _get_offset_point(item, x_offset, y_offset):
        item_bounds = item.Bounds
        item_center = RectX.Center(item_bounds)
        offset_point = Point(int(item_center.X) + int(x_offset),
                                int(item_center.Y) + int(y_offset))
        if not item_bounds.Contains(offset_point):
            raise AssertionError("click location out of bounds")
        return offset_point
