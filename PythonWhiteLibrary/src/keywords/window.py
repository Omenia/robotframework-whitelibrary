from librarycomponent import LibraryComponent
from robotlibcore import keyword
from TestStack.White.UIItems.WindowItems import Window
from robot.api import logger


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, window_title):
        self.window = self.state.app.GetWindow(window_title)
        logger.console("window {}".format(self.window))
