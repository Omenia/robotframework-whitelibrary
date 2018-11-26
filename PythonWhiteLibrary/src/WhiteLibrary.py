import os
import clr
clr.AddReference('System')
clr.AddReference('TestStack.White') #include full path to Dll if required
from System.Drawing import Bitmap
from System.Drawing.Imaging import ImageFormat
from TestStack.White import Desktop
from TestStack.White.UIItems.Finders import SearchCriteria


from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.utils import get_link_path

from keywords import ApplicationKeywords, KeyboardKeywords, WindowKeywords
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
                          WindowKeywords(self)]
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

    def take_desktop_screenshot(self):
        """ Takes a screenshot of the whole desktop and inserts screenshot link to log file.
        Returns
        -------
        string
            path to the screenshot file
        """
        filepath = self._get_screenshot_path("whitelib_screenshot_{index}.png")
        logger.info(get_link_path(filepath, self._log_directory), also_console=True)
        logger.info(
            '</td></tr><tr><td colspan="3">''<a href="{src}"><img src="{src}" width="800px"></a>'.format(
                src=get_link_path(filepath, self._log_directory)), html=True)
        bmp = Desktop.CaptureScreenshot()
        bmp.Save(filepath, ImageFormat.Png)
        return filepath

    def take_screenshots_on_failure(self, status):
        """ Disable or enable automatic screenshot creation on failure.
        Parameters
        ----------
        status: bool or str
            True or False, boolean or string, case insensitive. """
        if (str(status).lower() == 'false'):
            self.screenshots_enabled = False
        else:
            self.screenshots_enabled = True

    @property
    def _log_directory(self):
        try:
            logfile = BuiltIn().get_variable_value('${LOG FILE}')
            if logfile is None:
                return BuiltIn().get_variable_value('${OUTPUTDIR}')
            return os.path.dirname(logfile)
        except RobotNotRunningError:
            return os.getcwdu() if PY2 else os.getcwd()

    def _get_screenshot_path(self, filename):
        directory = self._log_directory
        filename = filename.replace('/', os.sep)
        index = 0
        while True:
            index += 1
            formatted = filename.format(index=index)
            filepath = os.path.join(directory, formatted)
            # filename didn't contain {index} or unique path was found
            if formatted == filename or not os.path.exists(filepath):
                return filepath

    def _end_keyword(self, name, attrs):
        if attrs['status'] == 'FAIL':
            if self.screenshot_type == 'desktop' and self.screenshots_enabled:
                self.take_desktop_screenshot()

    def _verify_value(self, expected, actual):
        if expected != actual:
            raise AssertionError("Expected value {}, but found {}".format(expected, actual))
