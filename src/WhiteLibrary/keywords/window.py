from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.UIItems.WindowItems import Window   # noqa: F401
from robot.api import logger    # noqa: F401


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, window_title):
        """Attach WhiteLibrary to a window of already attached application.

        See `Attach Application By Id`, `Attach Application By Name` or
        `Launch application` for more details.

        ``window_title`` is the title of the window.
        """
        self.state.window = self.state.app.GetWindow(window_title)

    @keyword
    def select_modal_window(self, window_title):
        """Select modal window.

        ``window_title`` is the title of the window.
        """
        self.state.window = self.state.window.ModalWindow(window_title)

    @keyword
    def close_window(self, window_title=None):
        """Closes a window.

        ``window_title`` is the title of the window (optional).

        If title is not given, the currently attached window is closed.
        See `Attach Application By Id`, `Attach Application By Name` or
        `Launch application` for more details.
        """
        if window_title is not None:
            self.state.window = self.state.app.GetWindow(window_title)

        self.state.window.Close()

