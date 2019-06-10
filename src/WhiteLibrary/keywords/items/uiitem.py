from robot.utils import timestr_to_secs
from TestStack.White.UIItems import UIItem  # noqa: F401 #pylint: disable=unused-import
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.utils.click import Clicks
import time


class UiItemKeywords(LibraryComponent):
    @keyword
    def click_item(self, locator, x_offset=0, y_offset=0):
        """Clicks an item.

        ``locator`` is the locator of the item or object of an item.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to define the coordinates to click at,
        relative to the center of the item.
        """
        item = self.state._get_item_by_locator(locator)
        Clicks.click(item, x_offset, y_offset)

    @keyword
    def right_click_item(self, locator, x_offset=0, y_offset=0):
        """Right clicks an item.

        ``locator`` is the locator of the item or object of an item.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to define the coordinates to click at,
        relative to the center of the item.
        """
        item = self.state._get_item_by_locator(locator)
        Clicks.right_click(item, x_offset, y_offset)

    @keyword
    def double_click_item(self, locator, x_offset=0, y_offset=0):
        """Double clicks an item.

        ``locator`` is the locator of the item or object of an item.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to define the coordinates to click at,
        relative to the center of the item.
        """
        item = self.state._get_item_by_locator(locator)
        Clicks.double_click(item, x_offset, y_offset)

    @keyword
    def get_items(self, locator):
        """Returns a list of items that match the given ``locator``.

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

    @keyword
    def item_should_be_enabled(self, locator):
        """Verifies that an item is enabled.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.
        """
        item = self.state._get_item_by_locator(locator)
        if not item.Enabled:
            raise AssertionError("Expected item with locator '{}' to be enabled but found disabled".format(locator))

    @keyword
    def item_should_be_disabled(self, locator):
        """Verifies that an item is disabled.

        ``locator`` is the locator of the item.
        Locator syntax is explained in `Item locators`.
        """
        item = self.state._get_item_by_locator(locator)
        if item.Enabled:
            raise AssertionError("Expected item with locator '{}' to be disabled but found enabled".format(locator))

    @keyword
    def wait_until_item_exists(self, locator, timeout):
        self._wait_until_true(lambda: self.item_exists(locator),
                              timeout,
                              "Item with locator '{}' was not visible in {} seconds".format(locator, timestr_to_secs(timeout)))

    @keyword
    def wait_until_item_does_not_exist(self, locator, timeout):
        self._wait_until_true(lambda: not self.item_exists(locator),
                              timeout,
                              "Item with locator '{}' did not disappear in {} seconds".format(locator, timestr_to_secs(timeout)))

    def item_exists(self, locator):
        search_criteria = self.state._get_search_criteria(locator)
        return self.state.window.Exists(search_criteria)

    def _wait_until_true(self, condition, timeout, error_msg):
        timeout = timestr_to_secs(timeout)
        max_wait = time.time() + timeout
        while True:
            if condition():
                break
            if time.time() > max_wait:
                raise AssertionError(error_msg)
            time.sleep(0.1)
