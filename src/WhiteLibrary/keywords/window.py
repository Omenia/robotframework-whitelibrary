from System.Windows import Automation
from TestStack.White.Configuration import CoreAppXmlConfiguration
from TestStack.White import AutomationException, Desktop
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.UIItems.WindowItems import Window   # noqa: F401
from TestStack.White.UIItems.Finders import SearchCriteria    # noqa: E402
from TestStack.White.Factory import InitializeOption    # noqa: E402
from robot.api import logger    # noqa: F401


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, locator):
        """Attach WhiteLibrary to a window of already attached application.

        See `Attach Application By Id`, `Attach Application By Name` or
        `Launch application` for more details.

        ``locator`` is the locator of the window. TODO: Documentation for window locators.
        """
        if isinstance(locator, Window):
            self.state.window = locator
        else:
            self.state.window = self._get_window(locator)

    @keyword
    def list_application_windows(self):
        """Returns a list of all main windows in belonging to an application. Does not return modal windows."""
        return list(self.state.app.GetWindows())

    @keyword
    def list_desktop_windows(self):
        """Returns a list of all main windows on the desktop. Does not return modal windows."""
        return list(Desktop.Instance.Windows())

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
        See `Attach Window` for more details.
        """
        if window_title is not None:
            window = self._get_window(window_title)
            window.Close()
        else:
            self.state.window.Close()

    @keyword
    def window_title_should_be(self, expected):
        """"""
        self.state._verify_string_value(expected, self.state.window.Title)

    @keyword
    def window_title_should_contain(self, expected):
        """"""
        self.state._contains_string_value(expected, self.state.window.Title)

    @keyword
    def get_window_title(self):
        """Returns title of the currently attached window.

        Assumes that a window is attached.
        """
        return self.state.window.Title

    def _get_window(self, locator):
        search_strategy, locator_value = self._parse_window_locator(locator)
        try:
            if search_strategy == "title":
                return self.state.app.GetWindow(locator_value)
            if search_strategy == "id":
                search_criteria = getattr(SearchCriteria, "ByAutomationId")(locator_value)
                return self.state.app.GetWindow(search_criteria, InitializeOption.NoCache)
            if search_strategy == "class_name":
                search_criteria = getattr(SearchCriteria, "ByClassName")(locator_value)
                return self.state.app.GetWindow(search_criteria, InitializeOption.NoCache)
            raise ValueError("'{}' is not a valid window locator prefix".format(search_strategy))
        except AutomationException as error_msg:
            error_msg = str(error_msg)
            replaced_text = "after waiting for {0} seconds".format(CoreAppXmlConfiguration.Instance.FindWindowTimeout/1000)
            raise AutomationException(error_msg.replace("after waiting for 30 seconds", replaced_text), "")
        except AttributeError as error_msg:
            error_msg = str(error_msg)
            if "NoneType" in error_msg:
                error_msg = "No application attached."
            raise AttributeError(error_msg)

    def _parse_window_locator(self, locator):
        if ":" not in locator:
            locator = "title:" + locator
        idx = locator.index(":")
        return locator[:idx], locator[idx+1:]
