from TestStack.White.UIItems.MenuItems import Menu
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class MenuKeywords(LibraryComponent):
    @keyword
    def verify_menu(self, locator, expected):
        """Verifies the text of a menu item.

        ``locator`` is the locator of the menu item.

        ``expected`` is the expected text of the menu item.
        """
        menu = self.state._get_typed_item_by_locator(Menu, locator)
        self.state._verify_value(expected, menu.Name)

    @keyword
    def click_menu_button(self, locator):
        """Clicks a menu button.

        ``locator`` is the locator of the menu button.
        """
        menu_button = self.state._get_typed_item_by_locator(Menu, locator)
        menu_button.Click()

    @keyword
    def click_item_in_popup_menu(self, *text_path):
        """Clicks an item in the currently open popup/context menu.

        ``text_path`` is the path to the item to click.

        Examples:
        | Click Popup Menu Item | Paste | | # click an item in the root level |
        | Click Popup Menu Item | Refactor | Rename | # click a sub item |
        """
        popup_menu = self.state.window.Popup
        popup_menu.Item(list(text_path)).Click()
