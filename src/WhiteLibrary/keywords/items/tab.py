from TestStack.White.UIItems.TabItems import Tab
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class TabKeywords(LibraryComponent):
    @keyword
    def select_tab_page(self, locator, title):
        """
        Selects a tab page.

        ``locator`` is the locator of the tab control item or Tab item object.
        Locator syntax is explained in `Item locators`.

        ``title`` is the title of the tab page.
        """
        tab_control = self.state._get_typed_item_by_locator(Tab, locator)
        tab_control.SelectTabPage(title)

    @keyword
    def select_tab_page_with_index(self, locator, index):
        """
        Selects a tab page.

        ``locator`` is the locator of the tab control item or Tab item object.
        Locator syntax is explained in `Item locators`.

        ``index`` is integer index the tab page. Indexing starts from 0.
        """
        tab_control = self.state._get_typed_item_by_locator(Tab, locator)
        tab_control.SelectTabPage(int(index))

    @keyword
    def get_tab_pages(self, locator):
        """
        Gets all tab pages and returns them as a list.
        The resulting list contains TabPage objects. You can select tab using TabPage as follows:
        @{tabs}=    Get Tab Pages    myTabControl
        Select Tab Page    tabControl    ${tabs[0].Name}

        ``locator`` is the locator of the tab control item or Tab item object.
        Locator syntax is explained in `Item locators`.

        """
        tab_control = self.state._get_typed_item_by_locator(Tab, locator)
        return tab_control.Pages
