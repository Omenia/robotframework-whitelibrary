from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.UIItems.WindowItems import Window
from TestStack.White import Desktop
from robot.api import logger


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, window_title):
        """
        Attaches WhiteLibrary to a window.

        ``window_title`` is the title of the window.
        """
        self.state.window = self.state.app.GetWindow(window_title)
        logger.debug("Attached to window {}".format(self.state.window))

    @keyword
    def list_application_windows(self):
        """
        Returns a list of all main windows in belonging to an application. Does not return modal windows.
        """
        return list(self.state.app.GetWindows())

    @keyword
    def attach_window_by_index(self, window_index):
        """
        Attaches WhiteLibrary to a window by its index.

        ``window_index`` is the index of the window.
        """
        self.state.window = self.state.app.GetWindows()[window_index]
        logger.debug("Attached to window {}".format(self.state.window))

    @keyword
    def list_desktop_windows(self):
        """
        Returns a list of all main windows on the desktop. Does not return modal windows.
        """
        return list(Desktop.Instance.Windows())

    @keyword
    def attach_desktop_window_by_name(self, name):
        """
        Attaches WhiteLibrary to a window by its name.

        ``name`` is the name of the window.
        """
        for win in Desktop.Instance.Windows():
            if win.Name == name:
                self.state.window = win
                logger.debug("Attached to window {}".format(self.state.window))
                return
        raise AssertionError("Window with name {} not found".format(name))

    @keyword
    def attach_desktop_window_by_id(self, id):
        """
        Attaches WhiteLibrary to a window by its automation id.

        ``id`` is the automation id of the window.
        """
        for win in Desktop.Instance.Windows():
            if win.Id == id:
                self.state.window = win
                logger.debug("Attached to window {}".format(self.state.window))
                return
        raise AssertionError("Window with id {} not found".format(id))

    @keyword
    def list_modal_windows(self):
        """
        Returns a list of modal windows. 
        """
        return list(self.state.window.ModalWindows())

    @keyword    
    def select_modal_window(self, window_title):
        """
        Selects a modal window by its title.
        
        ``window_title`` is the title of the modal window.
        """
        self.state.window = self.state.window.ModalWindow(window_title)
        logger.debug("Selected modal window {}".format(self.state.window))

    @keyword
    def select_modal_window_by_index(self, index):
        """
        Selects a modal windows by index.

        ``index`` is the index of the modal window.
        """
        self.state.window = self.state.window.ModalWindows()[index]
        logger.debug("Selected modal window {}".format(self.state.window))
