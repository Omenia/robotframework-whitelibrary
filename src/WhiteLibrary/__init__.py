# pylint: disable=invalid-name
import os
from robot.utils import is_truthy
import clr
DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'TestStack.White.dll')
clr.AddReference('System')
clr.AddReference(DLL_PATH)
from System.Windows.Automation import AutomationElement, ControlType    # noqa: E402
from TestStack.White.UIItems.Finders import SearchCriteria    # noqa: E402
from TestStack.White.UIItems import UIItem    # noqa: E402
from WhiteLibrary.keywords import (ApplicationKeywords, KeyboardKeywords, MouseKeywords,
                                   WindowKeywords, ScreenshotKeywords, WhiteConfigurationKeywords)    # noqa: E402
from WhiteLibrary.keywords.items import (ButtonKeywords,
                                         LabelKeywords,
                                         ListKeywords,
                                         ListViewKeywords,
                                         MenuKeywords,
                                         ProgressbarKeywords,
                                         SliderKeywords,
                                         TabKeywords,
                                         ToolStripKeywords,
                                         TreeKeywords,
                                         TextBoxKeywords,
                                         UiItemKeywords)   # noqa: E402
from WhiteLibrary.keywords.robotlibcore import DynamicCore   # noqa: E402
from WhiteLibrary import version   # noqa: E402


STRATEGIES = dict(id={"method": "ByAutomationId"},  # noqa: C408
                  text={"method": "ByText"},
                  index={"method": "Indexed"},
                  help_text={"method": "ByNativeProperty", "property": "HelpTextProperty"},
                  class_name={"method": "ByClassName"},
                  control_type={"method": "ByControlType"})


