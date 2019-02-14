from TestStack.White.UIItems import Button, CheckBox, RadioButton
from TestStack.White.InputDevices import Mouse
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from System.Windows import Point, Rect
from TestStack.White.UIA import RectX
from robot.api import logger

class ButtonKeywords(LibraryComponent):
    @keyword
    def click_button(self, locator, x_offset=0, y_offset=0):
        """Clicks a button.

        ``locator`` is the locator of the button.
        Locator syntax is explained in `Item locators`.
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        self.click(button, x_offset, y_offset)

    @keyword
    def button_text_should_be(self, locator, expected_text, case_sensitive=True):
        """Verifies exact text in a button.

        ``locator`` is the locator of the button.
        Locator syntax is explained in `Item locators`.

        ``expected_text`` is the expected button text.

        ``case_sensitive`` compare text in case sensitive matter. Defaults to True
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        self.state._verify_string_value(expected_text, button.Text, case_sensitive)

    @keyword
    def button_text_should_contain(self, locator, expected_text, case_sensitive=True):
        """Verifies expected text is found in a button.

        ``locator`` is the locator of the button.
        Locator syntax is explained in `Item locators`.

        ``expected_text`` is the expected button text.

        ``case_sensitive`` compare text in case sensitive matter. Defaults to True
        """
        button = self.state._get_typed_item_by_locator(Button, locator)
        self.state._contains_string_value(expected_text, button.Text, case_sensitive)

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
        """Selects a radio button.

        ``locator`` is the locator of the radio button.
        Locator syntax is explained in `Item locators`.
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        radiobutton.Select()

    @keyword
    def verify_radio_button(self, locator, expected):
        """Verifies state of a radio button.

        ``locator`` is the locator of the radio button.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected state (True/False).
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        self.state._verify_value(bool(expected), radiobutton.IsSelected)

    @keyword
    def get_radio_button_state(self, locator):
        """Returns the state of a radio button.

        Returns `True` if the radio button is selected, `False` if not.

        ``locator`` is the locator of the radio button.
        Locator syntax is explained in `Item locators`.
        """
        radiobutton = self.state._get_typed_item_by_locator(RadioButton, locator)
        return radiobutton.IsSelected

    @keyword
    def toggle_check_box(self, locator):
        """Toggles a check box.

        ``locator`` is the locator of the check box.
        Locator syntax is explained in `Item locators`.
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        checkbox.Toggle()

    @keyword
    def verify_check_box(self, locator, expected):
        """Verifies state of a check box.

        ``locator`` is the locator of the check box.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected state (True/False).
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        self.state._verify_value(bool(expected), checkbox.IsSelected)

    @keyword
    def get_check_box_state(self, locator):
        """Returns the state of a check box.

        Returns `True` if the check box is selected, `False` if not.

        ``locator`` is the locator of the check box.
        Locator syntax is explained in `Item locators`.
        """
        checkbox = self.state._get_typed_item_by_locator(CheckBox, locator)
        return checkbox.IsSelected

    #Low level helper function to handle offset related details.
    def click(self, item, x_offset, y_offset):
        item_bounds = item.Bounds
        item_center = RectX.Center(item_bounds)
        offset_position = Point(int(item_center.X) + int(x_offset),
                                int(item_center.Y) + int(y_offset))
        if not item_bounds.Contains(offset_position):
            raise AssertionError("click location out of bounds")

        logger.info("item center:" + str(item_center), True, True)
        logger.info("item bounds:" + str(item_bounds), True, True)
        logger.info("click location:" + str(offset_position), True, True)
        Mouse.Instance.Click(offset_position)
