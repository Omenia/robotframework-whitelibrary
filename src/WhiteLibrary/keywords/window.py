from robot.api import logger    # noqa: F401 #pylint: disable=unused-import
from TestStack.White.Configuration import CoreAppXmlConfiguration
from TestStack.White import AutomationException
from TestStack.White.UIItems.WindowItems import DisplayState   # noqa: F401
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, window_title):
        """Attach WhiteLibrary to a window of already attached application.

        See `Attach Application By Id`, `Attach Application By Name` or
        `Launch application` for more details.

        ``window_title`` is the title of the window.
        """

        self.state.window = self._get_window(window_title)

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
    def maximize_window(self, window_title=None):
        """Maximizes a window.

        ``window_title`` is the title of the window (optional).

        If title is not given, the currently attached window is maximized.
        See `Attach Window` for more details.
        """
        if window_title is not None:
            window = self._get_window(window_title)
        else:
            window = self.state.window
        window.DisplayState = DisplayState.Maximized

    @keyword
    def window_should_be_maximized(self, window_title=None):
        """Verifies that window is maximized

        ``window_title`` is the title of the window (optional).

        If title is not given, currently attached window status is queried.
        See `Attach Window` for more details.
        """
        if window_title is not None:
            window = self._get_window(window_title)
        else:
            window = self.state.window
        if window.DisplayState != DisplayState.Maximized:
            raise AssertionError("Expected window state to be maximized, but found {}".format(str(window.DisplayState)))

    @keyword
    def minimize_window(self, window_title=None):
        """Minimizes a window.

        ``window_title`` is the title of the window (optional).

        If title is not given, the currently attached window is minimized.
        See `Attach Window` for more details.
        """
        if window_title is not None:
            window = self._get_window(window_title)
        else:
            window = self.state.window
        window.DisplayState = DisplayState.Minimized

    @keyword
    def window_should_be_minimized(self, window_title=None):
        """Verifies that window is minimized

        ``window_title`` is the title of the window (optional).

        If title is not given, currently attached window status is queried.
        See `Attach Window` for more details.
        """
        if window_title is not None:
            window = self._get_window(window_title)
        else:
            window = self.state.window
        if window.DisplayState != DisplayState.Minimized:
            raise AssertionError("Expected window state to be minimized, but found {}".format(str(window.DisplayState)))

    @keyword
    def restore_window(self, window_title=None):
        """Restores a window.

        ``window_title`` is the title of the window (optional).

        If title is not given, the currently attached window is restored.
        See `Attach Window` for more details.
        """
        if window_title is not None:
            window = self._get_window(window_title)
        else:
            window = self.state.window
        window.DisplayState = DisplayState.Restored

    @keyword
    def window_should_be_restored(self, window_title=None):
        """Verifies that window is restored

        ``window_title`` is the title of the window (optional).

        If title is not given, currently attached window status is queried.
        See `Attach Window` for more details.
        """
        if window_title is not None:
            window = self._get_window(window_title)
        else:
            window = self.state.window
        if window.DisplayState != DisplayState.Restored:
            raise AssertionError("Expected window state to be restored, but found {}".format(str(window.DisplayState)))

    def _get_window(self, window_title):
        try:
            return self.state.app.GetWindow(window_title)
        except AutomationException as error_msg:
            error_msg = str(error_msg)
            replaced_text = "after waiting for {0} seconds".format(int(CoreAppXmlConfiguration.Instance.FindWindowTimeout / 1000))
            raise AutomationException(error_msg.replace("after waiting for 30 seconds", replaced_text), "")
        except AttributeError as error_msg:
            error_msg = str(error_msg)
            if "NoneType" in error_msg:
                error_msg = "No application attached."
            raise AttributeError(error_msg)
