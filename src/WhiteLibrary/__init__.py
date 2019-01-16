import clr
import os
from robot.api import logger    # noqa: F401
dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'TestStack.White.dll')
clr.AddReference('System')
clr.AddReference(dll_path)
from System.Windows.Automation import AutomationElement, ControlType    # noqa: E402
from TestStack.White.UIItems.Finders import SearchCriteria    # noqa: E402
from WhiteLibrary.keywords import ApplicationKeywords, KeyboardKeywords, WindowKeywords, ScreenshotKeywords    # noqa: E402
from WhiteLibrary.keywords.items import (ButtonKeywords,
                            LabelKeywords,
                            ListKeywords,
                            MenuKeywords,
                            ProgressbarKeywords,
                            SliderKeywords,
                            TabKeywords,
                            TimeoutKeywords,
                            TreeKeywords,
                            TextBoxKeywords,
                            UiItemKeywords)   # noqa: E402
from WhiteLibrary.keywords.robotlibcore import DynamicCore   # noqa: E402
from WhiteLibrary import version   # noqa: E402


STRATEGIES = dict(id={"method": "ByAutomationId"},
                  text={"method": "ByText"},
                  index={"method": "Indexed"},
                  help_text={"method": "ByNativeProperty", "property": "HelpTextProperty"},
                  class_name={"method": "ByClassName"},
                  control_type={"method": "ByControlType"})


class WhiteLibrary(DynamicCore):
    """WhiteLibrary is a Robot Framework library for automating Windows GUI.
    It is a wrapper for [https://github.com/TestStack/White | TestStack.White].

    = Applications and windows =
    To interact with UI items, the correct application and window must be attached to WhiteLibrary.

    When application is started with `Launch Application`, the keyword also attaches the application to WhiteLibrary.
    Attaching a running application is done with `Attach Application By Name` or `Attach Application By Id`.

    Once the application is attached, the window to interact with is attached with `Attach Window`.

    Examples:

    | # Launch application, no separate step for attaching application needed | |
    | `Launch Application` | C:/myApplication.exe |
    | `Attach Window`      | Main window |
    | | |
    | # Switch to an application that is already running | |
    | `Attach Application By Name` | calc1 |
    | `Attach Window`              | Calculator |

    = UI items =
    Keywords in WhiteLibrary use the same names for control types that are used in White.
    See [https://teststackwhite.readthedocs.io/en/latest/UIItems | White's documentation] for details about mapping
    UIA Control Types to classes in White.

    == Item locators ==
    Keywords that access UI items (e.g. `Click Button`) use a ``locator`` argument.
    The locator consists of a locator prefix that specifies the search criteria, and the locator value.

    The following locator prefixes are available:

    | = Prefix =        | = Description =                    |
    | id (or no prefix) | Search by AutomationID. If no prefix is given, the item is searched by AutomationID by default. |
    | text              | Search by exact item text or name. |
    | index             | Search by item index.              |
    | help_text         | Search by HelpTextProperty.        |
    | class_name        | Search by class name.              |
    | control_type      | Search by control type.            |

    Examples:

    | `Click Button` | myButton         | # clicks button by its AutomationID |
    | `Click Button` | id=myButton      | # clicks button by its AutomationID |
    | `Click Button` | text=Click here! | # clicks button by the button text  |
    | `Click Button` | index=2          | # clicks button whose index is 2    |
    """
    ROBOT_LIBRARY_VERSION = version.VERSION
    ROBOT_LIBRARY_SCOPE = "Global"
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.window = None
        self.screenshooter = None
        self.ROBOT_LIBRARY_LISTENER = self
        self.screenshot_type = 'desktop'
        self.screenshots_enabled = True
        self.libraries = [ApplicationKeywords(self),
                          ButtonKeywords(self),
                          KeyboardKeywords(self),
                          LabelKeywords(self),
                          ListKeywords(self),
                          MenuKeywords(self),
                          ProgressbarKeywords(self),
                          SliderKeywords(self),
                          TabKeywords(self),
                          TimeoutKeywords(self),
                          TextBoxKeywords(self),
                          TreeKeywords(self),
                          UiItemKeywords(self),
                          WindowKeywords(self),
                          ScreenshotKeywords(self)]
        DynamicCore.__init__(self, self.libraries)

    def _get_typed_item_by_locator(self, item_type, locator):
        search_criteria = self._get_search_criteria(locator)
        return self.window.Get[item_type](search_criteria)

    def _get_item_by_locator(self, locator):
        search_criteria = self._get_search_criteria(locator)
        return self.window.Get(search_criteria)

    def _get_multiple_items_by_locator(self, locator):
        search_criteria = self._get_search_criteria(locator)
        return self.window.GetMultiple(search_criteria)

    def _get_search_criteria(self, locator):
        if "=" not in locator:
            locator = "id=" + locator

        search_strategy, locator_value = locator.split("=", 1)
        if search_strategy == "index":
            locator_value = int(locator_value)

        try:
            search_method = STRATEGIES[search_strategy]["method"]
        except KeyError:
            raise ValueError("'{}' is not a valid locator prefix".format(search_strategy))

        if search_method == "ByNativeProperty":
            property_name = STRATEGIES[search_strategy]["property"]
            property_name = getattr(AutomationElement, property_name)
            search_params = (property_name, locator_value)
        else:
            if search_method == "ByControlType":
                locator_value = getattr(ControlType, locator_value)
            search_params = (locator_value,)

        method = getattr(SearchCriteria, search_method)
        return method(*search_params)

    def _end_keyword(self, name, attrs):
        if attrs['status'] == 'FAIL':
            if self.screenshot_type == 'desktop' and self.screenshots_enabled:
                self.screenshooter.take_desktop_screenshot()

    def _contains_string_value(self, expected, actual, case_sensitive=True):
        expected_value = expected if not case_sensitive else expected.upper()
        actual_value = actual if not case_sensitive else actual.upper()

        if expected_value not in actual_value:
            raise AssertionError("Expected value {} not found in {}".format(expected, actual))

    def _verify_string_value(self, expected, actual, case_sensitive=True):
        expected_value = expected if not case_sensitive else expected.upper()
        actual_value = actual if not case_sensitive else actual.upper()

        if expected_value != actual_value:
            raise AssertionError("Expected value {}, but found {}".format(expected, actual))

    def _verify_value(self, expected, actual):
        if expected != actual:
            raise AssertionError("Expected value {}, but found {}".format(expected, actual))
