from TestStack.White.UIItems.WindowStripControls import ToolStrip
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class ToolStripKeywords(LibraryComponent):
    @keyword
    def click_toolstrip_button_by_index(self, locator, index):
        """Clicks a button in a toolstrip (toolbar).

        ``locator`` is the locator of the toolstrip.

        ``index`` is the zero-based index of the toolstrip button to click.
        """
        button = self._get_toolstrip_button_by_index(locator, int(index))
        button.Click()

    def _get_toolstrip_button_by_index(self, locator, index):
        toolstrip = self.state._get_typed_item_by_locator(ToolStrip, locator)
        search_criteria = self.state._get_search_criteria("control_type:Button")
        try:
            return toolstrip.GetMultiple(search_criteria)[index]
        except IndexError:
            raise IndexError("Invalid ToolStrip button index '{}'".format(index))
