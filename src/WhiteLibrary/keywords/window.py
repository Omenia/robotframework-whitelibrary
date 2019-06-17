from System import Enum
from TestStack.White import AutomationException, Desktop
from TestStack.White.Configuration import CoreAppXmlConfiguration
from TestStack.White.Factory import InitializeOption  # noqa: E402
from TestStack.White.UIItems.Finders import SearchCriteria  # noqa: E402
from TestStack.White.UIItems.WindowItems import DisplayState, Window  # noqa: F401
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword

WINDOW_STRATEGIES = {"id": "ByAutomationId", "class_name": "ByClassName"}


class WindowKeywords(LibraryComponent):
    @keyword
    def attach_window(self, locator):
        """Attaches WhiteLibrary to a window.

        ``locator`` is the locator of the window or a window object.

        === Window locator syntax ===
        Syntax for a window locator is ``prefix:value``.

        When the locator syntax is used, the window is searched from the currently attached application.
        See `Attach Application By Id`, `Attach Application By Name` or
        `Launch application` for more details about attaching an application.

        The following window locators are available:
        | = Prefix =           | = Description =         |
        | title (or no prefix) | Search by the exact window title. If no prefix is given, the window is searched by title by default. |
        | id                   | Search by AutomationID. |
        | class_name           | Search by class name.   |

        Examples:
        | Attach Window | Main Window                   | # attach window with title         |
        | Attach Window | id:mainWindow                 | # attach window with Automation ID |
        | Attach Window | class_name:NavigationWindow   | # attach window with ClassName     |

        === Window objects ===
        A window can also be attached by directly passing the window object as the ``locator`` parameter value.
        This may be useful if the correct window cannot be found by using the window locator syntax.

        Example:
        | @{windows} | `Get Application Windows` | |
        | Attach Window | ${windows[1]} | # attach window at index 1 in window list |

        When using a window object as the ``locator`` parameter value, the window is attached even if it does not
        belong to the currently attached application.
        Note that when attaching a window that belongs to a different application than the currently attached one,
        attaching the window does not affect what application is attached to the library.

        """
        self.state.window = self._get_window(locator)

    @keyword
    def close_window(self, locator=None):
        """Closes a window.

        ``locator`` is the locator of the window or a window object (optional).

        If no ``locator`` value is given, the currently attached window is closed.
        See `Attach Window` for details about window locators and attaching a window.
        """
        if locator is not None:
            window = self._get_window(locator)
            window.Close()
        else:
            self.state.window.Close()

    @keyword
    def get_application_windows(self):
        """Returns a list of windows belonging to the currently attached application.

        Assumes that an application is attached.
        See `Attach Application By Name` and `Attach Application By Id` for details.
        """
        return list(self.state.app.GetWindows())

    @staticmethod
    @keyword
    def get_desktop_windows():
        """Returns a list of windows on the desktop."""
        return list(Desktop.Instance.Windows())

    @keyword
    def get_window_title(self):
        """Returns title of the currently attached window.

        Assumes that a window is attached. See `Attach Window` for details.
        """
        return self.state.window.Title

    @keyword
    def select_modal_window(self, window_title):
        """Attaches a modal window.

        ``window_title`` is the title of the window.
        """
        self.state.window = self.state.window.ModalWindow(window_title)

    @keyword
    def window_title_should_be(self, expected):
        """Verifies that the title of the currently attached window is ``expected``.

        Assumes that a window is attached. See `Attach Window` for details.
        """
        self.state._verify_string_value(expected, self.state.window.Title)

    @keyword
    def window_title_should_contain(self, expected):
        """Verifies that the title of the currently attached window contains text ``expected``.

        Assumes that a window is attached. See `Attach Window` for details.
        """
        self.state._contains_string_value(expected, self.state.window.Title)

    @keyword
    def maximize_window(self, locator=None):
        """Maximizes a window.

        ``locator`` is the locator of the window or a window object (optional).

        If no ``locator`` value is given, the currently attached window is maximized.
        See `Attach Window` for details about attaching a window and window locator syntax.
        """
        if locator is not None:
            window = self._get_window(locator)
        else:
            window = self.state.window
        window.DisplayState = DisplayState.Maximized

    @keyword
    def minimize_window(self, locator=None):
        """Minimizes a window.

        ``locator`` is the locator of the window or a window object (optional).

        If no ``locator`` value is given, the currently attached window is minimized.
        See `Attach Window` for details about attaching a window and window locator syntax.
        """
        if locator is not None:
            window = self._get_window(locator)
        else:
            window = self.state.window
        window.DisplayState = DisplayState.Minimized

    @keyword
    def restore_window(self, window_title=None):
        """Restores a window.

        ``locator`` is the locator of the window or a window object (optional).

        If no ``locator`` value is given, the currently attached window is restored.
        See `Attach Window` for details about attaching a window and window locator syntax.
        """
        if window_title is not None:
            window = self._get_window(window_title)
        else:
            window = self.state.window
        window.DisplayState = DisplayState.Restored

    @keyword
    def window_should_be_maximized(self, locator=None):
        """Verifies that a window is maximized.

        ``locator`` is the locator of the window or a window object (optional).

        If no ``locator`` value is given, the status of the currently attached window is verified.
        See `Attach Window` for details about attaching a window and window locator syntax.
        """
        self._verify_window_state("Maximized", locator)

    @keyword
    def window_should_be_minimized(self, locator=None):
        """Verifies that a window is minimized.

        ``locator`` is the locator of the window or a window object (optional).

        If no ``locator`` value is given, the status of the currently attached window is verified.
        See `Attach Window` for details about attaching a window and window locator syntax.
        """
        self._verify_window_state("Minimized", locator)

    @keyword
    def window_should_be_restored(self, locator=None):
        """Verifies that a window is restored.

        ``locator`` is the locator of the window or a window object (optional).

        If title is not given, currently attached window status is queried.
        See `Attach Window` for more details.
        """
        self._verify_window_state("Restored", locator)

    def _verify_window_state(self, expected_state, locator):
        if locator is not None:
            window = self._get_window(locator)
        else:
            window = self.state.window
        actual_state = window.DisplayState
        if actual_state != getattr(DisplayState, expected_state):
            raise AssertionError("Expected window state to be {}, but found {} ({})"
                                 .format(expected_state, self._window_state_to_str(actual_state), actual_state))

    def _get_window(self, locator):
        if isinstance(locator, Window):
            return locator
        return self._get_window_by_locator(locator)

    def _get_window_by_locator(self, locator):
        search_strategy, locator_value = self._parse_window_locator(locator)
        try:
            if search_strategy == "title":
                return self.state.app.GetWindow(locator_value)
            search_criteria = getattr(SearchCriteria, WINDOW_STRATEGIES[search_strategy])(locator_value)
            return self.state.app.GetWindow(search_criteria, InitializeOption.NoCache)
        except KeyError:
            raise ValueError("'{}' is not a valid locator prefix for a window".format(search_strategy))
        except AttributeError as error_msg:
            error_msg = str(error_msg)
            if "NoneType" in error_msg:
                error_msg = "No application attached."
            raise AttributeError(error_msg)
        except AutomationException as error_msg:
            error_msg = str(error_msg)
            replaced_text = "after waiting for {0} seconds".format(
                CoreAppXmlConfiguration.Instance.FindWindowTimeout / 1000.0
            )
            raise AutomationException(error_msg.replace("after waiting for 30 seconds", replaced_text), "")

    @staticmethod
    def _parse_window_locator(locator):
        if ":" not in locator:
            locator = "title:" + locator
        idx = locator.index(":")
        return locator[:idx], locator[(idx + 1):]

    @staticmethod
    def _window_state_to_str(state):
        return Enum.GetName(DisplayState, state)
