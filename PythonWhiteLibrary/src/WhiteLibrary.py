import clr
clr.AddReference('System')
clr.AddReference('TestStack.White') #include full path to Dll if required
from TestStack.White.UIItems.Finders import SearchCriteria

from robot.api import logger
#from robot.libraries.BuiltIn import BuiltIn

from keywords import ApplicationKeywords, KeyboardKeywords, WindowKeywords, ScreenshotKeywords
from keywords.items import (ButtonKeywords, 
                            LabelKeywords,
                            ListKeywords, 
                            MenuKeywords,
                            ProgressbarKeywords,
                            SliderKeywords,
                            TabKeywords,
                            TreeKeywords, 
                            TextBoxKeywords,
                            UiItemKeywords)
from keywords.robotlibcore import DynamicCore



STRATEGIES = {"id": "ByAutomationId",
              "text": "ByText",
              "index": "Indexed"}


class WhiteLibrary(DynamicCore):
    ROBOT_LIBRARY_SCOPE = "Global"
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.app = None
        self.window = None
        self.screenshotter = None
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

    def _get_search_criteria(self, locator):
        if "=" not in locator:
            locator = "id=" + locator
        search_strategy, locator_value = locator.split("=")
        if search_strategy == "index":
            locator_value = int(locator_value)
        search_method = STRATEGIES[search_strategy]
        method = getattr(SearchCriteria, search_method)
        return method(locator_value)

    def _end_keyword(self, name, attrs):
        if attrs['status'] == 'FAIL':
            if self.screenshot_type == 'desktop' and self.screenshots_enabled:
                self.screenshotter.take_desktop_screenshot()
                # Alternative solution:
                #BuiltIn().run_keyword("WhiteLibrary.Take Desktop Screenshot")

    def _verify_value(self, expected, actual):
        if expected != actual:
            raise AssertionError("Expected value {}, but found {}".format(expected, actual))