class WhiteLibrary(DynamicCore):
    """WhiteLibrary is a Robot Framework library for automating Windows GUI.

    It is a wrapper for [https://github.com/TestStack/White | TestStack.White] automation framework, which is based on
    [https://docs.microsoft.com/en-us/windows/desktop/WinAuto/entry-uiauto-win32 | Microsoft UI Automation API] (UIA).

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
    WhiteLibrary uses the same names for UI items (=controls) as White.
    See [https://teststackwhite.readthedocs.io/en/latest/UIItems | White's documentation] for details about mapping
    UIA control types to White's UI item classes.

    For example, the UIA control type ``Text`` maps to the ``Label`` class in White (e.g. in WhiteLibrary's keyword `Verify Label`).

    == Item locators ==
    Keywords that access UI items (e.g. `Click Button`) use a ``locator`` argument.
    The locator consists of a locator prefix that specifies the search criteria, and the locator value.

    Locator syntax is ``prefix:value``.
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
    | `Click Button` | id:myButton      | # clicks button by its AutomationID |
    | `Click Button` | text:Click here! | # clicks button by the button text  |
    | `Click Button` | index:2          | # clicks button whose index is 2    |

    *Note:* Old locator syntax ``prefix=value`` is also valid but it is recommended to use the ``prefix:value`` syntax
    since the old syntax *will be deprecated* in the future.

    == Item object as a locator ==
    It is also possible to use an item object reference as the ``locator`` value.
    An item object can be obtained with e.g. `Get Item` or `Get Items` keywords.

    The need to use an item object reference can arise for instance when multiple items match the same locator
    and one of the items is selected for further action.
    When using an item object, the action on the item can be executed regardless of the window it is in,
    i.e. the window where the item is located does not necessarily need to be attached.
    However, this does not change the attached window and the operation continues in the attached window after action on
    the referred item is complete.

    Example using item object:
    | @{my_buttons}= | `Get Items`         | class_name:MyButtonClass |
    | `Click Button` | ${my_buttons[2]}    | # clicks button object at index 2 of the list |

    = Workflow example =
    | ***** Variables *****   | | | |
    | ${TEST APPLICATION}     | C:/path/to/my_application.exe | | |
    | | | | |
    | ***** Settings *****    | | | |
    | Library | WhiteLibrary  | | |
    | | | | |
    | ***** Test Cases *****  | | | |
    | Small Example           | | | |
    | | Launch Application    | ${TEST APPLICATION} | |
    | | Attach Window         | Window Title        | |
    | | Button Text Should Be | my_button           | press this button |
    | | Click Button          | my_button | |
    | | Close Application     | | |

    = Waiting and timeouts =
    White handles a lot of the required waiting automatically, including waiting while the window is busy and
    waiting for a window to appear.

    White's internal waits use timeouts that can be read and configured with keywords:
    - BusyTimeout defines how long to wait while the window is busy,
      see `Get White Busy Timeout`, `Set White Busy Timeout`
    - FindWindowTimeout defines how long to wait until the specified window is found,
     see `Get White Find Window Timeout`, `Set White Find Window Timeout`.

    In situations that require additional waiting for UI items, see keywords `Wait Until Item Exists`
    and `Wait Until Item Does Not Exist`.

    """

    ROBOT_LIBRARY_VERSION = version.VERSION
    ROBOT_LIBRARY_SCOPE = "Global"
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, screenshot_dir=None):
        """WhiteLibrary can be imported with an optional argument ``screenshot_dir``.

        ``screenshot_dir`` is the directory where screenshots taken by WhiteLibrary are saved.
        If the given directory does not already exist, it will be created when the first screenshot is taken.
        The directory can also be set at runtime with `Set Screenshot Directory`.
        If the argument is not given, the default location for screenshots is the output directory of the Robot run,
        i.e. the directory where output and log files are generated.
        """
        self.app = None
        self.window = None
        self.screenshooter = None
        self.ROBOT_LIBRARY_LISTENER = self  # pylint: disable=invalid-name
        self.screenshots_enabled = True
        self.libraries = [ApplicationKeywords(self),
                          ButtonKeywords(self),
                          KeyboardKeywords(self),
                          LabelKeywords(self),
                          ListKeywords(self),
                          ListViewKeywords(self),
                          MenuKeywords(self),
                          MouseKeywords(self),
                          ProgressbarKeywords(self),
                          SliderKeywords(self),
                          TabKeywords(self),
                          WhiteConfigurationKeywords(self),
                          TextBoxKeywords(self),
                          ToolStripKeywords(self),
                          TreeKeywords(self),
                          UiItemKeywords(self),
                          WindowKeywords(self),
                          ScreenshotKeywords(self, screenshot_dir)]
        DynamicCore.__init__(self, self.libraries)

    def _get_typed_item_by_locator(self, item_type, locator):
        if isinstance(locator, UIItem):
            if not isinstance(locator, item_type):
                raise TypeError("Item object was not of the expected type")
            return locator
        search_criteria = self._get_search_criteria(locator)
        return self.window.Get[item_type](search_criteria)

    def _get_item_by_locator(self, locator):
        if isinstance(locator, UIItem):
            return locator
        search_criteria = self._get_search_criteria(locator)
        return self.window.Get(search_criteria)

    def _get_multiple_items_by_locator(self, locator):
        search_criteria = self._get_search_criteria(locator)
        return self.window.GetMultiple(search_criteria)

    def _get_search_criteria(self, locator):
        search_strategy, locator_value = self._parse_locator(locator)
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

    def _parse_locator(self, locator):
        if "=" not in locator and ":" not in locator:
            locator = "id:" + locator
        idx = self._get_locator_delimiter_index(locator)
        return locator[:idx], locator[idx + 1:]

    @staticmethod
    def _get_locator_delimiter_index(locator):
        if "=" not in locator:
            return locator.index(":")
        if ":" not in locator:
            return locator.index("=")
        return min(locator.index(":"), locator.index("="))

    def _end_keyword(self, name, attrs):  # pylint: disable=unused-argument
        if attrs['status'] == 'FAIL':
            if self.screenshots_enabled:
                self.screenshooter.take_desktop_screenshot()

    @staticmethod
    def _contains_string_value(expected, actual, case_sensitive=True):
        case_sensitive = is_truthy(case_sensitive)
        expected_value = expected if case_sensitive else expected.upper()
        actual_value = actual if case_sensitive else actual.upper()
        if expected_value not in actual_value:
            raise AssertionError(u"Expected value {} not found in {}".format(expected, actual))

    @staticmethod
    def _verify_string_value(expected, actual, case_sensitive=True):
        case_sensitive = is_truthy(case_sensitive)
        expected_value = expected if case_sensitive else expected.upper()
        actual_value = actual if case_sensitive else actual.upper()
        if expected_value != actual_value:
            raise AssertionError(u"Expected value {}, but found {}".format(expected, actual))

    @staticmethod
    def _verify_value(expected, actual):
        if expected != actual:
            raise AssertionError(u"Expected value {}, but found {}".format(expected, actual))
