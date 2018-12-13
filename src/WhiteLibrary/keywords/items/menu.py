from TestStack.White.UIItems.MenuItems import Menu
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class MenuKeywords(LibraryComponent):
    @keyword
    def verify_menu(self, locator, expected):
        """
        Verify menu item exists
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | expected | expected text in value | M |
        """
        menu = self.state._get_typed_item_by_locator(Menu, locator)
        self.state._verify_value(expected, menu.Name)

    @keyword
    def click_menu_button(self, locator):
        """
        Click menu button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        """
        menu_button = self.state._get_typed_item_by_locator(Menu, locator)
        menu_button.Click()
