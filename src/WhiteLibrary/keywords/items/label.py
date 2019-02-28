from TestStack.White.UIItems import Label
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class LabelKeywords(LibraryComponent):
    @keyword
    def verify_label(self, locator, expected):
        """Verifies text of a label.

        ``locator`` is the locator of the label or Label item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected text.
        """
        label = self.state._get_typed_item_by_locator(Label, locator)
        self.state._verify_value(expected, label.Text)

    @keyword
    def get_text_from_label(self, locator):
        """Returns the text of a label.

        ``locator`` is the locator of the label or Label item object.
        Locator syntax is explained in `Item locators`.
        """
        label = self.state._get_typed_item_by_locator(Label, locator)
        return label.Text
