from TestStack.White.UIItems import Label
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class LabelKeywords(LibraryComponent):
    @keyword
    def verify_label(self, locator, expected):
        """
        Verify text in label
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | actual | expected text | M |
        """
        label = self.state._get_typed_item_by_locator(Label, locator)
        self.state._verify_value(expected, label.Text)
