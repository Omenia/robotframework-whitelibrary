from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from TestStack.White.Configuration import CoreAppXmlConfiguration
from TestStack.White import AutomationException
from TestStack.White.Factory import InitializeOption  # noqa: E402
from TestStack.White.UIItems.Finders import SearchCriteria  # noqa: E402
from TestStack.White.UIItems.WindowItems import Window   # noqa: F401

WINDOW_STRATEGIES = {"id": "ByAutomationId",
                     "class_name": "ByClassName"}

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

        #Temporarily replace find window timeout to shorter time in case message box does not exist
        old_find_window_timeout = CoreAppXmlConfiguration.Instance.FindWindowTimeout
        CoreAppXmlConfiguration.Instance.FindWindowTimeout = 500
        try:
            window.MessageBox(expected)
            CoreAppXmlConfiguration.Instance.FindWindowTimeout = old_find_window_timeout
        except AutomationException:
            CoreAppXmlConfiguration.Instance.FindWindowTimeout = old_find_window_timeout
            raise AssertionError("Did not find message box with title {0}".format(str(expected)))

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
                CoreAppXmlConfiguration.Instance.FindWindowTimeout / 1000.0)
            raise AutomationException(error_msg.replace("after waiting for 30 seconds", replaced_text), "")

    def _parse_window_locator(self, locator):  # pylint: disable=no-self-use
        if ":" not in locator:
            locator = "title:" + locator
        idx = locator.index(":")
        return locator[:idx], locator[(idx + 1):]
