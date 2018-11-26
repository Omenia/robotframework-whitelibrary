from TestStack.White.UIItems.TabItems import Tab
from ..librarycomponent import LibraryComponent
from ..robotlibcore import keyword


class TabKeywords(LibraryComponent):
    @keyword
    def select_tab_page(self, locator, title):
        """ Selects a tab page. """
        tab = self.state._get_typed_item_by_locator(Tab, locator)
        tab.SelectTabPage(title)
