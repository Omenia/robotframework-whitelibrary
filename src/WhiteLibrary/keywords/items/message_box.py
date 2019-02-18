from TestStack.White.UIItems.WindowItems import Window
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class MessageBoxKeywords(LibraryComponent):
    @keyword
    def message_box_title_should_be(self, expected, window_title=None):
        """Verifies the title of a message box in a window.

        ``expected`` is the expected title of the message box.

        ``window_title`` is the locator of the window. If no window title is given, currently attached window is used.
        """
        if window_title is not None:
            window = self._get_window(window_title)
        else:
            window = self.state.window
        window.MessageBox(expected)
