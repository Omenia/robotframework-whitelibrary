from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.UIItems.WindowItems import Window
from robot.api import logger


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, window_title):
        """
        Attach WhiteLibrary to a window.

        ``window_title`` is the title of the window.
        """
        self.state.window = self.state.app.GetWindow(window_title)
        logger.console("window {}".format(self.state.window))

    @keyword
    def list_windows(self):
        """
        Returns a list of all main windows in belonging to an application. It doesn't return modal windows.
        """
        return self.state.app.GetWindows()

    @keyword
    def attach_window_by_index(self, window_index):
        """
        Attach WhiteLibrary with the index.

        ``window_index`` is the index of the window.
        """
        self.state.window = self.state.app.GetWindows()[windows_index]
        logger.console("window {}".format(self.state.window))

    @keyword    
    def select_modal_window(self, window_title):
        """
        Select modal window.
        
        ``window_title`` is the title of the window.
        """
        self.state.window = self.state.window.ModalWindow(window_title)
