from TestStack.White.UIItems import TextBox
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword

class TextBoxKeywords(LibraryComponent):
    @keyword
    def input_text_to_textbox(self, locator, text):
        """
        Writes text to a textbox.

        ``locator`` is the locator of the text box.

        ``text`` is the text to write.
        """
        textBox = self.state._get_typed_item_by_locator(TextBox, locator)
        textBox.Text = text

    @keyword
    def verify_text_in_textbox(self, locator, expected):
        """
        Verifies text in a text box.
        
        ``locator`` is the locator of the text box.

        ``expected`` is the expected text of the text box.
        """
        textbox = self.state._get_typed_item_by_locator(TextBox, locator)
        self.state._verify_value(expected, textbox.Text)
