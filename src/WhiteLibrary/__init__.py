import clr
import os
dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'TestStack.White.dll')
clr.AddReference('System')
clr.AddReference(dll_path)
from TestStack.White.UIItems.Finders import SearchCriteria

from robot.api import logger

from WhiteLibrary.keywords import ApplicationKeywords, KeyboardKeywords, WindowKeywords, ScreenshotKeywords
from WhiteLibrary.keywords.items import (ButtonKeywords, 
                            LabelKeywords,
                            ListKeywords, 
                            MenuKeywords,
                            ProgressbarKeywords,
                            SliderKeywords,
                            TabKeywords,
                            TreeKeywords, 
                            TextBoxKeywords,
                            UiItemKeywords)
from WhiteLibrary.keywords.robotlibcore import DynamicCore

STRATEGIES = {"id": "ByAutomationId",
              "text": "ByText",
              "index": "Indexed"}


class WhiteLibrary(DynamicCore):
    ROBOT_LIBRARY_SCOPE = "Global"
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.app = None
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
                self.screenshooter.take_desktop_screenshot()

    def _verify_value(self, expected, actual):
        if expected != actual:
            raise AssertionError("Expected value {}, but found {}".format(expected, actual))
