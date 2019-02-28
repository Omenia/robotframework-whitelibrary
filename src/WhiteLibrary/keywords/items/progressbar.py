from TestStack.White.UIItems import ProgressBar
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class ProgressbarKeywords(LibraryComponent):
    @keyword
    def verify_progressbar_value(self, locator, expected):
        """Verifies the value of a progress bar.

        ``locator`` is the locator of the progress bar or ProgressBar item object.
        Locator syntax is explained in `Item locators`.

        ``expected`` is the expected value of the progress bar.
        """
        progressbar = self.state._get_typed_item_by_locator(ProgressBar, locator)
        self.state._verify_value(float(expected), progressbar.Value)

    @keyword
    def get_progressbar_value(self, locator):
        """Returns the value of a progress bar.

        ``locator`` is the locator of the progress bar or ProgressBar item object.
        Locator syntax is explained in `Item locators`.
        """
        progressbar = self.state._get_typed_item_by_locator(ProgressBar, locator)
        return progressbar.Value
