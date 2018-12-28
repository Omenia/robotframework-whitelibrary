from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.UIItems.WindowItems import Window   # noqa: F401
from robot.api import logger


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, window_title):
        """
        Attach WhiteLibrary to a window of already attached application.
        See `Attach Application By Id', `Attach Application By Name´ or
        `Launch application` for more details.

        ``window_title`` is the title of the window.
        """
        self.state.window = self.state.app.GetWindow(window_title)
        logger.console("window {}".format(self.state.window))

    @keyword
    def select_modal_window(self, window_title):
        """
        Select modal window.

        ``window_title`` is the title of the window.
        """
        self.state.window = self.state.window.ModalWindow(window_title)
