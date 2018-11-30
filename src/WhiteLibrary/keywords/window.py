from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.UIItems.WindowItems import Window
from robot.api import logger


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, window_title):
        self.state.window = self.state.app.GetWindow(window_title)
        logger.console("window {}".format(self.state.window))

    @keyword    
    def select_modal_window(self, locator):
        """
        Select modal window by title
        | Arguments | Usage | (M)andatory / (O)ptional |
        | Title | Modal window title | M |
        """
        self.state.window = self.state.window.ModalWindow(locator)
