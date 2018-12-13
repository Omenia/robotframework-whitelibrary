from TestStack.White.UIItems.ListBoxItems import ComboBox, ListBox
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword

class ListKeywords(LibraryComponent):
    @keyword
    def select_listbox_value(self, locator, value):
        """
        Selects a value from a listbox.
        
        ``locator`` is the locator of the listbox.

        ``value`` is the value to be selected.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        listbox.Select(value)

    @keyword    
    def listbox_selection_should_be(self, locator, expected):
        """
        Checks the listbox selection.

        Fails if the selection was not as expected.

        ``locator`` is the locator of the listbox.

        ``expected`` is the expected selection value.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        if listbox.SelectedItemText != expected:
            raise AssertionError("Expected listbox selection to be " +
                                 expected + ", was " + listbox.SelectedItemText)

    @keyword
    def select_combobox_value(self, locator, value):
        """
        Selects a value from a combobox.
        
        ``locator`` is the locator of the combobox.

        ``value`` is the value to be selected.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        combobox.Select(value)

    @keyword
    def select_combobox_index(self, locator, index):
        """
        Selects a value from combobox by using its index.

        ``locator`` is the locator of the combobox.

        ``index`` is the index to be selected.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        combobox.Select(int(index))

    @keyword
    def verify_combobox_item(self, locator, expected):
        """
        *DEPRECATED* Please use Verify Combobox Selection instead
        Verifies the selected value of a combobox.
        
        ``locator`` is the locator of the combobox.

        ``expected`` is the expected selection value.
        """
        self.verify_combobox_selection(locator, expected)

    @keyword
    def verify_combobox_selection(self, locator, expected):
        """
        Verifies the selected value of a combobox.
        
        ``locator`` is the locator of the combobox.

        ``expected`` is the expected selection value.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        self.state._verify_value(expected, combobox.EditableText)
