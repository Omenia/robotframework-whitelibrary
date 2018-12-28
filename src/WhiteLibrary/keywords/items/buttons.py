from TestStack.White.UIItems import Button, CheckBox, RadioButton
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class ButtonKeywords(LibraryComponent):
    @keyword
    def click_button(self, locator):
        """ Clicks button.

        ``locator`` is the locator of the button.
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        button.Click()

    @keyword
    def button_text_should_be(self, locator, expected_text):
        raise NotImplementedError()

    @keyword
    def button_text_should_contain(self, locator, expected_text):
        raise NotImplementedError()

    @keyword
    def verify_button(self, locator, expected):
        """*DEPRECATED.* Use `Button Text Should Be` or `Button Text Should Contain` instead.

        Verifies text in a button.

        ``locator`` is the locator of the button.

        ``expected`` is the expected button text.
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        self.state._verify_value(expected, button.Text)

    @keyword
    def select_radio_button(self, locator):
        """
        Selects a radio button.

        ``locator`` is the locator of the radio button.
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        radiobutton.Select()

    @keyword
    def verify_radio_button(self, locator, expected):
        """
        Verifies state of a radio button.

        ``locator`` is the locator of the radio button.

        ``expected`` is the expected state (True/False).
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        self.state._verify_value(bool(expected), radiobutton.IsSelected)

    @keyword
    def get_radio_button_state(self, locator):
        """
        Gets the state of a radio button.

        ``locator`` is the locator of the radio button.

        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        return radiobutton.IsSelected

    @keyword
    def toggle_check_box(self, locator):
        """
        Toggles a check box.

        ``locator`` is the locator of the check box.
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        checkbox.Toggle()

    @keyword
    def verify_check_box(self, locator, expected):
        """
        Verifies state of a check box.

        ``locator`` is the locator of the check box.

        ``expected`` is the expected state (True/False).
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        self.state._verify_value(bool(expected), checkbox.IsSelected)

    @keyword
    def get_check_box_state(self, locator):
        """
        Gets the state of a check box.

        ``locator`` is the locator of the check box.

        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        return checkbox.IsSelected
