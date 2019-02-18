from TestStack.White.UIItems.WindowItems import Window
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class MenuKeywords(LibraryComponent):
    @keyword
    def message_box_title_should_be(self, locator, expected):
        """Verifies the text of a menu item.

        ``locator`` is the locator of the menu item.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected text of the menu item.
        """
        message_box = self.state._get_typed_item_by_locator(Window, locator)
        self.state._verify_value(expected, menu.Name)
