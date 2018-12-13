from TestStack.White.UIItems import ProgressBar
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class ProgressbarKeywords(LibraryComponent):
    @keyword
    def verify_progressbar_value(self, locator, expected):
        """
        Verify progressbar value
        | Arguments | Usage | (M)andatory / (O)ptional |
        | locator | element id | M |
        | expected | expected value | M |
        """
        progressbar = self.state._get_typed_item_by_locator(ProgressBar, locator)
        self.state._verify_value(float(expected), progressbar.Value)
