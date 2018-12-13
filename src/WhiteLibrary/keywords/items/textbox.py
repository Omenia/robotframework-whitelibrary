from TestStack.White.UIItems import TextBox
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword

class TextBoxKeywords(LibraryComponent):
    @keyword
    def input_text_to_textbox(self, locator, text):
        """
        Write text to textbox
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | text | inserted string | M |
        """
        textBox = self.state._get_typed_item_by_locator(TextBox, locator)
        textBox.Text = text

    @keyword
    def verify_text_in_textbox(self, locator, expected):
        """
        Verify text in textbox
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        """
        textbox = self.state._get_typed_item_by_locator(TextBox, locator)
        self.state._verify_value(expected, textbox.Text)
