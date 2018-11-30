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

        Verifies text in button.

        ``locator`` is the locator of the button.

        ``expected`` is the expected button text.
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        self.state._verify_value(expected, button.Text)

    @keyword
    def select_radio_button(self, locator):
        """
        Click button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        radiobutton.Select()
        
    @keyword
    def verify_radio_button(self, locator, expected):
        """
        Verify value of radio button
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        self.state._verify_value(bool(expected), radiobutton.IsSelected)

    @keyword
    def toggle_check_box(self, locator):
        """
        Toggle check box
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        checkbox.Toggle()
        
    @keyword
    def verify_check_box(self, locator, expected):
        """
        Verify value of check box
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected value | M |
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        self.state._verify_value(bool(expected), checkbox.IsSelected)
