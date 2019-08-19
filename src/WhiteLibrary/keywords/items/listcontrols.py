from robot.api import logger  # noqa:  F401 #pylint: disable=unused-import
from TestStack.White.UIItems.ListBoxItems import ComboBox, ListBox
from TestStack.White.UIItems import UIActionException
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class ListKeywords(LibraryComponent):
    @keyword
    def select_listbox_value(self, locator, value):
        """Selects a value from a listbox.

        ``locator`` is the locator of the listbox or ListBox item object.
        Locator syntax is explained in `Item locators`.

        ``value`` is the value to be selected.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        listbox.Select(value)

    @keyword
    def select_listbox_index(self, locator, item_index):
        """Selects an item by its index from a listbox.

        ``locator`` is the locator of the listbox or ListBox item object.
        Locator syntax is explained in `Item locators`.

        ``item_index`` is the index of the item to select.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        listbox.Select(int(item_index))

    @keyword
    def get_listbox_selected_text(self, locator):
        """Returns the text of the selected listbox item.

        ``locator`` is the locator of the listbox or ListBox item object.
        Locator syntax is explained in `Item locators`.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        return listbox.SelectedItemText

    @keyword
    def listbox_selection_should_be(self, locator, expected):
        """Checks the listbox selection.

        Fails if the selection was not as expected.

        ``locator`` is the locator of the listbox or ListBox item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected selection value.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        if listbox.SelectedItemText != expected:
            raise AssertionError(
                u"Expected listbox selection to be {}, was {}".format(expected, listbox.SelectedItemText)
            )

    @keyword
    def listbox_should_contain(self, locator, expected):
        """Checks that listbox contains an item with text ``expected``.

        Fails if the listbox does not contain an item with the given text.

        ``locator`` is the locator of the listbox or ListBox item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected item text.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        try:
            listbox.Item(str(expected))
        except UIActionException as error:
            # Check error in case we get UIActionException with another message
            if "Item of text" in str(error):
                raise AssertionError(u"ListBox with locator '{}' did not contain '{}'".format(locator, expected))
            raise error

    @keyword
    def listbox_should_not_contain(self, locator, expected):
        """Verifies that a listbox does not contain an item with text ``expected``.

        Fails if the listbox contains an item with the given text.

        ``locator`` is the locator of the listbox or ListBox item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected item text.
        """
        listbox = self.state._get_typed_item_by_locator(ListBox, locator)
        try:
            listbox.Item(str(expected))
            raise AssertionError(u"ListBox with locator '{}' should not have contained '{}'".format(locator, expected))
        except UIActionException as error:
            # Check error in case we get UIActionException with another message
            if "Item of text" not in str(error):
                raise error

    @keyword
    def select_combobox_value(self, locator, value):
        """Selects a value from a combobox.

        ``locator`` is the locator of the combobox or ComboBox item object.
        Locator syntax is explained in `Item locators`.

        ``value`` is the value to be selected.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        combobox.Select(value)

    @keyword
    def select_combobox_index(self, locator, item_index):
        """Selects a value from combobox by using its index.

        ``locator`` is the locator of the combobox or ComboBox item object.
        Locator syntax is explained in `Item locators`.

        ``item_index`` is the index to be selected.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        combobox.Select(int(item_index))

    @keyword
    def get_combobox_selected_text(self, locator):
        """Returns the text of the selected combobox item.

        ``locator`` is the locator of the combobox or ComboBox item object.
        Locator syntax is explained in `Item locators`.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        return combobox.SelectedItemText

    @keyword
    def verify_combobox_item(self, locator, expected):
        """*DEPRECATED* Please use Verify Combobox Selection instead.

        Verifies the selected value of a combobox.

        ``locator`` is the locator of the combobox or ComboBox item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected selection value.
        """
        self.verify_combobox_selection(locator, expected)

    @keyword
    def verify_combobox_selection(self, locator, expected):
        """Verifies that the combobox value is selected.

        ``locator`` is the locator of the combobox or ComboBox item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected selection value.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        self.state._verify_value(expected, combobox.EditableText)

    @keyword
    def combobox_should_contain(self, locator, expected):
        """Verifies that a combobox contains an item with text ``expected``.

        Fails if the combobox does not contain an item with the given text.

        ``locator`` is the locator of the combobox or ComboBox item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected item text.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        try:
            combobox.Item(str(expected))
        except UIActionException as error:
            # Check error in case we get UIActionException with another message
            if "Item of text" in str(error):
                raise AssertionError(u"ComboBox with locator '{}' did not contain '{}'".format(locator, expected))
            raise error

    @keyword
    def combobox_should_not_contain(self, locator, expected):
        """Verifies that a combobox does not contain an item with text ``expected``.

        Fails if the combobox contains an item with the given text.

        ``locator`` is the locator of the combobox or ComboBox item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected item text.
        """
        combobox = self.state._get_typed_item_by_locator(ComboBox, locator)
        try:
            combobox.Item(str(expected))
            raise AssertionError(u"ComboBox with locator '{}' should not have contained '{}'".format(locator, expected))
        except UIActionException as error:
            # Check error in case we get UIActionException with another message
            if "Item of text" not in str(error):
                raise error
