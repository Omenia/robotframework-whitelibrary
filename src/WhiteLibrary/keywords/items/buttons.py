from TestStack.White.UIItems import Button, CheckBox, RadioButton
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from WhiteLibrary.utils.click import Clicks


class ButtonKeywords(LibraryComponent):
    @keyword
    def click_button(self, locator, x_offset=0, y_offset=0):
        """Clicks a button.

        ``locator`` is the locator of the button or Button item object.
        Locator syntax is explained in `Item locators`.

        Optional arguments ``x_offset`` and ``y_offset`` can be used to define the coordinates to click at,
        relative to the center of the item.
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        Clicks.click(button, x_offset, y_offset)

    @keyword
    def button_text_should_be(self, locator, expected_text, case_sensitive=True):
        """Verifies exact text in a button.

        ``locator`` is the locator of the button or Button item object.
        Locator syntax is explained in `Item locators`.

        ``expected_text`` is the expected button text.

        ``case_sensitive`` defines if the text comparison is case sensitive (True/False). Defaults to ``True``.
        Boolean values are evaluated in the same way as the Robot Framework BuiltIn library does, see
        [http://robotframework.org/robotframework | the documentation of BuiltIn] for details.
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        self.state._verify_string_value(expected_text, button.Text, case_sensitive)

    @keyword
    def button_text_should_contain(self, locator, expected_text, case_sensitive=True):
        """Verifies expected text is found in a button.

        ``locator`` is the locator of the button or Button item object.
        Locator syntax is explained in `Item locators`.

        ``expected_text`` is the expected button text.

        ``case_sensitive`` defines if the text comparison is case sensitive (True/False). Defaults to ``True``.
        Boolean values are evaluated in the same way as the Robot Framework BuiltIn library does, see
        [http://robotframework.org/robotframework | the documentation of BuiltIn] for details.
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        self.state._contains_string_value(expected_text, button.Text, case_sensitive)

    @keyword
    def verify_button(self, locator, expected):
        """*DEPRECATED.* Use `Button Text Should Be` or `Button Text Should Contain` instead.

        Verifies text in a button.

        ``locator`` is the locator of the button or Button item object.

        ``expected`` is the expected button text.
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        self.state._verify_value(expected, button.Text)

    @keyword
    def select_radio_button(self, locator):
        """Selects a radio button.

        ``locator`` is the locator of the radio button or RadioButton item object.
        Locator syntax is explained in `Item locators`.
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        radiobutton.Select()

    @keyword
    def verify_radio_button(self, locator, expected):
        """Verifies state of a radio button.

        ``locator`` is the locator of the radio button or RadioButton item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected state (True/False).
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        self.state._verify_value(bool(expected), radiobutton.IsSelected)

    @keyword
    def get_radio_button_state(self, locator):
        """Returns the state of a radio button.

        Returns `True` if the radio button is selected, `False` if not.

        ``locator`` is the locator of the radio button or RadioButton item object.
        Locator syntax is explained in `Item locators`.
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        return radiobutton.IsSelected

    @keyword
    def toggle_check_box(self, locator):
        """Toggles a check box.

        ``locator`` is the locator of the check box or CheckBox item object.
        Locator syntax is explained in `Item locators`.
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        checkbox.Toggle()

    @keyword
    def verify_check_box(self, locator, expected):
        """Verifies state of a check box.

        ``locator`` is the locator of the check box or CheckBox item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected state (True/False).
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        self.state._verify_value(bool(expected), checkbox.IsSelected)

    @keyword
    def get_check_box_state(self, locator):
        """Returns the state of a check box.

        Returns `True` if the check box is selected, `False` if not.

        ``locator`` is the locator of the check box or CheckBox item object.
        Locator syntax is explained in `Item locators`.
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        return checkbox.IsSelected
